import pandas as pd
from config import OUTPUT_FILE


def export_to_excel(data: list[dict], filename: str = OUTPUT_FILE) -> str | None:
    """Converts clean data into a Pandas DataFrame and exports it to an Excel file."""
    if not data:
        print("[EXPORTER] No data available for export.")
        return None

    try:
        df = pd.DataFrame(data)

        # Rename columns for professional formatting
        df.rename(
            columns={
                "title": "Book Title",
                "price_gbp": "Price (£)",
                "rating": "Rating (1-5)",
                "in_stock": "In Stock"
            },
            inplace=True
        )

        # Export DataFrame to Excel
        df.to_excel(filename, index=False, engine="openpyxl")
        print(f"[EXPORTER] Data successfully exported to: {filename}")
        return filename

    except Exception as e:
        print(f"[EXPORTER] Error saving Excel file: {e}")
        return None