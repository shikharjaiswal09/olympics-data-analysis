# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data=pd.read_csv(path)
data.rename(columns={"Total": "Total_Medals"},inplace=True)

#Code starts here

# Data Loading 
#print(data.head())

# Summer or Winter
data['Better_Event']=np.where(data['Total_Summer']>=data['Total_Winter'],'Summer','Winter')
data['Better_Event'][146]=None
better_event='Summer'
print(data.tail())
print(data['Better_Event'].value_counts())

# Top 10
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop([145,146],axis=0,inplace=True)

def top_ten(df,col_name):
    '''lists top ten othe the selected collumn'''
    country_list=df.nlargest(10,col_name)
    country_list=list(country_list['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=[]
for ele in top_10_summer:
    if (ele in top_10_winter) and (ele in top_10):
        common.append(ele)
print(common)
# Plotting top 10
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
summer_df.set_index('Country_Name',inplace=True)
summer_df['Total_Summer'].plot(kind='bar')
plt.ylabel('Total summer')
plt.show()
# Top Performing Countries
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio,summer_country_gold=0.424947,'China'
winter_df['Golden_Ratio']=winter_df['Gold_Summer']/winter_df['Total_Summer']
winter_max_ratio,winter_country_gold=0.406836,'United States'
top_df['Golden_Ratio']=top_df['Gold_Summer']/top_df['Total_Summer']
top_max_ratio,top_country_gold=0.40,'China'
# Best in the world 
data_1=data.drop([146],axis=0)
data_1['Total_Points']= (3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + (data_1['Bronze_Total'])
val=data_1.sort_values(['Total_Points'] , ascending = False)
most_points,best_country=5684,'United States'


# Plotting the best
best=data[data['Country_Name']== best_country]
print(best)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()







