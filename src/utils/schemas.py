"""
DATA SCHEMAS (Pydantic Models)
Purpose: Defines the 'Source of Truth' for all data structures in the application.
Functionality:
    - Enforces strict type-checking and data validation for Jobs and Resumes.
    - Automates the conversion of complex types (like datetime) to JSON-safe strings.
    - Provides a blueprint for the data stored in the Vector Database (ChromaDB).
"""

from pydantic import BaseModel, Field, HttpUrl, field_serializer
from typing import List, Optional
from datetime import datetime

class JobModel(BaseModel):
    """
    Represents a single job posting within the system.
    This schema ensures that every job has the necessary metadata for 
    accurate semantic search and filtering.
    """
    # Essential Identification
    id: str = Field(..., description="Unique ID from the job board (e.g., Adzuna ID)")
    
    # Content Fields
    title: str = Field(..., min_length=2, description="Job title, e.g., 'AI Engineer'")
    company: str = Field(..., description="Name of the hiring organization")
    description: str = Field(..., min_length=20, description="The full text of the job posting")
    
    # Metadata & Links
    url: Optional[HttpUrl] = None
    location: str = "Remote"
    
    # Timestamps for Recency Management
    # posted_at: When the employer published the job.
    # updated_at: When our system last refreshed or processed this specific vector.
    posted_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Search Tags (e.g., ['Python', 'PyTorch', 'NLP'])
    tags: List[str] = []

    @field_serializer('posted_at', 'updated_at')
    def serialize_dt(self, dt: datetime, _info):
        """
        Converts datetime objects to ISO-formatted strings.
        This is required because ChromaDB metadata only accepts basic 
        types like strings, integers, or floats.
        """
        return dt.isoformat()


class ResumeModel(BaseModel):
    """
    Represents the output of the Resume Parsing process.
    This acts as the bridge between raw document files (.pdf, .docx) 
    and the embedding engine.
    """
    filename: str = Field(..., description="The name of the uploaded file")
    raw_text: str = Field(..., description="The full extracted text content of the resume")
    
    # Note: As the project grows, fields like 'email', 'skills', and 'name'
    # can be added here for more advanced filtering.