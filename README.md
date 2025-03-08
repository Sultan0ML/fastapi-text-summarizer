# AI Microservice (FastAPI + Streamlit)

## Overview

This repository contains a FastAPI-based AI microservice that provides text query processing and AI-powered summarization. Additionally, a Streamlit-based frontend is included to interact with the API.

## Features

- **Query Processing**: Receives and acknowledges user queries.
- **Text Summarization**: Generates AI-based summaries using a Hugging Face model.
- **Streamlit UI**: Provides an interactive interface for users to access both features.

## Tech Stack

- **FastAPI**: Backend API framework
- **Transformers (Hugging Face)**: Model for text summarization
- **Streamlit**: Frontend UI
- **Uvicorn**: ASGI server to run FastAPI
- **Requests**: Client-side interaction with the API

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Sultan0ML/fastapi-text-summarizer.git
   cd fastapi-text-summarizer
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the API Server

Start the FastAPI service using Uvicorn:

```sh
nohup uvicorn text_summarize:app --host 0.0.0.0 --port 8080 > output.log 2>&1 &
```

This command runs the server in the background, logging output to `output.log`.

## API Endpoints

### Health Check

```http
GET /
```

**Response:**

```json
{
  "message": "FastAPI AI Microservice is running."
}
```

### Query Processing

```http
POST /query
```

**Request:**

```json
{
  "query": "What is AI?"
}
```

**Response:**

```json
{
  "response": "You asked: What is AI?"
}
```

### Text Summarization

```http
POST /summarize
```

**Request:**

```json
{
  "text": "Artificial Intelligence (AI) is the simulation of human intelligence in machines."
}
```

**Response:**

```json
{
  "summary": "AI is the simulation of human intelligence in machines."
}
```

## Running the Streamlit UI

Start the Streamlit application:

```sh
streamlit run app.py
```

## File Structure

```
📂 project_root
├── text_summarize.py  # FastAPI server
├── Query_endpoint.py   # Query request script
├── summary_endpoint.py # Summarization request script
├── app.py    # Streamlit frontend
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```
## Performance & Limitations

## Performance

Inference Latency: The summarization model (sshleifer/distilbart-cnn-12-6) has an average response time of 1-2 seconds, depending on input length.

Computational Requirements: Requires a machine with at least 4GB RAM and a CPU/GPU for smooth processing.

Scalability: Can be deployed on cloud platforms like AWS/GCP using containerization.

## Limitations

High Latency for Large Inputs: Longer texts may experience increased processing time.

Limited to English Texts: The current model is trained for English text summarization only.

No Context Awareness: The summarization is extractive and does not deeply understand context beyond sentence structures.

Memory Consumption: Running multiple concurrent requests may cause increased RAM usage, especially without GPU acceleration.

## Contributing

Feel free to submit issues or pull requests to improve this project.

## License

This project is licensed under the MIT License.

