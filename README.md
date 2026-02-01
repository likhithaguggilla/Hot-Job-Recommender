## Hot Job Recommender 
An AI-powered job recommendation system that uses semantic search to match resumes with job postings. Instead of relying on simple keyword matching, this system understands the context and meaning of professional experience using Transformer-based embeddings.

## Key Features
**Semantic Matching:** Uses the all-MiniLM-L6-v2 Sentence-Transformer model to map resumes and jobs into a shared 384-dimensional vector space.

**Multi-Format Support:** Robust extraction logic for .pdf, .docx, and .txt files.

**Persistent Vector Storage:** Powered by ChromaDB for fast, high-dimensional similarity searches.

**Production-Ready Architecture:** Built with Pydantic for data validation, structured logging, and modular configuration.

## Tech Stack
Language: *Python 3.11+*

Dependency Management: *uv*

ML Frameworks: *Sentence-Transformers (PyTorch), Hugging Face*

Database: *ChromaDB (Vector Database)*

Validation: Pydantic v2

## Project Structure

hot-job-recommender/
├── data/               # Local Vector DB storage (ChromaDB)
├── src/
│   ├── engine/         # ML Logic (Embedding & Vector DB)
│   ├── scraper/        # Data ingestion pipelines
│   └── utils/          # Config, Loggers, Schemas, and Validators
├── .env                # Environment variables (API keys, paths)
├── pyproject.toml      # Project dependencies
└── main.py             # Application entry point

## Getting Started
1. Prerequisites

Ensure you have uv installed. if not, install it via:

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

2. Installation

Clone the repository and install dependencies:

git clone https://github.com/likhithaguggilla/hot-job-recommender.git

cd hot-job-recommender

uv sync

3. Environment Setup

Create a .env file in the root directory:

PROJECT_NAME="Hot Job Recommender"

CHROMA_PATH="./data/chroma_db"

ADZUNA_APP_ID="your_id"

ADZUNA_APP_KEY="your_key"

4. Running the Scraper

To populate the database with initial mock data:

uv run python -m src.scraper.main

## Roadmap & Enhancements
[ ] Integration with live Job Board APIs (Adzuna).

[ ] OCR Support for scanned/image-based resumes.

[ ] Recency-weighted ranking (prioritizing newer job postings).

[ ] Deployment of a FastAPI-based search interface.

##License
This project is licensed under the MIT License.