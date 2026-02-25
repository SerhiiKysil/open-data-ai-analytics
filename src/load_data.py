import pandas as pd
from pathlib import Path


def load_data(file_path):
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')
    print(f"Розмір датасету: {df.shape}")
    return df


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "raw" / "reestrtz01.01.2026.csv"


    df = load_data(DATA_PATH)
    print("\nПерші 5 рядків:")
    print(df.head())