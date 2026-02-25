import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "reestrtz01.01.2026.csv"
df = pd.read_csv(DATA_PATH, sep=';', low_memory=False)

print(f"Кількість дублікатів: {df.duplicated().sum()}")
print("\nПропущені значення:")
missing = df.isnull().sum()
print(missing[missing > 0])