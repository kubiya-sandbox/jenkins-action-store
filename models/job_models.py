from pydantic import BaseModel
from typing import List, Optional


class JenkinsJob(BaseModel):
    name: str
    url: str

class JenkinsBuild(BaseModel):
    id: str
    url: str
    timestamp: int
    result: str
    duration: int

class JenkinsBuildLog(BaseModel):
    log: str

class JobParams(BaseModel):
    job_name: str

class BuildParams(BaseModel):
    job_name: str
    build_number: str

class TextSearchParams(BaseModel):
    job_name: str
    build_number: str
    text: str

class NewJobConfig(BaseModel):
    job_name: str
    config_xml: str

class JenkinsJob(BaseModel):
    name: str
    url: str

class JobDeleteParams(BaseModel):
    job_name: str

class JobParamsRequest(BaseModel):
    job_name: str


class JobParameter(BaseModel):
    name: str
    type: str
    choices: List[str]


class JobParamsResponse(BaseModel):
    parameters: List[JobParameter]

class BuildConsoleLogsRequest(BaseModel):
    job_name: str
    build_number: int


class BuildConsoleLogsResponse(BaseModel):
    console_logs: str

class TriggerJobRequest(BaseModel):
    job_name: str
    parameters: Optional[dict] = None

class TriggerJobResponse(BaseModel):
    success: bool
    message: str
    build_number: Optional[str] = None

class CancelJobRequest(BaseModel):
    job_name: str

class CancelJobResponse(BaseModel):
    success: bool
    message: str

class JobStatusRequest(BaseModel):
    job_name: str
    build_number: Optional[str] = None

class JobStatusResponse(BaseModel):
    status: str
    message: str
    build_logs: Optional[str] = None