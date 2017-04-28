# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:09:54 2017
@filename: 04Z-Patient.Py
@author: cyruslentin
"""

# import
import pandas as pd
import numpy as np
import os

#reading data file
df = pd.read_csv("./data/patient-data.csv")
default_path = "/Users/nimeshvellera/Documents/201704-NMIMS-MTech-DS-Python/assignments"
os.chdir(default_path)
#reading data file
df = pd.read_csv("./patient-data.csv")


# view Data
print(df.head())
# check Column Names
print(df.columns)

##################
# checking
##################

# check Race
print("Race")
print(df.groupby(['Race'])['Name'].count())
print("")

# check Gender
print("Gender")
print(df.groupby(['Gender'])['Name'].count())
print("")

# check Smokes
print("Smokes")
print(df.groupby(['Smokes'])['Name'].count())
print("")

# check State
print("State")
print(df.groupby(['State'])['Name'].count())
print("")

# check Pet
print("Pet")
print(df.groupby(['Pet'])['Name'].count())
print("")

# check health
print("Health")
print(df.groupby(['HealthGrade'])['Name'].count())
print("")

# check Diead
print("Died")
print(df.groupby(['Died'])['Name'].count())
print("")

##################
# cleaning
##################

# clean Race
print("Original")
print(df.groupby(['Race'])['Name'].count())
df['Race'] = np.where(df['Race']=='Dog','Unknown', df['Race'])
print("")
print("Cleaned")
print(df.groupby(['Race'])['Name'].count())


# clean Gender
print("Original")
print(df.groupby(['Gender'])['Name'].count())
print("")
df['Gender'] = df['Gender'].str.strip()
print("Cleaned")
print(df.groupby(['Gender'])['Name'].count())

# cleaning Smokes
print("Original")
print(df.groupby(['Gender'])['Name'].count())
print("")
df['Smokes'] = np.where(df['Smokes'] == 'False', 'No', df['Smokes'])
df['Smokes'] = np.where(df['Smokes'] == 'True', 'Yes', df['Smokes'])
print("Cleaned")
print(df.groupby(['Smokes'])['Name'].count())

# clean State
print("Original")
print(df.groupby(['State'])['Name'].count())
print("")
df['State'] = np.where(df['State'] == 'Georgia,xxx', 'Georgia', df['State'])
print("Cleaned")
print(df.groupby(['State'])['Name'].count())

# clean Pet
print("Original")
print(df.groupby(['Pet'])['Name'].count())
print("")
df['Pet'] = df['Pet'].str.title()
print("Cleaned")
print(df.groupby(['Pet'])['Name'].count())

# clean health
print("Original")
print(df.groupby(['HealthGrade'])['Name'].count())
print("")
#print(type(df['HealthGrade'].iloc[0]))
#print(df['HealthGrade'].dtype())
# will not work
#df['HealthGrade'] = np.where(df['HealthGrade'] == 99, 'Unknown',      df['HealthGrade'])
#df['HealthGrade'] = np.where(df['HealthGrade'] == 1, 'Good Health', df['HealthGrade'])
# will work
#df['HealthGrade'] = np.where(df['HealthGrade'] == 99, 'Unknown',      df['HealthGrade'])
#df['HealthGrade'] = np.where(df['HealthGrade'] == '1', 'Good Health', df['HealthGrade'])
#df['HealthGrade'] = np.where(df['HealthGrade'] == '2', 'Normal',      df['HealthGrade'])
#df['HealthGrade'] = np.where(df['HealthGrade'] == '3', 'Bad Health',  df['HealthGrade'])
# better use map
# convert to string & then map values as required
df['HealthGrade'] = df['HealthGrade'].astype(str)
df['HealthGrade'] = df['HealthGrade'].map({"1": "Good Health", "2": "Normal", "3":"Bad Health", "99":"Unknown"})
print("Cleaned")
print(df.groupby(['HealthGrade'])['Name'].count())
print("")

# compute BMIValue
df = df.assign(BMIValue=df['WeightInKgs']/(df['HeightInCms']/100)**2)
df['BMIValue'].head()

# compute BMILabel
df = df.assign(BMILabel="")
df['BMILabel'] = np.where(df['BMIValue']  < 18.5 , 'Underweight', 
                    np.where((df['BMIValue'] < 25 ) , 'Normal', 
                    np.where((df['BMIValue'] < 30) , 'Overweight', 
                    "Obese")))
df['BMILabel'].head()


##################
# reports
##################

# top 10 records by BMI Value
print("Top 10 BMI Value")
dfs = df.sort_values('BMIValue',ascending=False)
print(dfs.head(10))
# bot 10 records by BMI Value
print("Bottom 10 BMI Value")
dfs = df.sort_values('BMIValue',ascending=True)
print(dfs.head(10))

# frequency count - Gender > Race
print("Frequency Count - Gender > Race")
print(df.groupby(['Gender','Race'])['Name'].count())

# min mean max values - Race > Gender
print("Max - Gender > Race")
print(df.groupby(['Race','Gender'])['BMIValue'].max())
print("")
print("Mean - Gender > Race")
print(df.groupby(['Race','Gender'])['BMIValue'].mean())
print("")
print("Max - Gender > Race")
print(df.groupby(['Race','Gender'])['BMIValue'].mean())

# display data for dead 
print("Dead")
print(df[df['Died'] == True])
print(df.groupby(['Died'])['Name'].count())

# display data for Hispanic Females
print("Hispanic Females")
print(df[(df['Race'] == "Hispanic") & (df['Gender'] == "Female")])
