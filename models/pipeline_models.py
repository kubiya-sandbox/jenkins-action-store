from pydantic import BaseModel

class JenkinsPipeline(BaseModel):
    name: str
    url: str