import pandas as pd

EXPECTED_COLUMNS = [
    "bookID", "title", "authors", "average_rating",
    "isbn", "language_code", "ratings_count", "text_reviews_count"
]

def validate_schema(df: pd.DataFrame):
    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes no dataset: {missing}")
    return True

if __name__ == "__main__":
    df = pd.read_csv("data/raw/books.csv")
    validate_schema(df)
    print("✔ Schema validado com sucesso!")
