import pandas as pd
import numpy as np

# Create a series from a list

marks = pd.Series([90, 80, 70, 60], index=['Math', 'Science', 'English', 'History'])
print(marks)

# creating a dataframe from a dictionary

inf0 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Tokyo', 'Paris']})

print(inf0)

# creating a dataframe from Numpy array

data = np.array([["tejas", 25, "New York"],["suresh", 30, "London"],])
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)