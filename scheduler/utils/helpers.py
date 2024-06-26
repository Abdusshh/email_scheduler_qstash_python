# utils/helpers.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/.env'))
load_dotenv(dotenv_path=env_path)

def get_env_variable(var_name):
    try:
        return os.getenv(var_name)
    except KeyError:
        message = f"Expected environment variable '{var_name}' not set."
        raise Exception(message)