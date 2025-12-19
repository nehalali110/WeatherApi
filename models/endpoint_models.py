from pydantic import BaseModel, Field
from typing import Union


month = r"(?:0?[1-9]|1[0-2])"
day = r"(?:0?[1-9]|[1-2][0-9]|3[0-1])"
year=r"\d{4}"
hour= r"[0-1][0-9]|2[0-3]"
min_sec = r"[0-5][0-9]"
time=rf"T(?:{hour}):(?:{min_sec}):(?:{min_sec})"


class Location(BaseModel):
	location: str = Field(pattern=r"^[a-zA-Z]+$")


class weatherReqParams(BaseModel):
	location: str = Field(pattern=r"^[a-zA-Z]+$")
	datetime1: str | None = Field(default=None, pattern=rf"^{year}-{month}-{day}(?:{time})?$")
	datetime2: str | None = Field(default=None, pattern=rf"^{year}-{month}-{day}(?:{time})?$")



