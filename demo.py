import pandas as pd

# Demo data to simulate the 'winequality-red.csv'
data = {
    'fixed_acidity': [7.4, 7.8, 7.8, 11.2, 7.4],
    'volatile_acidity': [0.7, 0.88, 0.76, 0.28, 0.7],
    'citric_acid': [0.0, 0.0, 0.04, 0.56, 0.0],
    'residual_sugar': [1.9, 2.6, 2.3, 1.9, 1.9],
    'chlorides': [0.076, 0.098, 0.092, 0.075, 0.076],
    'free_sulfur_dioxide': [11.0, 25.0, 15.0, 17.0, 11.0],
    'total_sulfur_dioxide': [34.0, 67.0, 54.0, 60.0, 34.0],
    'density': [0.9978, 0.9968, 0.9970, 0.9980, 0.9978],
    'pH': [3.51, 3.20, 3.26, 3.16, 3.51],
    'sulphates': [0.56, 0.68, 0.65, 0.58, 0.56],
    'alcohol': [9.4, 9.8, 9.8, 9.8, 9.4],
    'quality': [5, 5, 5, 6, 5]
}

# Create a DataFrame from the demo data
df_demo = pd.DataFrame(data)

print(df_demo.head(10))  # Shows the first 10 rows of the dataset