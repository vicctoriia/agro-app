from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env variables
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


