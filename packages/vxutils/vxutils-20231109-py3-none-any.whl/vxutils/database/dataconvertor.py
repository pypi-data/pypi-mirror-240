"""数据转换器"""

from typing import Type, Dict, Callable, Any, Tuple, Optional
from collections.abc import MutableMapping
from vxutils import logger
from vxutils.database.fields import _NOTSET


class vxDataConvertor:
    """数据转换器基础类"""

    def __init__(
        self,
        target_cls: Type,
        convertors_mapping: Optional[MutableMapping] = None,
        defaults: Optional[MutableMapping] = None,
    ) -> None:
        self._target_cls = target_cls
        self._convertors: Dict = {}
        self._defaults_data = defaults or {}

        if convertors_mapping is None:
            return

        for target_col, convertor in convertors_mapping.items():
            if callable(convertor):
                self.add_convertors(target_col, convertor)
            else:
                self.rename_columns(convertor, target_col)

    def add_convertors(self, target_col: str, conveter_func: Callable) -> None:
        """设置col的转换函数

        target_col : 待转换的字段名
        convertor_func(other_data) ：转换函数 或者是缺省值，其中other_data 为待转换对象内容
        """
        if not callable(conveter_func):
            raise ValueError(f"func({conveter_func.__name__} is not callable")
        self._convertors[target_col] = conveter_func

    def rename_columns(self, source_col: str, target_col: str) -> None:
        """重命名字段"""

        def _rename_func(other_data: Any) -> Any:
            """重命名转换器"""
            if hasattr(other_data, source_col):
                return getattr(other_data, source_col)
            return other_data[source_col]

        self.add_convertors(target_col, _rename_func)

        # self._convertors[target_col] = _rename_func

    def set_defaults(self, target_col: str, default_value: Any) -> None:
        """设置默认值"""
        self._defaults_data[target_col] = default_value

    def _convert_col(self, col: str, other_data: Any) -> Tuple[str, Any]:
        try:
            if col in self._convertors:
                col_value = self._convertors[col](other_data)
            elif hasattr(other_data, col):
                col_value = getattr(other_data, col)
            else:
                col_value = other_data[col]

        except Exception as err:
            logger.debug(
                "target class: %s Other_data load col:%s err. %s",
                self._target_cls.__name__,
                col,
                err,
                exc_info=True,
            )
            logger.debug("other_data=%s", other_data)
            col_value = self._defaults_data.get(col, _NOTSET)

        return col, col_value

    def __call__(self, other_data: Any, key: str = "", **kwargs: Dict[str, Any]) -> Any:
        cols = (
            self._target_cls.__vxfields__
            if hasattr(self._target_cls, "__vxfields__")
            else self._convertors.keys()
        )
        data = dict(
            map(
                lambda col: self._convert_col(col, other_data),
                cols,
            ),
            **kwargs,
        )

        instance = self._target_cls(**data)
        return (
            (str(instance[key]), instance)
            if len(key) > 0 and key in instance.keys()
            else instance
        )
