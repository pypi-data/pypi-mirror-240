"""基础模型"""
import datetime
from vxutils import vxtime, to_datetime
from typing import Any, Dict, Union
from pydantic import BaseModel, Field

DatetimeType = datetime.datetime


class vxDataModel(BaseModel):
    updated_dt: DatetimeType = Field(default_factory=vxtime.now, validate_default=True)
    created_dt: DatetimeType = Field(default_factory=vxtime.now, validate_default=True)

    def __init__(self, **data: Dict[str, Any]) -> None:
        created_dt: datetime.datetime = data.setdefault(
            "created_dt", datetime.datetime.now()
        )
        updated_dt: datetime.datetime = data.setdefault("updated_dt", created_dt)

        super().__init__(**data)
        self.created_dt = created_dt
        self.updated_dt = updated_dt

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in ["updated_dt", "created_dt"]:
            self.updated_dt = vxtime.now("%Y-%m-%d %H:%M:%S")
        return super().__setattr__(name, value)

    def __str__(self) -> str:
        return self.model_dump_json(indent=4)

    def __repr__(self) -> str:
        return self.model_dump_json(indent=4)


if __name__ == "__main__":

    class vxTick(vxDataModel):
        symbol: str

    tick = vxTick(symbol="123")
    print(tick)
