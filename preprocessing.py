
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Încărcare și curățare
recipes = pd.read_csv("greenrec_dataset.csv")
recipes.dropna(inplace=True)

# Normalizare
scaler = MinMaxScaler()
recipes[['HSI', 'ESI', 'PPI']] = scaler.fit_transform(recipes[['HSI', 'ESI', 'PPI']])
recipes.to_csv("processed_recipes.csv", index=False)
