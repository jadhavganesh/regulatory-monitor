from ollama import chat
from models.schemas import Regulation,RelevanceResult,ImpactResult


def impact_agent(
regulation:Regulation,relevanceResult:RelevanceResult):

    prompt=f"""
    
    You are a Regulatory Impact Analysis Agent.
    
    Your job is to determine how a relevant regulation
could impact our company.

Company profile:

Industry:
Software / Technology

Systems:
- AWS S3
- Amazon Redshift
- MySQL
- Python data pipelines
- APIs
- Kubernetes / EKS

Processes:
- Customer data processing
- Data storage
- Data pipelines
- Billing systems
- Data retention
- Monitoring and reporting

Regulation:

Name:
{regulation.regulation_name}

Effective Date:
{regulation.effective_date}

Requirements:
{regulation.requirements}

Affected Entities:
{regulation.affected_entities}


Affected Entities:
{regulation.affected_entities}

Analyze the potential impact.

Determine:

1. Impact level: LOW, MEDIUM, or HIGH
2. Which company systems could be affected
3. Which business/technical processes could be affected
4. What actions the company may need to take
5. What is the compliance risk
6. Explain your reasoning


Important:
Do not invent specific legal requirements that are not
present in the regulation.

Return ONLY valid JSON with these fields:

impact_level
affected_systems
affected_processes
required_actions
risk
reasoning

"""

    response = chat(model="qwen3:8b",
                    messages=[{

                        "role":"user",
                        "content": prompt
                    }],
                    format=ImpactResult.model_json_schema()
                    )

    return ImpactResult.model_validate_json(response.message.content)
