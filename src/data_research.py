import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "reestrtz01.01.2026.csv"

df = pd.read_csv(DATA_PATH, sep=';', low_memory=False)

# 1) Частка електромобілів
total_cars = len(df)
electro_cars = len(df[df['FUEL'] == 'ЕЛЕКТРО'])
electro_pct = (electro_cars / total_cars) * 100
print(f"1. Частка електромобілів: {electro_pct:.2f}%")

# 2) Найпопулярніший колір
top_color = df['COLOR'].mode()[0]
print(f"2. Найпопулярніший колір авто: {top_color}")

# 3) Більшість авто випущені до 2015 року
df['MAKE_YEAR'] = pd.to_numeric(df['MAKE_YEAR'], errors='coerce')
cars_before_2015 = len(df[df['MAKE_YEAR'] < 2015])
pct_before_2015 = (cars_before_2015 / len(df['MAKE_YEAR'].dropna())) * 100
print(f"3. Частка авто, випущених до 2015 року: {pct_before_2015:.2f}%")