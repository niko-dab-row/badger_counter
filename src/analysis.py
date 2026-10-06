import pandas as pd

df = pd.read_csv("data/sightings.csv")

print("Total badgers:")
print(df["badgers"].sum())
