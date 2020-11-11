# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:44:40 2020

@author: pual Nwosu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

res = pd.read_excel('edata.xlsx', sheet_name = 'RD')
opd = pd.read_excel('edata.xlsx', sheet_name = 'OPD')

rsv = pd.read_excel('edata.xlsx', sheet_name = 'Reserves')
opo = pd.read_excel('edata.xlsx', sheet_name = 'Oil Production')
vop = pd.read_csv('opo.csv')

imp = pd.read_excel('edata.xlsx', sheet_name = 'imp')
exp = pd.read_excel('edata.xlsx', sheet_name = 'exp')


imp2 = pd.read_excel('edata.xlsx', sheet_name = 'imp2')
exp2 = pd.read_excel('edata.xlsx', sheet_name = 'exp2')

bvl = ['OECD', 'Non-OECD', 'OPEC', 'Non-OPEC', 'Total World']

p1 = [0.036965542, 0.005869333, 0.00463076, 0.019913464, 0.013580516]
r1 = [-0.004543235,	-0.00059246, -7.65555E-05, -0.003776398, -0.001187235]


TWR = 1733.9
TWP = 95192
TOE = 70925 #Total oil exports in mbbls

k = []
p = []

        




res.columns = ['Year', 'OECD', 'Non-OECD', 'Non-OPEC2', 'Total World',
       'OPEC+', 'OPEC', 'Non-OPEC']
res.columns = res.columns
opd.columns = res.columns

plt.rc('font', family = 'serif' )


#10 Years change in Oil Production and Reserves Change
p
plt.ylim(-0.005,0.05)
plt.bar(bvl, p1, color = 'red')
plt.bar(bvl, r1)
plt.grid(which = 'major', axis = 'y')
plt.show()


