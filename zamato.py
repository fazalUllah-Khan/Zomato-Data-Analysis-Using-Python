# Import necessary Python libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the data frame

dataframe= pd.read_csv("Zomato_data.csv")
# dataframe.head()
print(dataframe.head())

# Convert the data type of the “rate” column to float and remove the denominator

def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

# Obtain a summary of the data frame

dataframe.info()

# **********************************************************
# ****** VISUALIZATIONS ************************************
# ********************************************************** 

#  Examine data frame for any null values

sns.countplot(x=dataframe ['listed_in(type)'])
plt.xlabel("Type of resturant")

# print(dataframe['listed_in(type)'].isnull().sum())

# Which type of resturants are prefered - Visualization 

grouped_data= dataframe.groupby('listed_in(type)') ['votes'].sum()
result= pd.DataFrame ({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of resturant" , c="red" , size=20)
plt.ylabel("Votes" , c="red" , size=20)

# restaurant’s name that received the maximum votes

max_votes= dataframe ['votes'].max()
resturant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print ("Resturant (s) with maximum votes: ")
print(resturant_with_max_votes)

# Online Vs dine in orders

sns.countplot(x=dataframe['online_order'], palette={'blue', 'yellow'})

# Visualize Ratings distribution

plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distributions")
plt.show()

#approx_cost(for two people)

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

# Compare online orders receive higher ratings OR offline orders

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=dataframe,  palette={'green', 'red'})

# visualize which kind of resturants accept which kind of orders more e.g offline,online etc

pivot_table= dataframe.pivot_table(index='listed_in(type)' , columns='online_order' , aggfunc='size' , fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed in (Type)")
plt.show()

