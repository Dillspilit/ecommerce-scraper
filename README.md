# 🛒 E-Commerce Web Scraper & Excel Exporter

An automated Python data extraction pipeline that parses product catalog data from dynamic e-commerce websites, cleans and formats the raw data, and exports structured results directly into Microsoft Excel (`.xlsx`) spreadsheets.

---

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **Web Scraping:** Requests, BeautifulSoup4
* **Data Processing & Analytics:** Pandas
* **Excel Generation:** OpenPyXL
* **Environment Management:** python-dotenv

---

## 📋 Key Features & Architecture

* **Pagination Handling:** Automatically parses across multiple pages using dynamic HTML link extraction.
* **Resilient Data Cleaning:** Cleans price formats into `float` values, converts string ratings into numerical scale (1–5), and normalizes stock availability into boolean values using Regex.
* **Structured Export:** Generates clean Excel spreadsheets with custom header column mappings.
* **Modular Design:** Built with decoupled architecture (`scraper`, `cleaner`, `exporter`, `config`, `main`) for high maintainability.

---

## 📂 Project Structure

```plaintext
├── config.py         # Environment variables and HTTP headers loader
├── scraper.py        # Web scraping logic and HTML parsing
├── cleaner.py        # Data normalization, typing, and regex cleaning
├── exporter.py       # Pandas DataFrame creation and Excel exporting
├── main.py           # Pipeline orchestrator
├── requirements.txt  # Dependency list
├── .env              # Environment secrets (ignored by Git)
└── .gitignore        # Git exclusion rules
```
🚀 Quick Start
1. Clone the Repository & Set Up Virtual Environment
Bash

git clone [https://github.com/your-username/ecommerce-scraper.git](https://github.com/your-username/ecommerce-scraper.git)
cd ecommerce-scraper

python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows

2. Install Dependencies
Bash

pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory:
Фрагмент кода

BASE_URL=[https://books.toscrape.com/](https://books.toscrape.com/)
OUTPUT_FILE=scraped_books.xlsx
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

4. Run the Script
Bash

python main.py

