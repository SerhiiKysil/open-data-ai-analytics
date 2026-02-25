import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "reestrtz01.01.2026.csv"
FIGURES_DIR = BASE_DIR / "reports" / "figures"

df = pd.read_csv(DATA_PATH, sep=';', low_memory=False)

top_brands = df['BRAND'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_brands.values, y=top_brands.index, hue=top_brands.index, palette="viridis", legend=False)

plt.title('ТОП-10 марок зареєстрованих авто', fontsize=14)
plt.xlabel('Кількість реєстрацій', fontsize=12)
plt.ylabel('Марка авто', fontsize=12)

output_path = FIGURES_DIR / "top_10_brands.png"
plt.tight_layout()
plt.savefig(output_path)

print(f"Графік збережено у {output_path}")