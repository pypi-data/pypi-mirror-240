
from typing import List, Union, Any, Optional
from pydantic import BaseModel, validator
from uuid import UUID

##### 
# UI instigated events
#####
class CaseTrigger(BaseModel):
    vars: dict

class RunTrigger(BaseModel):
    run_id: UUID
    cases: List[CaseTrigger]
    
class PollResponse(BaseModel):
    registered_apps: List[UUID]
    run_trigger: Union[RunTrigger, None]
    
class AppDeletionEvent(BaseModel):
    type: str = "app_deletion"
        
#####
# UI return formats
#####   
class CaseResult(BaseModel):
    value: Any
    error: Union[str, None]
    
class RunResult(BaseModel):
    results: Optional[List[CaseResult]]
    error: Optional[Union[str, None]]
    # launched = True # between progress and error, you don't need launched
    progress: int
    
class AppRegistration(BaseModel):
    api_key: str
    parameters: List[str]
    types: List[str] # This needs to be a string because you can't send the frontend a 'type'
    demo_values: List
    descriptions: List[Union[str, None]]
    constraints: List[Union[str, None]]