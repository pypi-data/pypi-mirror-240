"""量化交易时间计时器"""

import time
import datetime

import contextlib
from typing import Callable, List, Union, Set
from vxutils import logger, convertors

__all__ = ["vxtime"]

DatetimeType = Union[datetime.datetime, datetime.date, str, float, int]


class vxtime:
    """量化交易时间机器"""

    _timefunc: Callable[[], float] = time.time
    _delayfunc: Callable[[float], None] = time.sleep
    __holidays__: Set[datetime.date] = set()

    @classmethod
    def now(cls, fmt: str = "") -> DatetimeType:
        """当前时间

        Keyword Arguments:
            fmt {str} -- 时间格式 (default: {''}, 返回时间戳)

        Returns:
            _type_ -- _description_

        """

        now_timestamp: float = cls._timefunc()

        if fmt and fmt.lower() in {"datetime", "dt"}:
            return convertors.to_datetime(now_timestamp)
        elif fmt:
            return time.strftime(fmt, time.localtime(now_timestamp))
        else:
            return now_timestamp

    @classmethod
    def sleep(
        cls,
        seconds: float = 0,
        minutes: float = 0,
        hours: float = 0,
        weeks: float = 0,
        days: float = 0,
    ) -> None:
        """延时等待函数"""
        sleep_time: float = datetime.timedelta(
            seconds=seconds, minutes=minutes, hours=hours, weeks=weeks, days=days
        ).total_seconds()
        cls._delayfunc(sleep_time)

    @classmethod
    @contextlib.contextmanager
    def timeit(cls, prefix: str = "") -> None:
        """计时器"""

        if prefix == "":
            prefix = "default timer"
        try:
            start = time.perf_counter()
            yield
        finally:
            cost_str = f"{prefix} use time: {(time.perf_counter() - start)*1000:,.2f}"
            logger.warning(cost_str)

    @classmethod
    def is_holiday(cls, date_: DatetimeType = "") -> bool:
        """是否假日"""
        check_date: datetime.date = convertors.to_datetime(date_ or cls.now()).date()
        return (
            True if check_date.weekday() in [5, 6] else check_date in cls.__holidays__
        )

    @classmethod
    def set_timefunc(cls, timefunc: Callable[[], float]) -> None:
        """设置timefunc函数"""
        if not callable(timefunc):
            raise ValueError(f"{timefunc} is not callable.")
        cls._timefunc = timefunc

    @classmethod
    def set_delayfunc(cls, delayfunc: Callable[[float], None]) -> None:
        """设置delayfunc函数"""
        if not callable(delayfunc):
            raise ValueError(f"{delayfunc} is not callable.")
        cls._delayfunc = delayfunc

    @classmethod
    def today(cls, time_str: str = "00:00:00") -> float:
        """今天 hh:mm:ss 对应的时间"""
        date_str = cls.now("%Y-%m-%d")
        return convertors.combine_datetime(date_str, time_str)

    @classmethod
    def date_range(
        cls,
        start_date: DatetimeType = "",
        end_date: DatetimeType = "",
        interval: int = 1,
        skip_holidays: bool = False,
    ) -> List[datetime.date]:
        """生成时间序列

        Arguments:
            start_date {str} -- 起始日期,默认值: None,即:2005-01-01
            end_date {str} -- 终止日期,默认值: None, 即: 当天
            interval {int} -- 间隔时间 默认值: 1天
            skip_holidays (bool) -- 是否跳过假期

        Returns:
            List -- 时间序列
        """
        _start_date: datetime.date = convertors.to_datetime(
            start_date or "2005-01-01"
        ).date()

        _end_date: datetime.date = convertors.to_datetime(
            end_date or cls.today()
        ).date()

        if _start_date > _end_date:
            raise ValueError(
                f"start_date({_start_date}) must larger then end_date({_end_date})."
            )

        delta = datetime.timedelta(days=1)
        result: List[datetime.date] = []
        date = _start_date
        while date <= _end_date:
            if skip_holidays is False or date in cls.__holidays__:
                result.append(date)
            date += delta

        return result[::interval]

    @classmethod
    def add_holidays(cls, *holidays: List[DatetimeType]) -> None:
        """增加假期时间"""
        if len(holidays) == 1 and isinstance(holidays[0], list):
            holidays = holidays[0]

        cls.__holidays__.update(
            map(lambda d: convertors.to_datetime(d).date(), holidays)
        )

    @classmethod
    def add_businessdays(cls, *businessdays: List[DatetimeType]) -> None:
        """添加工作日"""
        if not businessdays:
            return

        if len(businessdays) == 1 and isinstance(businessdays[0], (list, tuple)):
            businessdays = businessdays[0]

        businessdays: List[datetime.date] = sorted(
            map(lambda x: convertors.to_datetime(x).date(), businessdays)
        )
        start_date: datetime.date = businessdays[0]
        end_date: datetime.date = businessdays[-1]
        business_dates: List[datetime.date] = cls.date_range(
            start_date, end_date, skip_holidays=False
        )
        holidays = set(business_dates) - set(businessdays)
        cls.__holidays__ = cls.__holidays__ - set(businessdays)
        cls.__holidays__.update(holidays)


if __name__ == "__main__":
    print(vxtime.now("%Y-%m-%d %H:%M:%S"))
