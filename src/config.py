from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    MODEL_NAME = os.getenv("MODEL_NAME")
    CHUNK_SIZE = os.getenv("CHUNK_SIZE")
    CHUNK_OVERLAP = os.getenv("CHUNK_OVERLAP")