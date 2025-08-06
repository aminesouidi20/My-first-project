import pandas as pd

data = pd.read_csv("data.csv")

print("🔍 معدل تركيز كل معدن:")
print(data.mean(numeric_only=True))
