import pandas as pd

# تحميل الملف من GitHub مباشرة
url = "https://raw.githubusercontent.com/aminesouidi20/butter-metal-analyzer/main/data.csv"
data = pd.read_csv(url)

print("🔍 معدل تركيز كل معدن:")
print(data.mean(numeric_only=True))
