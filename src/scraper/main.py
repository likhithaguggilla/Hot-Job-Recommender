"""
JOB SCRAPER PIPELINE
Purpose: Orchestrates the fetching, validating, and indexing of job postings.
Functionality:
    - Fetches raw job data (currently supports mock data for testing).
    - Filters data through the Pydantic validation gatekeeper.
    - Coordinates with the Embedding Engine to vectorize job descriptions.
    - Commits validated jobs and their vectors to the ChromaDB collection.
"""

from src.engine.embedder import JobEmbedder
from src.engine.vector_db import JobVectorDB
from src.utils.validators import validate_and_parse_job
from src.utils.loggers import get_logger
from datetime import datetime

logger = get_logger(__name__)

class JobScraper:
    def __init__(self):
        self.embedder = JobEmbedder()
        self.db = JobVectorDB()

    def run_mock_scrape(self):
        """
        Generates sample AI Engineer jobs to test the full system pipeline.
        """
        logger.info("Starting mock scrape for AI Engineer roles...")
        
        mock_jobs = [
            {
                "id": "mock-001",
                "title": "Junior AI Engineer",
                "company": "TechCorp Solutions",
                "description": "We are looking for a Python developer interested in LLMs and RAG systems. Experience with PyTorch is a plus.",
                "url": "https://example.com/jobs/1",
                "location": "Jersey City, NJ",
                "posted_at": datetime.now()
            },
            {
                "id": "mock-002",
                "title": "Machine Learning Intern",
                "company": "DataVision AI",
                "description": "Join our team to build computer vision models. Requires knowledge of Python, NumPy, and basic neural networks.",
                "url": "https://example.com/jobs/2",
                "location": "Remote",
                "posted_at": datetime.now()
            }
        ]

        for raw_job in mock_jobs:
            # Step 1: Validate the data
            job_model = validate_and_parse_job(raw_job)
            
            if job_model:
                # Step 2: Create Embedding
                logger.info(f"Generating embedding for: {job_model.title}")
                vector = self.embedder.get_embedding(job_model.description)
                
                # Step 3: Save to Vector DB
                self.db.upsert_job(job_model, vector)
        
        logger.info("Mock scrape and indexing complete.")

if __name__ == "__main__":
    scraper = JobScraper()
    scraper.run_mock_scrape()