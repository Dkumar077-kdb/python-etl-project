import pandas as pd

# Extract
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Transform
data_clean = data.dropna()
data_clean["sepal_area"] = data_clean["sepal_length"] * data_clean["sepal_width"]

# Load
data_clean.to_csv("output.csv", index=False)

print("ETL process completed. Output saved as output.csv")