from typing import List, Any
from . import action_store as action_store
from .http_wrapper import get_wrapper
from models.node_models import JenkinsNode

@action_store.kubiya_action()
def list_jenkins_nodes(_: Any = None) -> List[JenkinsNode]:
    return get_wrapper("/computer/api/json?tree=computer[displayName,offline]")
