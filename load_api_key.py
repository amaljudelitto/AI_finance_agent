from dotenv import load_dotenv
import os

load_dotenv("secret.env")
api_key = os.getenv("OPENAI_API_KEY")
