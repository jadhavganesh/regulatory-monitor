from ollama import chat
from models.schemas import Regulation


def extraction_agent(text:str):

    prompt=f"""
    
    You are a regulatory document extraction agent.

Extract the following information from the regulation.

Return ONLY JSON with exactly these fields:

- regulation_name
- effective_date
- requirements
- affected_entities

Regulation document: {text}

"""

    response = chat(model="qwen3:8b",
                    messages=[
                        {"role":"user",
                         "content":prompt}

                    ],
                    format = Regulation.model_json_schema()
                    )

    return Regulation.model_validate_json(response.message.content)