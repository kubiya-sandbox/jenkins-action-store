from typing import List, Any
from . import action_store as action_store
from .http_wrapper import get_wrapper
from models.pipeline_models import JenkinsPipeline

@action_store.kubiya_action()
def list_jenkins_pipelines(_: Any = None) -> List[JenkinsPipeline]:
    return get_wrapper("/api/json?tree=jobs[name,url]")