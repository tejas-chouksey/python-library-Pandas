import pandas as pd
data = {"prooduct": ["pen","pencil","eraser","shopner","notebook","marker"],"price":[10,5,2,2,100,20],"stock":[100,60,200,80,150,120],"rating":[4.5,4.7,4.2,4.8,4.3,4.4]}
df = pd.DataFrame(data)
print(df)

# sort by a single column -> price,ascending

print(df.sort_values(by="price"))

# sort by a single column -> rating,decending

print(df.sort_values(by = 'rating',ascending = False))

# sort by multiple columns -> price and stock

print(df.sort_values(by = ['price','stock']))

# sort by index

print(df.sort_index(ascending=False))

# mean of numerical columns only
print(df.mean(numeric_only=True))

# median of numerical columns only
print(df.median(numeric_only=True))

# mode
print(df.mode())

# summary of numerical columns
print(df.describe())

# standard deviation of numerical columns only
print(df.std(numeric_only=True))

# count how many time each product appears
print(df['prooduct'].value_counts())
print(df['rating'].value_counts())

# count how many time each product appears and show percentages
print(df['prooduct'].value_counts(normalize=True))

# corr()
print(df['price'].corr(df['stock']))
print(df.corr(numeric_only=True))

# cov()
print(df['price'].cov(df['stock']))
print(df.cov(numeric_only=True))