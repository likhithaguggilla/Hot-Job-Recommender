"""
JOB EMBEDDING ENGINE
Purpose: Translates raw resume and job documents into high-dimensional vectors.
Functionality:
    - Multi-format text extraction (PDF, DOCX, TXT).
    - Text cleaning and normalization for better ML performance.
    - Semantic encoding using Sentence-Transformers (BERT-based).
    - Bridges the gap between unstructured human language and searchable math.
"""

import PyPDF2
from docx import Document
from sentence_transformers import SentenceTransformer
from src.utils.logger import get_logger
from src.utils.config import settings

# Initialize module-level logger
logger = get_logger(__name__)

class JobEmbedder:
    """
    The 'Brain' of the system. This class manages the lifecycle of the 
    Machine Learning model and the extraction pipeline.
    """
    
    def __init__(self):
        """
        Initializes the JobEmbedder by loading the ML model weights.
        The model is loaded from the path/name specified in global settings.
        """
        # Load the SentenceTransformer model into memory.
        # Note: This may take a few seconds on the first run as weights are downloaded.
        self.model = SentenceTransformer(settings.MODEL_NAME)
        logger.info(f"Loaded embedding model: {settings.MODEL_NAME}")

    def extract_text(self, file_path: str) -> str:
        """
        Strategy Dispatcher: Identifies file type and routes it to the correct parser.
        
        Args:
            file_path (str): Path to the resume or job document.
            
        Returns:
            str: The extracted plain text content.
        """
        # Extract extension safely from the file path
        ext = file_path.lower().rsplit('.', 1)[-1]
        
        if ext == 'pdf':
            return self._extract_from_pdf(file_path)
        elif ext == 'docx':
            return self._extract_from_docx(file_path)
        elif ext == 'txt':
            return self._extract_from_txt(file_path)
        else:
            logger.error(f"No extractor for extension: {ext}")
            return ""

    def _extract_from_pdf(self, path: str) -> str:
        """Internal helper to extract text from PDF layers."""
        text = ""
        try:
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                # Join text from all pages with spaces to avoid merging words at page breaks
                text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        except Exception as e:
            logger.error(f"PDF extraction failed for {path}: {e}")
        return text

    def _extract_from_docx(self, path: str) -> str:
        """Internal helper to extract text from Microsoft Word paragraphs."""
        try:
            doc = Document(path)
            # Iterates through paragraphs to reconstruct the document structure
            return " ".join([para.text for para in doc.paragraphs])
        except Exception as e:
            logger.error(f"DOCX extraction failed for {path}: {e}")
            return ""

    def _extract_from_txt(self, path: str) -> str:
        """Internal helper to read plain text files with UTF-8 safety."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            logger.error(f"TXT extraction failed for {path}: {e}")
            return ""

    def get_embedding(self, text: str):
        """
        Converts extracted text into a numerical vector (embedding).
        
        Args:
            text (str): The cleaned text to be vectorized.
            
        Returns:
            list: A list of floats representing the semantic meaning of the text.
        """
        # Guard against empty input which can cause model errors or noisy vectors
        if not text.strip():
            logger.warning("Attempted to embed empty or whitespace-only text.")
            return []
            
        # .encode() generates the vector; .tolist() ensures compatibility with ChromaDB
        return self.model.encode(text).tolist()