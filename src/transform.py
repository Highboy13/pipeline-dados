import pandas as pd
from utils import load_csv, save_csv
from validate_schema import validate_schema

def main():
    # Carrega dados brutos
    df = load_csv("data/raw/books.csv")

    # Valida schema
    validate_schema(df)

    # Limpeza básica
    df = df.drop_duplicates()
    df = df.dropna(subset=["title", "authors"])

    # Criação de campo derivado: popularidade
    df["popularity"] = df["ratings_count"] * df["average_rating"]

    # Salvar dataset processado
    save_csv(df, "data/processed/books_clean.csv")

    print("✔ ETL concluído!")

if __name__ == "__main__":
    main()
