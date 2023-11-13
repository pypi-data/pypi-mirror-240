"""引擎上下文context类"""

from pathlib import Path
from typing import Union, Optional, Dict, Any
from collections.abc import Mapping
from vxutils.convertors import vxJSONEncoder, to_json, save_json
from vxutils.collections import vxDict

try:
    import simplejson as json
except ImportError:
    import json

__all__ = ["vxContext"]


class vxContext:
    def __init__(
        self,
        settings: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        **kwargs: Dict[str, Any],
    ) -> None:
        self._settings = vxDict()
        self._params = vxDict()

        if settings:
            self.settings.update(settings)

        if params:
            self.params.update(params)

        self.__dict__.update(kwargs)
        self.initialize()

    def initialize(self) -> None:
        """初始化"""
        pass

    def __len__(self) -> int:
        return len(self.params) + len(self.settings) - 2 + len(self.__dict__)

    def __contains__(self, key: str) -> bool:
        return any((key in self.__dict__, key in self.params, key in self.settings))

    def __setitem__(self, key: str, value: object) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key: str) -> None:
        return self.__dict__[key]

    def __str__(self) -> str:
        return f"< {self.__class__.__name__}(id-{id(self)}) : {to_json(self)} >"

    def update(self, *args: Dict[Any, Any], **kwargs: Dict[Any, Any]) -> None:
        """批量更新"""
        self.__dict__.update(*args, **kwargs)

    @property
    def params(self) -> Dict:
        """参数"""
        return self._params

    @property
    def settings(self) -> Dict:
        """设置"""
        return self._settings

    @classmethod
    def load_json(cls, config_file: Union[str, Path]) -> "vxContext":
        """从json文件加载配置"""

        config_file = Path(config_file)
        if not config_file.exists():
            raise OSError(f"config_file({config_file.as_posix()}) is not exists.")

        with open(config_file.as_posix(), "r", encoding="utf-8") as fp:
            config = json.load(fp)
            settings = config.pop("settings", {})
            params = config.pop("params", {})
        return cls(settings=settings, params=params)

    def save_json(self, config_file: Union[str, Path]) -> None:
        """保存配置到json文件"""
        config = {
            "settings": self.settings,
            "params": self.params,
        }
        save_json(config, config_file)


@vxJSONEncoder.register(vxContext)
def _(obj):
    return {"settings": obj.settings, "params": obj.params}
    # return dict(obj.items())


Mapping.register(vxContext)


if __name__ == "__main__":
    context = vxContext.load_json("log/config.json")
    context.hello = "world"

    print(context.params)
    context.settings.id = 1.3
    context.settings.name = "test"
    print(context)
    context.save_json("log/config.json")
    print(len(context))
