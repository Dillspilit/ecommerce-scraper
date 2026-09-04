from cleaner import process_book_data
from exporter import export_to_excel
from scraper import scrape_catalog


def main():
    print("=== Starting E-Commerce Catalog Scraper ===")
    
    # Step 1: Scrape raw data
    print("Step 1/3: Scraping catalog data...")
    raw_data = scrape_catalog(max_pages=3)
    
    if not raw_data:
        print("[MAIN] Error: Failed to retrieve data.")
        return

    print(f"[MAIN] Scraped {len(raw_data)} raw records.")

    # Step 2: Clean and parse data
    print("Step 2/3: Cleaning and processing data...")
    cleaned_data = process_book_data(raw_data)

    # Step 3: Save results to Excel
    print("Step 3/3: Exporting results to Excel...")
    output_file = export_to_excel(cleaned_data)

    if output_file:
        print(f"=== Execution Complete! Output saved to '{output_file}'. ===")


if __name__ == "__main__":
    main()