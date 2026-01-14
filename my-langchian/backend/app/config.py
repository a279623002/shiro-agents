import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

class Config:
    # LLM Configuration
    LLM_MODEL_ID = os.getenv("LLM_MODEL_ID", "default-model")
    LLM_API_KEY = os.getenv("LLM_API_KEY", "")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8001v1")
    
    # App Configuration
    APP_HOST = os.getenv("HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("PORT", "8000"))

# Create a config instance
config = Config()
