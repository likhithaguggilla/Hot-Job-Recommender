"""
CONFIGURATION UTILITY
Purpose: Centralizes application settings and environment variables.
Functionality:
    - Uses Pydantic Settings for type-safe configuration management.
    - Automatically parses the root '.env' file for sensitive keys.
    - Provides a single 'settings' object used across the entire system.
    - Defines default values for project structure and ML model parameters.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    # --- Project Metadata ---
    PROJECT_NAME: str = "Hot Job Recommender"
    
    # --- Machine Learning Config ---
    # The 'all-MiniLM-L6-v2' is a fast, lightweight Sentence-Transformer 
    # model that converts text into 384-dimension vectors.
    MODEL_NAME: str = "all-MiniLM-L6-v2"
    
    # --- Path Management ---
    # BASE_DIR calculates the root of the project relative to this file.
    # CHROMA_PATH defines where the local vector database files are stored.
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    CHROMA_PATH: str = str(BASE_DIR / "data" / "chroma_db")
    
    # --- External API Keys ---
    # Marked as Optional (str | None) to prevent the app from crashing 
    # if the keys aren't present during local development or testing.
    ADZUNA_APP_ID: str | None = None
    ADZUNA_APP_KEY: str | None = None

    # --- Pydantic Settings Configuration ---
    # Tells Pydantic to look for a .env file and how to handle extra data.
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"  # Keeps the app stable even if the .env has extra keys
    )

# Create a singleton instance of Settings to be imported by other modules.
# This ensures we aren't reloading the .env file multiple times.
settings = Settings()


# ------ Usage Example ------
# 
# from src.utils.config import settings
#
# def connect_db():
#     print(f"Initializing {settings.PROJECT_NAME}...")
#     print(f"Connecting to database at: {settings.CHROMA_PATH}")