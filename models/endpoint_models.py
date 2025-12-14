from pydantic import BaseModel, Field
from typing import Union

class datetime1Format(BaseModel):
	datetime1: str = Field(pattern=r"^\d+|\d{4}-0?[1-9]|1[0-2]-0?[1-9]|[1-2][0-9]|3[0-1]$")


class datetime2Format(BaseModel):
	datetime2: str = Field(pattern=r"^\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])$")


class Location(BaseModel):
	location: str = Field(pattern=r"^[a-zA-Z]+$")


class weatherReqParams(BaseModel):
	location: str = Field(pattern=r"^[a-zA-Z]+$")
	datetime1: str | None = Field(default=None, pattern=r"^(?:(\d+)|(?:\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])))$")
	datetime2: str | None = Field(default=None, pattern=r"^(?:(?:\d+)|(?:\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])))$")
	include: str | None = None


