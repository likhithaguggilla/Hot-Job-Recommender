"""
DATA VALIDATORS
Purpose: Acts as the system's 'Gatekeeper' to ensure data integrity.
Functionality:
    - Verifies physical file existence and format compliance for resumes.
    - Safely transforms raw, unstructured scraper data into validated Pydantic objects.
    - Prevents application crashes by catching and logging data-level errors.
"""

import os
from typing import Optional, Set
from pydantic import ValidationError
from .schemas import JobModel
from .loggers import get_logger

# Initialize logger for this specific module to track validation success/failure
logger = get_logger(__name__)

# Define allowed extensions at the top level. 
# In a production environment, this makes it easy to add new formats (like .md)
# without touching the core logic.
ALLOWED_RESUME_EXTENSIONS: Set[str] = {'.pdf', '.docx', '.txt', '.rtf'}

def is_valid_resume(file_path: str) -> bool:
    """
    Performs integrity checks on a resume file before processing.
    
    Args:
        file_path (str): The local system path to the resume file.
        
    Returns:
        bool: True if the file exists and is an allowed format, False otherwise.
    """
    # Check 1: Physical existence on the server/machine
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return False
    
    # Check 2: Extension validation
    # os.path.splitext handles complex paths and extracts the extension safely.
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in ALLOWED_RESUME_EXTENSIONS:
        logger.warning(f"Unsupported file format '{ext}': {file_path}")
        return False
        
    return True

def validate_and_parse_job(raw_data: dict) -> Optional[JobModel]:
    """
    Converts a raw dictionary (likely from a web scraper) into a JobModel.
    This is the 'Gatekeeper' that ensures our Vector DB only stores clean data.
    
    Args:
        raw_data (dict): The unstructured dictionary containing job details.
        
    Returns:
        Optional[JobModel]: A validated JobModel object if successful, else None.
    """
    try:
        # Pydantic validates types, lengths, and required fields automatically.
        job = JobModel(**raw_data)
        logger.info(f"Successfully validated job: {job.title} at {job.company}")
        return job
    except ValidationError as e:
        # We log the specific validation error (e.g., 'missing title' or 'description too short')
        # returning None allows the scraper loop to skip one bad job and continue with others.
        logger.error(f"Validation failed for a job entry. Errors: {e.errors()}")
        return None