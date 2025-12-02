from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
import uvicorn
from langchain_community.llms import Ollama
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

app = FastAPI(
    title="Customized Local LLM with Groq and Ollama",
    description="An API Server to interact with a customized local LLM using Groq and Ollama models.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled error: {exc}")
    raise HTTPException(status_code=500, detail="Internal server error")

# Check API keys on startup
@app.on_event("startup")
async def startup_event():
    if not os.getenv("GROQ_API_KEY"):
        logger.warning("GROQ_API_KEY not set. Groq routes may fail.")
    if not os.getenv("LANGCHAIN_API_KEY"):
        logger.warning("LANGCHAIN_API_KEY not set. Tracing may not work.")

try:
    add_routes(
        app,
        ChatGroq(model="llama-3.3-70b-versatile"),
        path="/chat/groq"
    )
except Exception as e:
    logger.error(f"Failed to add Groq route: {e}")

model = ChatGroq(model="llama-3.3-70b-versatile")
llm = Ollama(model="gemma3:1b")

prompt1 = ChatPromptTemplate.from_template("Write to me an essay about {topic} in less than 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write to me a poem about {topic} for a 5-year-old child with 100 words.")

try:
    add_routes(
        app,
        prompt1 | model,
        path="/essay"
    )
except Exception as e:
    logger.error(f"Failed to add essay route: {e}")

try:
    add_routes(
        app,
        prompt2 | llm,
        path="/poem"
    )
except Exception as e:
    logger.error(f"Failed to add poem route: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
