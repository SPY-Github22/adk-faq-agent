from google.adk.agents import Agent

KNOWLEDGE_BASE = """
ADK (Agent Development Kit) is a framework by Google for building AI agents using Gemini models.
Gemini is Google's most capable AI model, used for text, code, and reasoning tasks.
Cloud Run is a serverless platform on Google Cloud for deploying containerized applications.
This agent was built for the Hack2Skill Gen AI APAC Hackathon Track 1.
The hackathon focuses on building and deploying production-ready AI agents using Gemini and ADK.
Google Cloud Skills Boost is a learning platform for Google Cloud certifications and labs.
A2A (Agent-to-Agent) SDK allows multiple ADK agents to communicate with each other.
Vertex AI is Google Cloud's machine learning platform for training and deploying AI models.
FastAPI is a modern Python web framework used to expose agents as HTTP endpoints.
Docker is used to containerize applications for deployment on Cloud Run.
"""

root_agent = Agent(
    name="faq_agent",
    model="gemini-2.0-flash",
    description="Answers questions about Google ADK, Gemini, Cloud Run, and the Hack2Skill hackathon.",
    instruction=f"""You are a helpful FAQ assistant. Answer questions clearly and concisely 
using the knowledge base below. If the question is not covered, answer from your general knowledge.
Keep answers under 3 sentences.

Knowledge Base:
{KNOWLEDGE_BASE}
""",
)