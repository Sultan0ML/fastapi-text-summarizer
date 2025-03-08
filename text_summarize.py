from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import logging
import re

# Initialize FastAPI app
app = FastAPI(
    title="AI Microservice",
    description="Provides query responses and AI-based summarization.",
    version="1.0"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the Hugging Face summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Request Models
class QueryRequest(BaseModel):
    query: str

class SummarizationRequest(BaseModel):
    text: str

@app.get("/", summary="Health Check", response_model=dict)
async def root():
    """Check if the API is running."""
    return {"message": "FastAPI AI Microservice is running."}

@app.post("/query", summary="Process User Query", response_model=dict)
async def process_query(request: QueryRequest):
    """Receives user query and responds with an acknowledgment."""
    logger.info(f"Received raw request: {request.dict()}")  # Convert request model to dict
    return {"response": f"You asked: {request.query}"}


from fastapi.responses import JSONResponse

@app.post("/summarize", summary="Summarize Text", response_model=dict)
async def summarize_text(request: SummarizationRequest):
    """Summarizes the given text using an AI model."""
    try:
        # Process and clean input text
        raw_text = request.text.strip()
        formatted_text = raw_text.encode("utf-8", "ignore").decode("utf-8")
        formatted_text = formatted_text.replace("\n", " ").replace("\t", " ")
        formatted_text = formatted_text.replace("’", "'").replace("“", '"').replace("”", '"')
        formatted_text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"]', '', formatted_text)

        if not formatted_text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")
        if len(formatted_text.split()) < 10:
            raise HTTPException(status_code=400, detail="Text is too short to summarize.")

        # Generate Summary
        summary = summarizer(formatted_text, max_length=250, min_length=50, do_sample=False)
        summary_text = summary[0]["summary_text"]

        # ✅ Convert response to JSON format
        return JSONResponse(content={"summary": summary_text}, media_type="application/json")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
