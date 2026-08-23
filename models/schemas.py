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

class JudgeResult(BaseModel):
    approved:bool
    confidence:float
    issues:List[str]
    evidence_supported:bool
    confirmed_requirements: List[str]
    inferred_impacts: List[str]
    unsupported_claims: List[str]
    recommendation:str