import pandas as pd

df = pd.read_excel("aquasec_july.xlsx")
# Modify this as per your processing logic
summary = df.describe()
summary.to_csv("aquasec_summary.csv", index=False)
