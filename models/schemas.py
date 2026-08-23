from pydantic import BaseModel
from typing import List

class Regulation(BaseModel):
    regulation_name:str
    effective_date:str
    requirements:List[str]
    affected_entities:List[str]


class RelevanceResult(BaseModel):
    relevant:bool
    reason:str
    confidence:float

class ImpactResult(BaseModel):
    impact_level:str
    affected_systems:List[str]
    affected_processes:List[str]
    required_actions:List[str]
    risk:str
    reasoning:str

