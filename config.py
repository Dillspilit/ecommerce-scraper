import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://books.toscrape.com/")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "scraped_books.xlsx")
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0")

HEADERS = {
    "User-Agent": USER_AGENT
}