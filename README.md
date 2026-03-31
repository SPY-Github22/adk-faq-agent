# ADK FAQ Agent — Hack2Skill Gen AI APAC Hackathon (Track 1)

A production-ready AI agent built with **Google ADK** and **Gemini 2.0 Flash**, deployed on **Google Cloud Run**.

## What It Does
This agent answers FAQ-style questions about Google ADK, Gemini, Cloud Run, and the Hack2Skill hackathon. It uses a Gemini model for inference and is accessible via a simple HTTP endpoint.

## Tech Stack
- **Google ADK** — Agent Development Kit
- **Gemini 2.0 Flash** — LLM for inference
- **FastAPI** — HTTP server
- **Docker** — Containerization
- **Google Cloud Run** — Serverless deployment

## API Usage

### Health Check
```
GET /
```
Response:
```json
{"status": "ok", "agent": "faq_agent", "model": "gemini-2.0-flash"}
```

### Ask the Agent
```
POST /run
Content-Type: application/json

{"input": "What is ADK?"}
```
Response:
```json
{
  "response": "ADK (Agent Development Kit) is a framework by Google for building AI agents using Gemini models.",
  "agent": "faq_agent"
}
```

## Sample Questions to Try
- `"What is ADK?"`
- `"What is Cloud Run?"`
- `"What is Gemini?"`
- `"What is this hackathon about?"`

## Local Setup
```bash
pip install -r requirements.txt
set GOOGLE_API_KEY=your_key_here   # Windows
python main.py
```

## Deployment
```bash
gcloud run deploy faq-agent --source . --region us-central1 --allow-unauthenticated --set-env-vars GOOGLE_API_KEY=your_key_here
```
