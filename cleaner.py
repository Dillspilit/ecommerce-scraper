import re

# Mapping for string ratings to integer values
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def clean_price(price_raw: str) -> float:
    """Extracts a numeric float value from a price string (e.g., '£51.77' -> 51.77)."""
    if not price_raw:
        return 0.0
    match = re.search(r"[\d.]+", price_raw)
    if match:
        try:
            return float(match.group())
        except ValueError:
            return 0.0
    return 0.0


def clean_rating(rating_raw: str) -> int:
    """Converts a string rating ('Three') to an integer from 1 to 5."""
    return RATING_MAP.get(rating_raw, 0)


def clean_availability(availability_raw: str) -> bool:
    """Determines stock status as a boolean (True/False)."""
    if not availability_raw:
        return False
    return "in stock" in availability_raw.lower()


def process_book_data(raw_books: list[dict]) -> list[dict]:
    """Processes raw scraped dictionaries into cleaned, typed structures."""
    cleaned_books = []
    
    for book in raw_books:
        cleaned_item = {
            "title": book.get("title", "").strip(),
            "price_gbp": clean_price(book.get("price_raw", "")),
            "rating": clean_rating(book.get("rating_raw", "")),
            "in_stock": clean_availability(book.get("availability_raw", ""))
        }
        cleaned_books.append(cleaned_item)
        
    return cleaned_books