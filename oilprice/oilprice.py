# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:03:05 2020

@author: pual Nwosu
"""

import os
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
sns.set_style('white')

df = pd.read_excel('oilprices.xlsx')
plt.rc('font', family = 'serif' )

prc = pd.read_excel('edata.xlsx', sheet_name = 'OPCO')
exp = pd.read_excel('oilprices.xlsx', sheet_name = 'exports')
imp = pd.read_excel('edata.xlsx', sheet_name = 'imvsex')
spc = pd.read_excel('edata.xlsx', sheet_name = 'SCP')
cost = pd.read_excel('oilprices.xlsx', sheet_name = 'Sheet3')


c1 = [i for i in cost['Country']]
c2 = [i for i in cost['Pcost (bbl)']]
c3 = [i for i in cost['Tcost (bbl)']]


gdp = [20, 50, 65, 60, 45, 17, 65, 40, 60, 10, 50, 30, 14]

fr = [85, 89, 95, 86, 80, 82, 90, 92, 69, 86, 90, 39, 94]

country = ['Algeria', 'Angola', 'Congo', 'Equatorial Guinea', 'Garbon', 'Iran', 'Iraq', 'Kuwait', 'Libya', 'Nigeria', 'Saudi Arabia', 'United Arab Emirates', 'Venezuela']
tm1 = ['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']
tm2 = ['85%', '89%', '95%', '86%', '80%', '82%', '90%', '92%', '69%', '86%', '90%', '39%', '94%']






x = np.arange(0, len(gdp))
y = np.arange(0, len())


fig, ax = plt.subplots(figsize = (20,14))
plt.scatter(gdp, fr, s = 150, edgecolor = 'black', linewidths = 4,  c = 'r')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False) 
plt.xlabel('GDP%', fontsize = 15, fontweight = 'bold')
plt.ylabel('Total Exports(%)', fontsize = 20, fontweight = 'bold')
plt.xticks(fontsize = 20, fontweight  = 'bold')
plt.yticks(fontsize = 20, fontweight  = 'bold')
plt.grid(which = 'major', axis = 'y')
plt.title('OPEC Members Overdependence on Oil Revenue', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
for i, v, m in list(zip(gdp, fr, country)):
    ax.text(i+0.5, v, m, fontsize = 20, color = 'white', fontweight = 'bold', bbox = dict(facecolor = 'black', alpha = 0.5))
plt.show()


#cost per barrel and production cost
fig, ax = plt.subplots(figsize = (20,14))
plt.scatter(c2, c3, s = 150, edgecolor = 'black', linewidths = 4,  c = 'r')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False) 
plt.xlabel('Production cost ($/barrel)', fontsize = 15, fontweight = 'bold')
plt.ylabel('Total cost ($/barrel)', fontsize = 15, fontweight = 'bold')
plt.grid(which = 'major', axis = 'y')
plt.title('Production cost and Total cost for Diffrent Countries', fontsize = 15, fontweight = 'bold')
for i, v, m in list(zip(c2, c3, c1)):
    ax.text(i+0.1, v, m, fontsize = 13, color = 'white', fontweight = 'bold', bbox = dict(facecolor = 'black', alpha = 0.5))
plt.show()




prc['size'] = prc['Oil Price']*8

exp['Exports'] = exp['Exports']*100
imp['Imports'] = imp['Imports']*1000
imp['Exports'] = imp['Exports']*1000


TOT = 44964000

#df  = df[-(df['Year'] <= 1973)]

df['Low'] = pd.to_numeric(df['Low'])
df['High'] = pd.to_numeric(df['High'])
df1 = df[-(df['Year'] >= 2000)]
df2 = df[df['Year'] >= 2000]
#df.set_index('Causes', inplace = True)

#plt.figure(figsize = (32,16))
#plt.plot(df['Year'], df['Average'], 'b+')
#plt.plot(df['Year'], df['Low'], 'ro')
#plt.plot(df['Year'], df['High'], 'y*')
#plt.xticks(df['Year'])
#plt.plot(df['Year'], df['Average'], label = 'Average')
#plt.plot(df['Year'], df['Low'], label = 'Low')
#plt.plot(df['Year'], df['High'], label = 'High')
#plt.legend(fontsize = 15)
#plt.grid()
#plt.savefig('/Users/pual Nwosu/Desktop/oilprices.png')

data = df[['Causes','Year', 'High']]
data.set_index('Causes', inplace = True)


#data1 = df1[['Causes','Year', 'Average']]
#data1.set_index('Causes', inplace = True)
#data2 = df2[['Causes','Year', 'Average']]
#data2.set_index('Causes', inplace = True)


pos_text2 =  data.to_dict()

pos_text1 = {
   'OPEC oil embargo ended': (1974, 30),
  'Stagflation': (1975, 30),
  'Economy recovered': (1976, 35),
#  'Fed raised and lowered rates': (1978, 30),
  'Iran-Iraq War, fed rate 20%': (1979, 50),
  'Iran oil embargo': (1980, 60),
  'Reagan cut taxes': (1981, 60),
  'Recession ends inflation': (1982, 65),
  'OPEC added to supply': (1987, 65),
  'Gulf War': (1990, 60),
  'SPR released oil': (1991, 60),
  'NAFTA allowed cheap oil from Mexico': (1994, 55),
  'Prices doubled': (1999, 55),
  'Recession and 9/11': (2001, 55),
  'Afghanistan War': (2002, 55),
  'Hurricane Katrina': (2005, 100),
  'Bernanke becomes Fed chair': (2006, 100),
  'Banking crisis': (2007, 120),
  'Financial crisis': (2008, 150),
  'Great Recession': (2009, 130),
  'Iran threatened Straits of Hormuz': (2012, 120),
  'The dollar rose 15%': (2014, 150),
  'U.S. shale oil increased': (2015, 100),
  'Dollar fell': (2016, 100),
  'OPEC cut oil supply to keep prices stable': (2017, 100),
  'As of April 2020. Pandemic reduced demand.': (2020, 100),
  }




ax = df.plot(kind = 'scatter', x = 'Year', y = 'High', figsize = (18,12) )
ax.axis([1969,2021,0,210])
ax.spines['right'].set_visible(False)             
#ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
plt.grid(which = 'major', axis = 'y')
plt.xticks(df['Year'], rotation = 'vertical')
for causes, pos_text in pos_text1.items():
    pos_data_x, pos_data_y = data.loc[causes]
    plt.annotate(causes, xy=(pos_data_x, pos_data_y), xytext=pos_text, fontsize = 15, fontweight = 'bold',  rotation = 'vertical',
    arrowprops=dict(facecolor='black', width=3, shrink=1, headwidth=8))
    plt.plot(pos_data_x, pos_data_y, "bs")
ax.plot(df['Year'], df['High'], 'b', label = 'Highest Oil price for the Year')
ax.plot(df['Year'], df['Average'], 'go')
ax.plot(df['Year'], df['Average'], 'g--', label = 'Average Oil price for the Year')
ax.plot(df['Year'], df['Low'], 'ro')
ax.plot(df['Year'], df['Low'], 'r', label = 'Lowest Oil price for the Year')
plt.legend(loc = 'upper left', fontsize = 15)
#ax.yaxis.tick_right()                        
plt.ylabel('PRICE($/barrel)', fontsize = 15, fontweight = 'bold')
plt.xlabel('')
plt.tick_params(labeltop = False, labelright = True)
plt.title('Variation in WTI Oil Price', fontsize = 15, fontweight = 'bold')
plt.show()
#df2.plot(kind = 'scatter', x = 'Year', y = 'Average', figsize = (10,7) )
#plt.axis([2000,2021,0,190])
#plt.xticks(df2['Year'], rotation = 'vertical')
#plt.grid()
#for causes, pos_text in pos_text2.items():
#    pos_data_x, pos_data_y = data2.loc[causes]
#    plt.annotate(causes, xy=(pos_data_x, pos_data_y), xytext=pos_text,rotation = 'vertical',
#    arrowprops=dict(facecolor='black', width=3, shrink=1, headwidth=8))
#    plt.plot(pos_data_x, pos_data_y, "rs")
#plt.plot(df2['Year'], df2['Average'], 'b')
#plt.savefig('/Users/pual Nwosu/Desktop/2000.png')
#
#
#
#plt.xticks(df['Year'], rotation = 'vertical')
#plt.xlabel('Year', fontsize = 15)
#plt.ylabel('Avg_price', fontsize = 15)
#plt.savefig('/Users/pual Nwosu/Desktop/oilprices.png')




#relationship between oil production, consumption and price
ax = prc.plot(kind="scatter", x="Production", y="Consumption",
             alpha=0.4,    s=prc["size"], label="Oil Price",
             figsize=(12,10),    c="Oil Price", cmap=plt.get_cmap("rainbow"),
             colorbar=True,    sharex=False) 
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False) 
plt.legend(fontsize = 15)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Oil Production in Thousand Barrels', fontsize = 15, fontweight = 'bold')
plt.xlabel('Oil Production in Thousand Barrels', fontsize = 15, fontweight = 'bold')
plt.text(31000, 93000, 'Oil Price is in $/barrel', fontsize = 15)
plt.title('Relationship Between Oil Production, Oil Consumption and Oil Price', fontsize = 15, fontweight = 'bold')
plt.show()



#prc.plot(kind="scatter", x="Year", y="Consumption",
#             alpha=0.4,    s=prc["Oil Price"], label="Oil Price", 
#             figsize=(10,7),    c="Oil Price", cmap=plt.get_cmap("jet"),
#             colorbar=True,    sharex=False) 



#increase in production over the years
fig, ax = plt.subplots(figsize = (12,10))
ax.plot(prc['Year'], prc['Production'], 'y')
ax.plot(prc['Year'], prc['Production'], 'ys', markersize = 7, label = 'Oil Consumption in Thousand Barrels')
ax.plot(prc['Year'], prc['Consumption'], 'r')
ax.plot(prc['Year'], prc['Consumption'], 'rH', markersize = 7, label = 'Oil Production in Thousand Barrels')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False) 
plt.legend(loc = 'upper left', fontsize = 15)    
plt.xlabel('')
plt.tick_params(labeltop = False, labelright = True)        
plt.grid(which = 'major', axis = 'y')
plt.title('Increase in Production and Consumption over the Years', fontsize = 15, fontweight = 'bold')
plt.show()




#Top 10 oil exporters
exp2 = imp[['Country', 'Exports']].sort_values(by = 'Exports', ascending = True)
#oilc2 = oilc2[-(oilc2[2019].isna())]
exp2 = exp2.set_index('Country')
rx = exp2.tail(15)
rx.columns = ['OIL EXPORTS']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = '#9b59b6')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Oil Exports', fontsize = 15, fontweight = 'bold')
for i, v in enumerate(rx['OIL EXPORTS']):
    ax.text(v + 5, i + 0.25, str('{}%'.format(round((v/TOT)*100, 2))), fontsize = 13)   
plt.show()



#Top 10 Oil importers
ixp2 = imp[['Country', 'Imports']].sort_values(by = 'Imports', ascending = True)
#oilc2 = oilc2[-(oilc2[2019].isna())]
ixp2 = ixp2.set_index('Country')
rx = ixp2.tail(15)
rx.columns = ['OIL IMPORTS']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = '#3498db')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Oil Imports', fontsize = 15, fontweight = 'bold')
for i, v in enumerate(rx['OIL IMPORTS']):
    ax.text(v + 5, i + 0.25, str('{}%'.format(round((v/TOT)*100, 2))), fontsize = 13)    
plt.show()


#Spot Crude oil prices
fig, ax = plt.subplots(figsize = (12,10))
ax.plot(spc['Year'], spc['Dubai'], 'k--')
ax.plot(spc['Year'], spc['Dubai'], 'ks', markersize = 5, label = 'Dubai')
ax.plot(spc['Year'], spc['Brent'], 'r')
ax.plot(spc['Year'], spc['Brent'], 'rH', markersize = 5, label = 'Brent')
ax.plot(spc['Year'], spc['Nigeria Forcados'], 'y--')
ax.plot(spc['Year'], spc['Nigeria Forcados'], 'yD', markersize = 5, label = 'Nigeria Forcados')
ax.plot(spc['Year'], spc['West Texas'], 'g')
ax.plot(spc['Year'], spc['West Texas'], 'go', markersize = 5, label = 'West Texas Intermediate')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.legend(loc = 'upper left', fontsize = 12, ncol = 2, title = 'Benchmarks:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Spot Oil Prices over the past 50 Years for Differnt Benchmarks', fontsize = 15, fontweight = 'bold')
plt.show()