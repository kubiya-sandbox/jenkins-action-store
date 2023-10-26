from pydantic import BaseModel


class Plugin(BaseModel):
    shortName: str
    longName: str