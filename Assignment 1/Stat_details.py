# Set B 3).Write a Python program to view basic statistical details of the data.

import pandas as pd
data = pd.read_csv("SOCR-HeightWeight.csv")
print(data.describe())
