# Hot Job Recommender 🚀

An AI-powered job recommendation system that uses semantic search to match resumes with job postings. Instead of relying on simple keyword matching, this system understands the context and meaning of professional experience using Transformer-based embeddings.

## 🌟 Key Features
* **Semantic Matching**: Uses the `all-MiniLM-L6-v2` Sentence-Transformer model to map resumes and jobs into a shared 384-dimensional vector space.
* **Multi-Format Support**: Robust extraction logic for `.pdf`, `.docx`, and `.txt` files.
* **Persistent Vector Storage**: Powered by **ChromaDB** for fast, high-dimensional similarity searches.
* **Production-Ready Architecture**: Built with **Pydantic v2** for data validation, structured logging, and modular configuration.

## 🛠️ Tech Stack
* **Language**: Python 3.11+
* **Dependency Management**: [uv](https://github.com/astral-sh/uv)
* **ML Frameworks**: Sentence-Transformers (PyTorch), Hugging Face
* **Database**: ChromaDB (Vector Database)
* **Validation**: Pydantic v2

## 📂 Project Structure
```text
hot-job-recommender/
├── data/               # Local Vector DB storage (ChromaDB)
├── src/
│   ├── engine/         # ML Logic (Embedding & Vector DB)
│   ├── scraper/        # Data ingestion pipelines
│   └── utils/          # Config, Loggers, Schemas, and Validators
├── .env                # Environment variables (API keys, paths)
├── pyproject.toml      # Project dependencies
└── main.py             # Application entry point
```

## 🚀 Getting Started
1. Prerequisites
Ensure you have uv installed. If not, install it via:
```text
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```
2. Installation
Clone the repository and install dependencies:
```text
git clone [https://github.com/likhithaguggilla/hot-job-recommender.git](https://github.com/likhithaguggilla/hot-job-recommender.git)
cd hot-job-recommender
uv sync
```
4. Environment Setup
Create a .env file in the root directory and add your credentials:
```text
PROJECT_NAME="Hot Job Recommender"
CHROMA_PATH="./data/chroma_db"
ADZUNA_APP_ID="your_adzuna_id"
ADZUNA_APP_KEY="your_adzuna_key"
```
4. Running the Scraper
To populate the database with initial mock data and verify the pipeline:
```text
uv run python -m src.scraper.main
```
🗺️ Roadmap & Enhancements
* Live API Integration: Transition from mock data to real-time Adzuna API fetches.

* OCR Support: Implement Tesseract or LayoutLM for scanned/image-based resumes.

* Recency Ranking: Implement time-decay scoring to prioritize newer job postings.

* Web Interface: Deployment of a FastAPI-based search and upload interface.

📄 License

This project is licensed under the MIT License.
