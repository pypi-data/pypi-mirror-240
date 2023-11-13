"""api工具箱"""

import importlib
from pathlib import Path
from typing import Union, Dict, Any, Optional, Mapping
from collections.abc import Mapping
from abc import ABC
from vxutils.sched.context import vxContext
from vxutils.convertors import to_json
from vxutils import logger


def import_tools(
    mod_path: Union[str, Path, Any], params: Optional[Dict[str, Any]] = None
) -> Any:
    """导入工具"""

    if params is None:
        params = {}

    cls_or_obj = mod_path
    if isinstance(mod_path, str):
        if mod_path.find(".") > -1:
            class_name = mod_path.split(".")[-1]
            mod_name = ".".join(mod_path.split(".")[:-1])
            mod = importlib.import_module(mod_name)
            cls_or_obj = getattr(mod, class_name)
        else:
            cls_or_obj = importlib.import_module(mod_path)

    return cls_or_obj(**params) if isinstance(cls_or_obj, type) else cls_or_obj


def import_by_config(config: Mapping) -> Any:
    """根据配置文件初始化对象

    配置文件格式:
    config = {
        'class': 'vxsched.vxEvent',
        'params': {
            "type": "helloworld",
            "data": {
                'class': 'vxutils.vxtime',
            },
            "trigger": {
                "class": "vxsched.triggers.vxIntervalTrigger",
                "params":{
                    "interval": 10
                }
            }
        }
    }

    """
    if "class" not in config:
        return config

    mod_path = config["class"]
    params = {
        k: import_by_config(v) if isinstance(v, Mapping) and "class" in v else v
        for k, v in config.get("params", {}).items()
    }

    if isinstance(mod_path, str):
        if mod_path.find(".") < 0:
            cls_or_obj = importlib.import_module(mod_path)
        else:
            class_name = mod_path.split(".")[-1]
            mod_name = ".".join(mod_path.split(".")[:-1])
            mod = importlib.import_module(mod_name)
            cls_or_obj = getattr(mod, class_name)

    return cls_or_obj(**params) if isinstance(cls_or_obj, type) else cls_or_obj


class vxProviderBase(ABC):
    """供应接口基类"""

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        context: vxContext = vxContext()
        self.set_context(context, **kwargs)

    @property
    def context(self) -> vxContext:
        """上下文对象"""
        return self._context

    def set_context(self, context: vxContext, **kwargs: Dict[str, Any]) -> None:
        """设置上下文对象

        Arguments:
            context {vxContext} -- 上下文对象
        """

        self._context: vxContext = context
        self._context.update(kwargs)

    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class vxAPIWrappers:
    """api box"""

    __defaults__: Dict[str, Any] = {}

    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        **providers: Union[str, Dict[str, Any]],
    ) -> None:
        self._context: vxContext = vxContext()
        if config:
            self.set_context(**config)

        _providers = dict(**self.__defaults__)
        _providers.update(**providers)
        self.register_providers(**_providers)

    @property
    def context(self) -> vxContext:
        """上下文管理器"""
        return self._context

    def set_context(self, **config: Dict[str, Any]) -> None:
        """设置上下文管理器"""
        self.context.update(**config)
        for provider in self.__dict__.values():
            if hasattr(provider, "set_context"):
                provider.set_context(self.context)

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]

    def __str__(self) -> str:
        message = {
            name: (
                f"module {tool.__name__}(id-{id(tool)})"
                if hasattr(tool, "__name__")
                else f"class {tool.__class__.__name__}(id-{id(tool)})"
            )
            for name, tool in self.__dict__.items()
        }

        return f"< {self.__class__.__name__} (id-{id(self)}) : {to_json(message)} >"

    def _load_privoder(
        self, provider: Any, providers: Optional[Dict[str, Any]] = None
    ) -> Any:
        """加载当个工具"""
        if providers is None:
            providers = {}

        if isinstance(provider, str) and provider.startswith("@"):
            provider_name = provider[1:]
            if provider_name in self.__dict__:
                return self.__dict__[provider_name]

            elif provider_name in providers:
                return self._load_privoder(providers[provider_name], providers)
            else:
                raise ValueError(f"{provider} is not available. ")

        if not isinstance(provider, dict) or "class" not in provider:
            return provider

        params = provider.get("params", {})
        kwargs = {k: self._load_privoder(v, providers) for k, v in params.items()}
        return import_tools(provider["class"], kwargs)

    def register_providers(self, **providers: Dict[str, Any]) -> Any:
        """注册接口供应商"""
        for name, provider_config in providers.items():
            if not provider_config:
                continue

            if name in self.__dict__:
                logger.warning(
                    "providers({name}) 已注册为: {self.__dict__[name]},忽略更新"
                )
                continue

            try:
                provider = self._load_privoder(provider_config, providers)
                self.__dict__[name] = provider
                if hasattr(provider, "set_context"):
                    provider.set_context(self.context)
                logger.info(f"注册{name}接口成功..")
            except Exception as err:
                logger.error(
                    f"加载provider: {name}({provider_config})出错: {err}", exc_info=True
                )
