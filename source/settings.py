import os

from dotenv import load_dotenv

load_dotenv(".env.development")

TOKEN_BOT = os.getenv("TOKEN_BOT")
