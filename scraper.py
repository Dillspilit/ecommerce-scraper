import urllib.parse
import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS


def fetch_html(url: str) -> str | None:
    """Executes an HTTP GET request and returns the page HTML content."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def parse_books_from_page(html: str) -> list[dict]:
    """Extracts raw book data from a single HTML page."""
    soup = BeautifulSoup(html, "html.parser")
    books_data = []

    # Find all product cards on the page
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        # Book title
        title_tag = article.h3.find("a")
        title = title_tag["title"] if title_tag and "title" in title_tag.attrs else title_tag.text

        # Raw price string (e.g., "£51.77")
        price_tag = article.find("p", class_="price_color")
        price_raw = price_tag.text if price_tag else ""

        # Raw stock availability string
        availability_tag = article.find("p", class_="instock availability")
        availability_raw = availability_tag.text.strip() if availability_tag else ""

        # Star rating class string (e.g., "star-rating Three")
        rating_tag = article.find("p", class_="star-rating")
        rating_raw = ""
        if rating_tag:
            classes = rating_tag.get("class", [])
            rating_raw = classes[1] if len(classes) > 1 else ""

        books_data.append({
            "title": title,
            "price_raw": price_raw,
            "availability_raw": availability_raw,
            "rating_raw": rating_raw
        })

    return books_data


def scrape_catalog(max_pages: int = 3) -> list[dict]:
    """
    Main scraping function: iterates through catalog pages handling pagination.
    Defaults to 3 pages for testing purposes.
    """
    all_books = []
    current_url = BASE_URL

    for page in range(1, max_pages + 1):
        print(f"[INFO] Scraping page {page}: {current_url}")
        html = fetch_html(current_url)
        if not html:
            break

        books = parse_books_from_page(html)
        all_books.extend(books)

        # Look for pagination next button
        soup = BeautifulSoup(html, "html.parser")
        next_button = soup.find("li", class_="next")

        if next_button and next_button.find("a"):
            next_relative_url = next_button.find("a")["href"]
            current_url = urllib.parse.urljoin(current_url, next_relative_url)
        else:
            print("[INFO] Reached the last page of the catalog.")
            break

    return all_books