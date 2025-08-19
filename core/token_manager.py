import os
from dotenv import load_dotenv

load_dotenv()

def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token not found in environment.")
    return token
