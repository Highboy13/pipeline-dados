import pandas as pd
from src.transform import main
import os

def test_etl_runs():
    # Executa processo ETL
    main()

    # Verifica se o arquivo foi gerado
    assert os.path.exists("data/processed/books_clean.csv")

def test_processed_has_popularity_column():
    df = pd.read_csv("data/processed/books_clean.csv")
    assert "popularity" in df.columns
