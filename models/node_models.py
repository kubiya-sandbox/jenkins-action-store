from pydantic import BaseModel

class JenkinsNode(BaseModel):
    displayName: str
    offline: bool
