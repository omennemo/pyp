# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:51:19 2017

@author: cyruslentin
"""

# import modules
import pandas as pd

# create dataframe
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'gender': ['Male','Female','Female','Male','Female'],
        'race': ['black','brown','yellow','green','white'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, columns = ['name', 'age', 'gender', 'race', 'preTestScore', 'postTestScore'])
print(data)
print(df)

# count the number of non-NA values
print("Count Non-NA")
print(df['preTestScore'].count())
print(df['name'].count())

# sum
print("Sum")
print(df['age'].sum())

# mean preTestScore
print("Mean")
print(df['preTestScore'].mean())

# cumulative sum of preTestScores, moving from the rows from the top
print("CumSum")
print(df['preTestScore'].cumsum())

# summary statistics on preTestScore
print("Summary")
print(df['preTestScore'].describe())

# minimum value of preTestScore
print("Minimum")
print(df['preTestScore'].min())

# maximum value of preTestScore
print("Maximum")
print(df['preTestScore'].max())

# median value of preTestScore
print("Median")
print(df['preTestScore'].median())

# variance of preTestScore values
print("Variance")
print(df['preTestScore'].var())

# standard deviation of preTestScore values
print("StdDev")
print(df['preTestScore'].std())

# group count
print("Group Count")
print(df.groupby(['gender'])['name'].count())

# group sum
print("Group Sum")
print(df.groupby(['gender'])['age'].sum())

print("Group Mean")
print(df.groupby(['gender'])['age'].mean())

print("Group Describe")
print(df.groupby(['gender'])['age'].describe())

print(df.groupby(['gender','race'])['age'].describe())
print(df.groupby(['gender','race'])['age'].count())
print(df.groupby(['gender','race'])['age'].mean())