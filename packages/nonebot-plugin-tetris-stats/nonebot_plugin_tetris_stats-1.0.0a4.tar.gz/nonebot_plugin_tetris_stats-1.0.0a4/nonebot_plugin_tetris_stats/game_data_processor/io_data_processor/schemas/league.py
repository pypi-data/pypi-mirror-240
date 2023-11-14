from pydantic import BaseModel, Field

from .base import Cache


class User(BaseModel):
    _id: str
    username: str


class Handling(BaseModel):
    arr: float
    das: float
    dcd: float
    sdf: int
    safelock: bool
    cancel: bool


class Extra(BaseModel):
    vs: float


class ExtraAvgTracking(BaseModel):
    aggregatestats___vsscore: list[float]


class Points(BaseModel):
    primary: int
    secondary: float
    tertiary: float
    extra: Extra
    secondary_avg_tracking: list[float] = Field(..., alias='secondaryAvgTracking')
    tertiary_avg_tracking: list[float] = Field(..., alias='tertiaryAvgTracking')
    extra_avg_tracking: ExtraAvgTracking = Field(..., alias='extraAvgTracking')


class EndcontextItem(BaseModel):
    user: User
    handling: Handling
    active: bool
    success: bool
    inputs: int
    piecesplaced: int
    naturalorder: int
    score: int
    wins: int
    points: Points


class User1(BaseModel):
    _id: str
    username: str


class Record(BaseModel):
    _id: str
    endcontext: list[EndcontextItem]
    ismulti: bool
    replayid: str
    stream: str
    ts: str
    user: User1


class Data(BaseModel):
    records: list[Record]


class Model(BaseModel):
    success: bool
    data: Data
    cache: Cache
