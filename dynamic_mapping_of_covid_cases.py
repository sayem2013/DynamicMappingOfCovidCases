# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:36:08 2021

@author: motta
"""

import pandas as pd 

import geopandas as gpd

data = pd.read_csv('time_series_covid19_confirmed_global.csv')

#grouping data by country

data = data.groupby('Country/Region').sum()

data = data.drop(columns = ['Lat', 'Long'])

data_transposed = data.T

# data_transposed.plot(y = ['Bangladesh', 'Canada', 'US', 'Italy'], use_index = True, figsize = (8,8), marker ='*')

world = gpd.read_file(r'D:\Covid\World_Map.shp')




world.replace('Viet Nam', 'Vietnam', inplace = True)
world.replace('Brunei Darussalam', 'Brunei', inplace = True)
world.replace('Cape Verde', 'Cabo Verde', inplace = True)
world.replace('Democratic Republic of the Congo', 'Congo (Kinshasa)', inplace = True)
world.replace('Congo', 'Congo (Brazzaville) ', inplace = True)
world.replace('Czech Republic', 'Czechia', inplace = True)
world.replace('Swaziland', 'Eswatini', inplace = True)
world.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
world.replace('Korea, Republic of', 'Korea, South', inplace = True)
world.replace("Lao People's Democratic Republic", 'Laos', inplace = True)
world.replace('Libyan Arab Jamahiriya', 'Libya', inplace = True)
world.replace('Republic of Moldova ', 'Moldova ', inplace = True)
world.replace('The former Yugoslav Republic of Macedonia', 'North Macedonia', inplace = True)
world.replace('Syrian Arab Republic', 'Syria', inplace = True)
world.replace('Taiwan', 'Taiwan*', inplace = True)
world.replace('United Republic of Tanzania', 'Tanzania', inplace = True)
world.replace('United States', 'US', inplace = True)
world.replace('Palestine', 'West Bank and Gaza', inplace = True)


#for index, row in data.iterrows():
#    if index not in world['NAME'].to_list():
#        print(index + ' :is not in the list')
#  else:
#        pass

merge = world.join(data, on = 'NAME', how = 'right')

ax = merge.plot(column = '2/1/20',
                cmap = 'OrRd',
                figsize = (10,10),
                legend = True,
                scheme = 'user_defined',
                classification_kwds = {'bins':[10,20,50,100,500,1000,5000,10000,50000]},
                edgecolor = 'black',
                linewidth = 0.4
                )