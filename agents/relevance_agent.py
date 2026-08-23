from ollama import chat
from models.schemas import Regulation,RelevanceResult

def relevance_agent(regulation:Regulation):

    prompt= f""" You are a Regulatory Relevance Agent.
    
    Your job is to determine where the regulation is relevant to our company.
    
    company profile:
    
    Industry:
    Software / Technology
    
    The Company:
    - Develops software applications
    - Processes customer data
    - Uses AWS
    - Uses databases
    - Uses data pipelines
    - Uses cloud storage
    
    Regulation information:
    
    Regulation Name:
    {regulation.regulation_name}
    
    Effective Date:
    {regulation.effective_date}

    Requirements:
    {regulation.requirements}
    
    Affected Entities:
    {regulation.affected_entities}
    
    Determine:
    1. Is this regulation relevant to our company?
    2. Explain why.
    3. Give a confidence score between 0 and 1.
    
    Return ONLY valid JSON with:

    relevant
    reason
    confidence
    """

    response = chat(model = "qwen3:8b",messages = [{
        "role":"user",
        "content":prompt
    }],
       format=RelevanceResult.model_json_schema()
                    )

    return RelevanceResult.model_validate_json(response.message.content)