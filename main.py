# Import all the necessary libraries of panda
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
# Create a DataFrame from CSV file
df_airbnb = pd.read_csv('/kaggle/input/new-york-city-airbnb-open-data/AB_NYC_2019.csv')
df_airbnb.head(5)
# check the datatype
df_airbnb.info()
# Check null value
df_airbnb.isnull().sum()
# to check each column unique value I used nunique().
df_airbnb.nunique()
df_airbnb.columns.to_list()
# remove unnecessary columns 
droplist=['host_name',
 'neighbourhood',
 'latitude',
 'longitude','reviews_per_month',
 'calculated_host_listings_count']
df2=df_airbnb.drop(droplist,axis='columns')
#remove empty cells with dropna
df2.dropna(inplace=True)
df2.info()
df2.to_csv('ab_nyc_df2.csv', index=False)
df2.to_csv(r'C:\All Project\test.csv', index=False)
# remove duplicate values, making a different name
df3=pd.read_csv('/kaggle/working/ab_nyc_df2.csv')
df3.drop_duplicates(inplace=True)
#Use to_datetime() to format a column’s data info 
df3['last_review']=pd.to_datetime(df3['last_review'])
#use query to fetch value (business qn)
df3_queryvalue=df3.query('price > 1000 & minimum_nights <3')
df3_queryvalue.groupby('neighbourhood_group').count()
df3_queryvalue.head(5)
#Lets check the total neighbourhood group percentage
neighbourhood_group_percentage_share=df3_queryvalue['neighbourhood_group'].value_counts().reset_index()
neighbourhood_group_percentage_share.columns=['neighbourhood_group','count']
neighbourhood_group_percentage_share['total_percentage']=neighbourhood_group_percentage_share['count']/neighbourhood_group_percentage_share['count'].sum()*100
neighbourhood_group_percentage_share
labels=neighbourhood_group_percentage_share.neighbourhood_group.tolist()
data=neighbourhood_group_percentage_share.total_percentage.to_list()
colors=['skyblue','green','orange']
explode=[0,0,0]
plt.pie(data, labels=labels, explode=explode,autopct='%1.1f%%',colors=colors)
plt.title('Area based luxury rooms in percentage')
plt.show()
df4_airbnb=df3_queryvalue[['neighbourhood_group','room_type','price','availability_365','minimum_nights']]
df4_airbnb=df4_airbnb.groupby('neighbourhood_group').apply(lambda x : x.sort_values(by = 'price', ascending = False).reset_index(drop = True))
df4_airbnb
# Minimum_nights based room price and room type
sns.barplot(x = 'minimum_nights', y = 'price', hue = 'room_type', data = df4_airbnb)
plt.title("Area based top luxury room")
plt.show()
df4_airbnb.count()
# display availabiliyu_365 and price in group/cluster
plt.scatter(x='availability_365',y='price',data = df4_airbnb)
plt.title("Price wise rom avaialability")
import seaborn as sns
# create plot
sns.barplot(x = 'neighbourhood_group', y = 'price', hue = 'room_type', data = df4_airbnb)
plt.title("Area based top luxury room")
plt.show()

airbnb_review=df3_queryvalue[['number_of_reviews','availability_365','last_review', 'neighbourhood_group']]
h=airbnb_review.sort_values(by='neighbourhood_group')
print(h)
h.plot.line(x='last_review', y='number_of_reviews')
plt.title("Year based review in number")

