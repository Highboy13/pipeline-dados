from utils import load_csv, save_csv

def main():
    df = load_csv("data/raw/books.csv")
    # Exemplo de transformação simples
    df["popularity"] = df["ratings_count"] / df["ratings_count"].max()
    save_csv(df, "data/processed/books_clean.csv")

if __name__ == "__main__":
    main()