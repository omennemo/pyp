#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:46:57 2017

@author: nimeshvellera
"""

import pandas as pd
import numpy as np
import os
#Setting path
default_path = "/Users/nimeshvellera/Documents/201704-NMIMS-MTech-DS-Python/assignments"
os.chdir(default_path)
#reading data file
df = pd.read_csv("./patient-data.csv")

#Viewing Data
df.head()
#Achieving Column Names
print(df.columns)
#Checking Data Quality
df.groupby(['Race'])['Name'].count()
#Cleaning up
df['Race'] = np.where(df['Race']=='Dog','Unknown', df['Race'])
#Checking Data Quality
df.groupby(['Gender'])['Name'].count()
#Cleaning up
for i in range(1,100):
    df.ix[i,'Gender'] = df.ix[i,'Gender'].strip()
#Cleaning up
df['Smokes'] = np.where(df['Smokes'] == 'False', 'No', df['Smokes'])
df['Smokes'] = np.where(df['Smokes'] == 'True', 'Yes', df['Smokes'])

df.groupby(['Smokes'])['Name'].count()

df.groupby(['State'])['Name'].count()

#Cleaning up
df['State'] = np.where(df['State'] == 'Georgia,xxx', 'Georgia', df['State'])

#Establish Different varieties of data values
df.groupby(['Pet'])['Name'].count()

#Cleaning up
df['Pet'] = np.where(df['Pet'] == 'CAT', 'Cat', df['Pet'])
df['Pet'] = np.where(df['Pet'] == 'DOG', 'Dog', df['Pet'])
df['Pet'] = np.where(df['Pet'] == 'NONE', None, df['Pet'])
df['Pet'] = np.where(df['Pet'] == 'None', None, df['Pet'])

df.groupby(['HealthGrade'])['Name'].count()

df['HealthGrade'] = np.where(df['HealthGrade'] == 99, 'Unknown', df['HealthGrade'])

df.head()

df = df.assign(BodyMassIndex=df['WeightInKgs']/(df['HeightInCms']/100)**2)

df = df.assign(BMILabel="")
df['BMILabel'] = np.where(df['BodyMassIndex'] < 18.5 , 'Underweight', df['BMILabel'])
df['BMILabel'] = np.where((df['BodyMassIndex'] > 18.5) , 'Normal', df['BMILabel'])
df['BMILabel'] = np.where((df['BodyMassIndex'] >= 18.5) & (df['BodyMassIndex'] < 25.0) , 'Normal', df['BMILabel'])
df['BMILabel'] = np.where((df['BodyMassIndex'] >= 25.0) & (df['BodyMassIndex'] < 30.0) , 'Overweight', df['BMILabel'])
df['BMILabel'] = np.where(df['BodyMassIndex'] >=30, 'Obese', df['BMILabel'])

#Convert column data from int to string then remap values as required
df['HealthGrade'] = df['HealthGrade'].astype(str)
df.head()
df['HealthGrade'] = df['HealthGrade'].map({"1": "Good Health", "2": "Normal", "3":"Bad Health"})


df.groupby(['HealthGrade'])['Name'].count()

df.groupby(['BMILabel'])['Name'].count()


#Displaying Top 10 records by BMI Value
df.iloc[df['BodyMassIndex'].nlargest(10).index.values]
#Displaying Bottom 10 records by BMI Value
df.iloc[df['BodyMassIndex'].nsmallest(10).index.values]

#Frequency Counts Gender > Race
df.groupby(['Gender','Race'])['Name'].count()

#Min Max and Mean values by Race > Gender
df.groupby(['Race', 'Gender'])['BodyMassIndex'].min()
df.groupby(['Race', 'Gender'])['BodyMassIndex'].max()
df.groupby(['Race', 'Gender'])['BodyMassIndex'].mean()

#Displaying records for dead individuals
print(df[df['Died'] == True])

#Data for Hispanic Females
print(df[(df['Race'] == "Hispanic") & (df['Gender'] == "Female")])

df.to_csv("./Sample.csv", index=False)
