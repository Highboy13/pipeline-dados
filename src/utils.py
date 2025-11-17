import pandas as pd

def load_csv(path):
    return pd.read_csv(on_bad_lines="skip")

def save_csv(df, path):
    df.to_csv(path, index=False)
