# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:41:02 2020

@author: pual Nwosu
"""

#show vwnuzuela increase in reserves and decrease in produvtion

#show niferia current consumption, compare it with developed countries production



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
import datetime as dt
plt.rc('font', family = 'serif')
#plt.rc('lines', lw = 4, c = 'r')

res = pd.read_excel('edata.xlsx', sheet_name = 'RD')
opd = pd.read_excel('edata.xlsx', sheet_name = 'OPD')

rsv = pd.read_excel('edata.xlsx', sheet_name = 'Reserves')
opo = pd.read_excel('edata.xlsx', sheet_name = 'Oil Production')
vop = pd.read_csv('opo.csv')


rop = pd.read_excel('rop.xlsx')

rop = rop.drop_duplicates(keep = 'first')

rop['Price'] = rop['Price'].str.strip('$')
rop['Price'] = pd.to_numeric(rop['Price'])



rop['no'] =rop['Date'].dt.month
rop['day'] = rop['Date']. dt.day

rop['day'] = rop['day'].astype('str')

def month(x):
    if x == 12:
        return 'December'
    elif x == 1:
        return 'January'
    elif x == 2:
        return 'February'
    elif x == 3:
        return 'March'
    elif x == 4:
        return 'April'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'June'
    else:
        return 'July'
       
rop['month'] = rop['no'].apply(month)

rop['Month'] = rop['month'] + '-'+ rop['day']

rop['Month2'] =  rop['Month']

rop = rop.set_index(rop['Month'])


rsv[2019] = rsv[2019]*100 #ten million barrels (*10,000,000)
opo[2019] = opo[2019] #Thousand barrels (*100)


df = opo[opo['Country'].isin(['Iran', 'Venezuela', 'Saudi Arabia', 'Iraq', 'Kuwait', 'Canada'])]
df2 = rsv[rsv['Country'].isin(['Iran', 'Venezuela', 'Saudi Arabia', 'Iraq', 'Kuwait', 'Canada'])]

cp = [i for i in df[2019]]
cr = [i for i in df2[2019]]

#lb  = ['Iran', 'Venezuela', 'Saudi Arabia', 'Iraq', 'Kuwait', 'Canada',  'Russia']

lb1 = [i for i in df['Country']]
lb2 = [i for i in df2['Country']]


gr = [2.7, -37.7, 3.2, -26.4, -1.8, -3.5] #2019 decrease in production
gro = [5.1, -5.5, 6.7, 0.8, 0.9, 1.4]  #10 years decrease in production

gr1 = [2.7, 0, 0, 0, 0, 0]
gr2 = [0, -37.7, 0, 0, 0, 0]
gr3 = [0, 0, 3.2, 0, 0, 0]
gr4 = [0, 0, 0, -26.4, 0, 0]
gr5 = [0, 0, 0, 0, -1.8, 0]
gr6 = [0, 0, 0, 0, 0, -3.5]


cas1 = dict(zip(x, gr))

x = np.arange(0, len(lb1))
w = 0.3
y = x+w
cs1 = dict(zip(x, cr))
cs2 = dict(zip(y, cp))


#reserves vs Production for Top producers
fig = plt.figure(figsize = (12,10))
ax = fig.add_subplot(1,1,1)
#ax.yaxis([])
p1 = ax.bar(x, cr, width = w, color = 'g')
p2 = ax.bar(x+w, cp, width = w, color = 'y')
plt.xticks(x+w, lb1, fontsize = 14, fontweight = 'bold',  rotation = 45)
ax.legend((p1[0], p2[1]), ('Reserves in 10(Mbbls)', 'Production in (mbbls)'), loc = 'best', fontsize = 12)
for i, v in cs1.items():
    ax.text(i-0.1, v+100, str('{}Mbbls'.format(round(v))), rotation = 10, fontsize = 11, fontweight = 'bold')
for i, v in cs2.items():
    ax.text(i-0.1, v+500, str('{}mbbls'.format(round(v))), rotation = 45, fontsize = 11, fontweight = 'bold')
plt.text(1.7, 25500, '[10Mbbls - 10,000,000 barrels]', fontsize = 12, fontweight = 'bold')
plt.text(1.7, 24000, '[mbbls - 1000 barrels]', fontsize = 12, fontweight = 'bold')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
#plt.legend(loc = 'upper right', fontsize = 15)
plt.grid(which = 'major', axis = 'y')
plt.title('Comparing Current Reserves and Current Producton of Venezuela with other Top Reserves', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()


#Decrease in oil production 
fig, ax = plt.subplots(figsize = (12,10))
plt.ylim(-40, 40)
plt.xlim(x[0]-0.3,x[-1]+0.3)
ax.bar(x, gr1, color = 'blue', width = 0.3, label = 'Canada')
ax.bar(x, gr2, color = 'red', width = 0.3, label = 'Venezuela')
ax.bar(x, gr3, color = 'blue', width = 0.3, label = 'Iran')
ax.bar(x, gr4, color = 'red', width = 0.3, label = 'Iraq')
ax.bar(x, gr5, color = 'red', width = 0.3, label = 'Kuwait')
ax.bar(x, gr6, color = 'red', width = 0.3,label = 'Saudi Arabia')
plt.xticks(x, lb2, fontsize = 14, fontweight = 'bold',  rotation = 15)
plt.plot([x[0]-0.3, x[-1]+0.3], [0, 0], 'k--')

#ax.plot([(lab2[0]-3),(lab2[-1]+5)], [0,0], 'k--', lw = 3)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper right', fontsize = 15)
plt.grid(which = 'major', axis = 'y')
#plt.xticks(fontsize = 13, fontweight = 'bold', rotation = 15)
plt.title('2018 - 2019 Decrease in Oil Production by Top Reserves Holders', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 11, loc = 'right', y = -0.01)
for i, v in cas1.items():
    if v < 0:
        ax.text(i, v-2, str('{}%'.format(v)), fontsize = 13, fontweight = 'bold')
    else:
        ax.text(i, v+2, str('{}%'.format(v)), fontsize = 13, fontweight = 'bold')
plt.show()   


#vop['Venuzuela'] = uu
#uu = df.iloc[]
#uu = pd.DataFrame({'Venuzuela': uu})
        
#Variation in  Venezuela oil production over the years
fig, ax = plt.subplots(figsize = (12,10))
plt.plot(vop['Year'], vop['Venezuela'], 'b')
plt.plot(vop['Year'], vop['Venezuela'], 'bh', markersize = 7)
#plt.xticks(vop['Year'], rotation = 'vertical' )
plt.plot(vop['Year'][28:33], vop['Venezuela'][28:33], 'y')
plt.plot(vop['Year'][28:33], vop['Venezuela'][28:33], 'yh', markersize = 7, label = 'Maduro\'s Effect on Oil Production')
plt.plot(vop['Year'][32:], vop['Venezuela'][32:], 'r')
plt.plot(vop['Year'][32:], vop['Venezuela'][32:], 'rh', markersize = 7, label = 'Effect of US Sanctions on Oil Production')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
ax.xaxis.set_major_locator(plt.MaxNLocator(10))                            
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Production in Thousand Barrels', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'lower left', fontsize = 14, title = 'Causes of Decrease in Production:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Decrease in Venezuela Oil Poduction', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()







#plt.plot(vop['Year'], vop['Iran'], 'r')
#plt.plot(vop['Year'], vop['Iran'], 'rd', markersize = 7, label = 'Iran')
fig, ax = plt.subplots(figsize = (10,7))
plt.plot(vop['Year'], vop['Iran'], 'b')
plt.plot(vop['Year'], vop['Iran'], 'bh', markersize = 7)
#plt.xticks(vop['Year'], rotation = 'vertical' )
plt.plot(vop['Year'][32:], vop['Iran'][32:], 'r')
plt.plot(vop['Year'][32:], vop['Iran'][32:], 'rh', markersize = 7, label = 'Effect of US Sanctions on Oil Production')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
ax.xaxis.set_major_locator(plt.MaxNLocator(10))                            
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Production in Thousand Barrels', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper left', fontsize = 14, title = 'Causes of Decrease in Production:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Decrease in Iran Oil Poduction', fontsize = 15, fontweight = 'bold', loc= 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()





fig, ax = plt.subplots(figsize = (30,20))
plt.xlim(rop['Date'][0], rop['Date'].iloc[-1])
plt.plot(rop['Date'], rop['Price'], 'b')
plt.plot(rop['Date'], rop['Price'], 'b', label = 'Reduction in Global oil demand\ndue to coranavirus')
plt.plot([rop['Date'][0], rop['Date'].iloc[-1]], [0, 0], 'k--')
plt.plot(rop['Date'].loc['March-6':'April-9'], rop['Price'].loc['March-6':'April-9'], 'k', lw = 3, label = 'Saudi and Russia oil price war')
plt.plot(rop['Date'].loc['April-9':'April-20'], rop['Price'].loc['April-9':'April-20'], 'r', lw = 3, label = 'Reports of storage issues')
plt.plot(rop['Date'].loc['April-20':'May-1'], rop['Price'].loc['April-20':'May-1'], 'y', lw = 3, label = 'Oil markets start to rebalance')
plt.plot([rop['Date'].loc['April-20']], [rop['Price'].loc['April-20']], 'ro', markersize = 10)
plt.plot([rop['Date'].loc['May-1']], [rop['Price'].loc['May-1']], 'go', markersize = 10)
plt.plot([rop['Date'].loc['March-6']], [rop['Price'].loc['March-6']], 'ko', markersize = 10)
plt.plot([rop['Date'].loc['April-9']], [rop['Price'].loc['April-9']], 'ro', markersize = 10)
plt.plot(rop['Date'].loc['May-1':], rop['Price'].loc['May-1':], 'g', lw = 2, label = 'OPEC+ starts output cuts')
plt.text(rop['Date'].loc['March-9'], rop['Price'].loc['March-6'], 'Saudi - Russia oil price war starts', fontsize = 18, bbox = dict(facecolor = 'red', alpha = 0.5) )
plt.text(rop['Date'].loc['April-23'], rop['Price'].loc['April-20'], 'BLACK APRIL', fontsize = 18, bbox = dict(facecolor = 'red', alpha = 0.5) )
plt.text(rop['Date'].loc['May-4'], rop['Price'].loc['May-1'], 'OPEC+ starts historical cut', fontsize = 18, bbox = dict(facecolor = 'red', alpha = 0.5))
plt.text(rop['Date'].loc['April-13'], rop['Price'].loc['April-9'], 'Storage issues worsens', fontsize = 18, bbox = dict(facecolor = 'red', alpha = 0.5))
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True) 
ax.xaxis.set_major_locator(plt.MaxNLocator(10))                            
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in $ per barrel', fontsize = 25, fontweight = 'bold')
plt.xticks(fontsize = 25, fontweight  = 'bold')
plt.yticks(fontsize = 25, fontweight  = 'bold')
plt.legend(loc = 'upper right', fontsize = 20, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('January - July variation in oil price', fontsize = 30, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()
#
#