#Total World Reserves
fig, ax = plt.subplots(figsize = (10,7))
ax.stackplot(res['Year'],  res['Non-OPEC'], res['OPEC'], labels = ('Non-OPEC', 'OPEC+'), colors = ('blue', 'red'), baseline = 'zero' )
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                                              
plt.grid(which = 'major', axis = 'y')
plt.legend(loc = 'upper left', ncol = 2, title = 'Total World Reserves by:', title_fontsize = 15)
plt.title('Increase in Total World Reseves', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()



#Oil Reserves  
fig, ax = plt.subplots(figsize = (14,10))
ax.plot(res['Year'], res['OPEC+'], 'k--')
ax.plot(res['Year'], res['OPEC+'], 'ko', markersize = 7, label = 'OPEC+')
ax.plot(res['Year'], res['OPEC'], 'r')
ax.plot(res['Year'], res['OPEC'], 'ro', markersize = 7, label = 'OPEC')
ax.plot(res['Year'], res['Non-OPEC'], 'y')
ax.plot(res['Year'], res['Non-OPEC'], 'yo', markersize = 7, label = 'Non-OPEC')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)        
plt.tick_params(labeltop = False, labelright = True)                                 
#plt.xticks(res['Year'], rotation = 'vertical')
plt.grid(which = 'major', axis = 'y')
plt.xticks(fontsize = 15, fontweight = 'bold')
plt.yticks(fontsize = 15, fontweight = 'bold')
plt.legend(loc = 'upper left', markerfirst = True, fancybox = True)
plt.text(1980, 1150, 'OPEC+ total reserves: {}Bbbls, {}%'.format(round(res['OPEC+'].iloc[-1],2), round((res['OPEC+'].iloc[-1]/res['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1980, 1100, 'OPEC total reserves: {}Bbbls, {}%'.format(round(res['OPEC'].iloc[-1],2), round((res['OPEC'].iloc[-1]/res['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1980, 1050, 'Non-OPEC total reserves: {}Bbbls, {}%'.format(round(res['Non-OPEC'].iloc[-1],2), round((res['Non-OPEC'].iloc[-1]/res['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1987, 1300, 'World total reserves: {}Bbbls'.format(round(res['Total World'].iloc[-1],2)), fontsize = 14, fontweight = 'bold')
plt.text(1980, 900, '(Bbbls = 10^9bbls)', fontsize = 15, fontweight = 'bold')
plt.title('OPEC vs Non-OPEC Oil Reserves', fontsize = 20,  fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
#plt.savefig('/Users/pual Nwosu/Desktop/e1.png',  orientation = {'landscape'})
plt.show()

#Oil Production
fig, ax = plt.subplots(figsize = (14,10))
plt.plot(opd['Year'], opd['OPEC+'], 'k--')
plt.plot(opd['Year'], opd['OPEC+'], 'ks', markersize = 5, label = 'Estimated OPEC+')
plt.plot(opd['Year'], opd['OPEC'], 'r')
plt.plot(opd['Year'], opd['OPEC'], 'rH', markersize = 7, label = 'OPEC')
plt.plot(opd['Year'], opd['Non-OPEC'], 'y')
plt.plot(opd['Year'], opd['Non-OPEC'], 'yD', markersize = 7, label = 'Non-OPEC')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
plt.xticks(fontsize = 14, fontweight = 'bold')
plt.yticks(fontsize = 14, fontweight = 'bold')
plt.tick_params(labeltop = False, labelright = True)                                 
plt.grid(which = 'major', axis = 'y')
plt.legend(loc = 'upper left', markerfirst = True, fancybox = True)
plt.text(1965, 53000, 'OPEC+ total production: {}mbbls/day, {}%'.format(round(opd['OPEC+'].iloc[-1],2), round((opd['OPEC+'].iloc[-1]/opd['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1965, 51000, 'OPEC total production: {}mbbls/day, {}%'.format(round(opd['OPEC'].iloc[-1],2), round((opd['OPEC'].iloc[-1]/opd['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1965, 48000, 'Non-OPEC total production: {}mbbls/day, {}%'.format(round(opd['Non-OPEC'].iloc[-1],2), round((opd['Non-OPEC'].iloc[-1]/opd['Total World'].iloc[-1])*100),2), fontsize = 14, fontweight = 'bold')
plt.text(1977, 55000, 'World total production: {}mbbls/day'.format(round(opd['Total World'].iloc[-1],2)), fontsize = 14, fontweight = 'bold')
plt.text(1965, 45000, '(mbbls == 1000bbls)', fontsize = 15, fontweight = 'bold')
plt.title('OPEC vs Non-OPEC Oil Production', fontsize = 20,  fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()


colors = ('yellow', 'red')
explode = (0.1,0.1)
ls1 = [opd['OPEC'].iloc[-1], opd['Non-OPEC'].iloc[-1]]
ls2 = [res['OPEC'].iloc[-1], res['Non-OPEC'].iloc[-1]]
lab1 = ['OPEC', 'Non-OPEC']
wp = {'linewidth' : 1, 'edgecolor' : 'black'}

#Pie chart of Oil Production
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return '{:.1f}%'.format(pct, absolute)

fig, ax = plt.subplots(figsize =(10,7))
wedges, texts, autotexts = ax.pie(ls1, autopct = lambda pct: func(pct, ls1),
                                  labels = lab1, shadow = False, explode = explode,
                                  colors = colors, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab1, title = 'Legends', loc = 'center left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('World Oil Production', fontsize = 18, weight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()

#Pie chart of Oil Reserves
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return '{:.1f}%'.format(pct, absolute)

fig, ax = plt.subplots(figsize =(10,7))
wedges, texts, autotexts = ax.pie(ls2, autopct = lambda pct: func(pct, ls2),
                                  labels = lab1, shadow = False, explode = explode,
                                  colors = colors, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab1, title = 'Legends', loc = 'center left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('World Oil Reserves', fontsize = 18, weight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()

#Top 10 producing countries
opo1 = opo[['Country', 2019]].sort_values(by = 2019, ascending = True)
opo1 = opo1[-(opo1[2019].isna())]
opo1 = opo1.set_index('Country')
px = opo1.tail(15)
px.columns = ['PRODUCTION']
ax = px.plot(kind = 'barh', figsize = (16,10), color = 'red')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.xticks(fontsize = 15, fontweight = 'bold')
plt.yticks(fontsize = 15, fontweight = 'bold')
#plt.title('Highest Oil Producing Countries', fontsize = 15, fontweight = 'bold')
plt.ylabel('')
for i, v in enumerate(px['PRODUCTION']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TWP)*100, 2))), fontsize = 15)
plt.title('2019 Top 15 Oil Producing Nations', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()


#Top 10 Oil Reserves holders
rsv1 = rsv[['Country', 2019]].sort_values(by = 2019, ascending = True)
rsv1 = rsv1[-(rsv1[2019].isna())]
rsv1 = rsv1.set_index('Country')
rx = rsv1.tail(15)
rx.columns = ['RESERVES']
ax = rx.plot(kind = 'barh', figsize = (16,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.xticks(fontsize = 15, fontweight = 'bold')
plt.yticks(fontsize = 15, fontweight = 'bold')
plt.ylabel('')
#plt.title('Highest World Reserves', fontsize = 15, fontweight = 'bold')
for i, v in enumerate(rx['RESERVES']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TWR)*100, 2))), fontsize = 15)
plt.title('Top 15 Oil Reserves Holders', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()




#Increase in US Shale Production
fig, ax = plt.subplots(figsize = (14,10))
plt.plot(vop['Year'], vop['US'], 'k')
plt.plot(vop['Year'], vop['US'], 'ko', markersize = 7)
plt.plot(vop['Year'][23:32], vop['US'][23:32], 'y')
plt.plot(vop['Year'][23:32], vop['US'][23:32], 'yo', markersize = 7, label = 'Shale oil Boom')
plt.plot(vop['Year'][31:], vop['US'][31:], 'g')
plt.plot(vop['Year'][31:], vop['US'][31:], 'go', markersize = 7, label = 'Advancement in Shale oil production')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
plt.xticks(fontsize = 15, fontweight = 'bold')
plt.yticks(fontsize = 15, fontweight = 'bold')
plt.tick_params(labeltop = False, labelright = True)                                 
plt.grid(which = 'major', axis = 'y')
plt.legend(fontsize = 15)
plt.text(1985, 15000, '2019 US oil production: {}mbbls/day, {}%'.format(round(vop['US'].iloc[-1],2), round((vop['US'].iloc[-1]/opd['Total World'].iloc[-1])*100),2), fontsize = 11, fontweight = 'bold')
plt.text(1985, 14500, '2008 US oil production: {}mbbls/day, {}%'.format(round(vop['US'].iloc[23],2), round((vop['US'].iloc[23]/opd['Total World'].iloc[-1])*100),2), fontsize = 11, fontweight = 'bold')
plt.title('Rise of US Shale Oil Production', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()


lb = ['OPEC', 'Non-OPEC', 'OPEC+', 'US', 'Saudi Arabia', 'Russia', 'Canada']
lb2 = ['OPEC', 'Non-OPEC', 'US', 'Saudi Arabia', 'Russia', 'Canada']
v1 = [37.4, 62.6, 56, 17.9, 12.4, 12.1, 5.9] #2019 production shares
v2 = [0.5 ,2 ,8.5, 1.4, 1.4, 5.1]

c1 = dict(zip(lb, v1))
c2 = dict(zip(lb2, v2))
color1 = ['gold', 'blue', 'brown', 'green', 'violet', 'cyan', 'purple']
color2 = ['gold', 'blue', 'green', 'violet', 'cyan', 'purple']


#OIL Market shares
fig, ax = plt.subplots(figsize = (14,10))
ax.bar(lb, v1, width = 0.5, color = color1)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper left', fontsize = 10)
plt.grid(which = 'major', axis = 'y')
plt.xticks(lb, rotation = 45, fontsize = 15, fontweight = 'bold')
plt.title('Oil Market Shares in terms of Oil Production', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
for i, v in c1.items():
    if v < 6:
        ax.text(i, v+1, str('{}%'.format(v)), fontsize = 12, fontweight = 'bold', rotation = 10)
    elif v > 6 and v < 10:
        ax.text(i, v+5, str('{}%'.format(v)), fontsize = 12, fontweight = 'bold', rotation = 10)
    else:
        ax.text(i, v+1, str('{}%'.format(v)), fontsize = 12, fontweight = 'bold', rotation = 10)
plt.text('US', 42, 'OPEC shares already includes Saudi Arabia shares\nOPEC+ shares include OPEC shares and Saudi Arabia\nNon-OPEC shares include US, Russia and Canada', fontsize = 13, fontweight = 'bold')
plt.show()

#oil shares growth in the past ten years
fig, ax = plt.subplots(figsize = (20,14))
ax.bar(lb2, v2, width = 0.5, color = color1)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper left', fontsize = 10)
plt.grid(which = 'major', axis = 'y')
plt.xticks(lb2, rotation = 45, fontsize = 15, fontweight = 'bold')
plt.title('Ten Years(2009 - 2019) Oil production growth', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
for i, v in c2.items():
    ax.text(i, v, str('{}%'.format(v)), fontsize = 12, fontweight = 'bold', rotation = 10)
plt.text('Saudi Arabia', 6.3, 'North America Countries like US and Canada\nhave the highest increase in Oil Production due\nto the Shale revolution', fontsize = 12, fontweight = 'bold')
plt.show()


#Top oil importers
imp1 = imp[['Country', 2019]].sort_values(by = 2019, ascending = True)
imp1 = imp1.set_index('Country')
rx = imp1.tail(5)
rx.columns = ['IMPORTS']
ax = rx.plot(kind = 'barh', width = 0.5,  figsize = (20,14), color = 'gold')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.xticks(fontsize = 20, fontweight  = 'bold')
plt.yticks(fontsize = 20, fontweight  = 'bold')
plt.title('TOP OIL IMPORTERS', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
for i, v in enumerate(rx['IMPORTS']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TOE)*100, 2))), fontsize = 15)    
plt.show()


#Top oil exporters
exp1 = exp[['Country', 2019]].sort_values(by = 2019, ascending = True)
exp1 = exp1[-(exp1[2019].isna())]
exp1 = exp1.set_index('Country')
rx = exp1.tail(11)
rx.columns = ['EXPORTS']
ax = rx.plot(kind = 'barh', width = 0.5,  figsize = (30,14), color = 'blue')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.yticks(fontsize = 13, rotation = 45)
plt.ylabel('')
plt.xticks(fontsize = 20, fontweight  = 'bold')
plt.yticks(fontsize = 20, fontweight  = 'bold')
plt.title('TOP OIL EXPORTERS', fontsize = 20, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
for i, v in enumerate(rx['EXPORTS']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TOE)*100, 2))), fontsize = 15)
plt.show()




lx = [i for i in exp2['Year']]
ex = [i for i in exp2['US']]
im = [i for i in imp2['US']]



x = np.arange(0, len(lx))
w = 0.3
y = x+w
cs1 = dict(zip(x, ex))
cs2 = dict(zip(y, im))



fig = plt.figure(figsize = (30,14))
ax = fig.add_subplot(1,1,1)
#ax.ylim(0, 16000)
#ax.yaxis([])
p1 = ax.bar(x, ex, width = w, color = 'g')
p2 = ax.bar(x+w, im, width = w, color = 'y')
plt.xticks(x+w, lx, fontsize = 12, fontweight = 'bold',  rotation = 'vertical')
ax.plot(x, ex, 'r--')
ax.plot(x+w, im, 'k--')
ax.legend((p1[0], p2[1]), ('Exports in (mbbls))', 'Imports in (mbbls)'), loc = 'upper left', fontsize = 20)
for i, v in cs2.items():
    if v >= 12872:
        ax.text(i-0.1, v-1000, str('{}mbbls'.format(round(v))), rotation = 'vertical', fontsize = 13, fontweight = 'bold')
    else:
        ax.text(i-0.1, v+100, str('{}mbbls'.format(round(v))), rotation = 'vertical', fontsize = 13, fontweight = 'bold')   
for i, v in cs1.items():
    ax.text(i-0.1, v+100, str('{}mbbls'.format(round(v))), rotation = 'vertical', fontsize = 13, fontweight = 'bold')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
#ax.spines['top'].set_visible(False)  
#plt.legend(loc = 'upper right', fontsize = 15)
plt.grid(which = 'major', axis = 'y')
plt.xticks(fontsize = 20, fontweight  = 'bold')
plt.yticks(fontsize = 20, fontweight  = 'bold')
#plt.text(1985, 11000, 'US Oil Imports have decreased by -3%\nsince the development of the Shale Industry', fontsize = 15, fontweight = 'bold')
#plt.text(1985, 11500, 'US Oil Exports have increased by 14%\nsince the development of the Shale Industry', fontsize = 15, fontweight = 'bold')
plt.title('US Oil Imports and Oil Exports(1980 - 2019)', fontsize = 25, fontweight = 'bold')
plt.title('Source:BP Statistical Review 2020', fontsize = 10, loc = 'right')
plt.show()




