import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from google.genai import types
from agent import KNOWLEDGE_BASE

app = FastAPI(title="ADK FAQ Agent - Hack2Skill Track 1")

class QueryRequest(BaseModel):
    input: str

class QueryResponse(BaseModel):
    response: str
    agent: str

SYSTEM_INSTRUCTION = f"""You are a helpful FAQ assistant. Answer questions clearly and concisely 
using the knowledge base below. If the question is not covered, answer from your general knowledge.
Keep answers under 3 sentences.

Knowledge Base:
{KNOWLEDGE_BASE}
"""

@app.get("/")
def health_check():
    return {"status": "ok", "agent": "faq_agent", "model": "gemini-2.0-flash"}

@app.post("/run", response_model=QueryResponse)
async def run_agent(req: QueryRequest):
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=req.input,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=300,
        )
    )

    return QueryResponse(
        response=response.text,
        agent="faq_agent"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)