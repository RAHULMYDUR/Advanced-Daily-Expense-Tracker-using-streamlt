import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration variables
EXPENSE_FILE = "daily_expenses.csv"
LLM_API_KEY = os.getenv("LLM_API_KEY")
