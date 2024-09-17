# add your code here
import pandas as pd

data = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

country = data.groupby(['country']).points.agg([len, "mean"]).round(decimals=1)
country_cleaned = country.rename(columns={"county": 'country', 'len': "count", 'mean': "points"})

print (country_cleaned)

country_cleaned.to_csv("data/reviews-per-country.csv")