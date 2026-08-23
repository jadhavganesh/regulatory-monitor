from ollama import chat
from models.schemas import (
    Regulation,
    RelevanceResult,
    ImpactResult,
    JudgeResult
)

def judge_agent(regulation:Regulation,relevance:RelevanceResult,impactResult:ImpactResult):


    prompt=f"""
        
        You are a Regulatory compliance judge agent.
        
        your job is to validate the analysis produced by other AI agents.
        
        you must Not blindly trust their conclusions.
        
        REGULATION
        -----------
        
        Name: {regulation.regulation_name}
        Effective Date:{regulation.effective_date}
        Requirements:{regulation.requirements}
        Affected Entities: {regulation.affected_entities}
        
        
        RELEVANCE ANALYSIS
        ------------------
        Relevant:{relevance.relevant}
        Reason:{relevance.reason}
        confidence:{relevance.confidence}
        
        IMPACT ANALYSIS
        ---------------
        Impact Level:{impactResult.impact_level}
        Affected Systems:{impactResult.affected_systems}
        Affected Processes:{impactResult.affected_processes}
        Required Actions:{impactResult.required_actions}
        Risk:{impactResult.risk}
        Reasoning:{impactResult.reasoning}
    
        Your Task
        ---------------
        Validate the analysis.
        Check:
        1. Is the relevance decision reasonable?
        2. Is the impact analysis supported by the
   regulation?
        
        3. Are the affected systems reasonable?
        
        4. Are the required actions reasonable?
        
        5. Did the previous agents invent information
           that is not supported by the regulation?
        
        6. Is there enough evidence to approve the result?
        
        If the analysis contains unsupported claims,
list them in "issues".

Set:

approved = true

ONLY if the analysis is sufficiently supported.

Set:

approved = false

if important claims are unsupported or unreliable.

Confidence must be between 0 and 1.

Return ONLY valid JSON with:

approved
confidence
issues
evidence_supported
recommendation

"""

    response = chat(model="qwen3:8b",
                    messages = [{"role":"user","content":prompt}],format=JudgeResult.model_json_schema()
)
    return JudgeResult.model_validate_json(response.message.content)