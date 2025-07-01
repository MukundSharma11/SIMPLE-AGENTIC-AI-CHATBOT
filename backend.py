from pydantic import BaseModel
from typing import List
from agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODEL_NAME = ['qwen-qwq-32b', 'gemma2-9b-it']

from fastapi import FastAPI

app = FastAPI(title = "Chatbot")

@app.post("/chat")

def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAME:
        return {'Error': "Invalid Model"}
    
    llm_name = request.model_name
    allow_search = request.allow_search
    prompt = request.prompt
    query = request.messages[-1]

    response = get_response_from_ai_agent(llm_name, allow_search, prompt, query)
    
    return response

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=9999)


    
