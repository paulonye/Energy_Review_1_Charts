# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 03:06:18 2020

@author: hP
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

pec = pd.read_excel('edata.xlsx', sheet_name = 'CO21')
ems = pd.read_excel('interndata.xlsx', sheet_name = 'envsem')
ems = ems.dropna(how = 'any', axis = 0)
cco2 = pd.read_excel('edata.xlsx', sheet_name = 'CCO2')
coal = pd.read_excel('edata.xlsx', sheet_name = 'coal_c')
oilc = pd.read_excel('edata.xlsx', sheet_name = 'oil_c')
gasc = pd.read_excel('edata.xlsx', sheet_name = 'gas_c')
renc = pd.read_excel('edata.xlsx', sheet_name = 'ren_c')
tpec = pd.read_excel('edata.xlsx', sheet_name = 'pec')
nuc = pd.read_excel('edata.xlsx', sheet_name = 'nuc_c')
hyc = pd.read_excel('edata.xlsx', sheet_name = 'hydro_c')
soc = pd.read_excel('edata.xlsx', sheet_name = 'sol_c')
wec = pd.read_excel('edata.xlsx', sheet_name = 'win_c')
est = pd.read_excel('edata.xlsx', sheet_name = 'est_co2')
bio = pd.read_excel('edata.xlsx', sheet_name = 'bio_c')


oren = pec.iloc[45:,:]
oren = oren[['Year', 
       'Coal_C(exj)', 'Renw(exj)', 'Hydro(exj)', 'Oil_C(exj)', 'Gas_C(exj)',
       'Nuclear_C(exj)']]



TCE = pec['C02(mt)'].iloc[-1]
TCOAL = pec['Coal_C(exj)'].iloc[-1]
TOIL = 98272 #Thousand barrels 
TGAS = pec['Gas_C(exj)'].iloc[-1]
TREN = pec['Renw(exj)'].iloc[-1]
TPEC = pec['PEC(exj)'].iloc[-1]
THYD = pec['Hydro(exj)'].iloc[-1]
TNUC = pec['Nuclear_C(exj)'].iloc[-1]
TSE = 6.45 #exjoules
TWE = 12.74 #exjoules
TBE = 3967


eml1 = [ems['Coal_Emissions'].iloc[-1], ems['Oil_Emissions'].iloc[-1], ems['Gas_Emissions'].iloc[-1]]
eml2 = [pec.iloc[-1].values[5:]]
ape =  [116.58, 28.61, 83.82, 38.68, 38.78, 19.87, 257.56]
ape2 = [5975.9, 1254.9, 4110.8, 2085.3, 2164.1, 1308.5, 17269.5]

oren11 = [0.8, 13.7, 1.9, 1.1, 2.5, -0.7]
oren1 = [0.8, 0, 0, 0, 0, 0]
oren2 = [0, 13.7, 0, 0, 0, 0]
oren3 = [0, 0, 1.9, 0, 0, 0]
oren4 = [0, 0, 0, 1.1, 0, 0]
oren5 = [0, 0, 0, 0, 2.5, 0]
oren6 = [0, 0, 0, 0, 0, -0.7]

afc = [6.70, 2.73, 8.18, 0.03 , 0.12, 0.41, 10.81]
afc1 = [6.70, 0, 0, 0, 0, 0, 0]
afc2 = [0, 2.73, 0, 0, 0, 0, 0]
afc3 = [0, 0, 8.18, 0, 0, 0, 0]
afc4 = [0, 0, 0, 0.03, 0, 0, 0]
afc5 = [0, 0, 0, 0, 0.12, 0, 0]
afc6 = [0, 0, 0, 0, 0, 0.41, 0]
afc7 = [0, 0, 0, 0, 0, 0, 10.81]

eg = [5425.7, 1329.3, 3993.3, 1431.0, 1264.7, 870.1, 12690.5]
eg1= [5425.7, 0, 0, 0, 0, 0, 0]
eg2 =[0, 1329.3, 0, 0, 0, 0, 0]
eg3= [0, 0, 3999.3, 0, 0, 0, 0]
eg4= [0, 0, 0, 1431.0, 0, 0, 0]
eg5= [0, 0, 0, 0, 1264.7, 0, 0]
eg6= [0, 0, 0, 0, 0, 870.1, 0]
eg7= [0, 0, 0, 0, 0, 0, 12690.5]








#oren3 = [1.6, 15.5, , ,2.4,   ]
lab2 = [col for col in pec.columns[5:]]
lab1 = ['Coal Emissions', 'Oil Emissions', 'Gas Emissions']
lab3 = ['North America', 'S&Cent America', 'Europe', 'CIS', 'Middle East', 'Africa', 'Asia Pacific']



explode = (0.1,0.1,0.1)
explode2 = (0.1,0.0,0.0,0.1,0.1,0.1)
explode3 = (0.0,0.0,0.0,0.0,0.0,0.3,0.0)

wp = {'linewidth' : 1, 'edgecolor' : 'black'}

color1 = ('red', 'brown', 'blue')

#def tt(x, y):
#    for i, v in enumerate(zip(x, y)):
#        return i
#tt(lab2, eml2)


color2 = ('brown', 'green', 'blue', 'yellow', 'grey', 'red' )
color3 = ('brown', 'green', 'blue', 'yellow', 'grey', 'red', 'gold')


cast = dict(zip(lab2, oren11))
cast2 = dict(zip(lab3, afc))
cast3 = dict(zip(lab3, eg))

#Total Primary Energy
plt.rc('font', family = 'serif' )
fig, ax = plt.subplots(figsize = (10,7))
ax.stackplot(pec['Year'],  pec['Coal_C(exj)'], pec['Renw(exj)'], pec['Hydro(exj)'], pec['Oil_C(exj)'], pec['Gas_C(exj)'],
       pec['Nuclear_C(exj)'], labels = ('Coal = {}'.format(round(pec['Coal_C(exj)'].iloc[-1], 2)), 'Renewables = {}'.format(round(pec['Renw(exj)'].iloc[-1], 2)), 'Hydro = {}'.format(round(pec['Hydro(exj)'].iloc[-1], 2)), 'Oil = {}'.format(round(pec['Oil_C(exj)'].iloc[-1], 2)), 'Gas = {}'.format(round(pec['Gas_C(exj)'].iloc[-1], 2)), 'Nuclear = {}'.format(round(pec['Nuclear_C(exj)'].iloc[-1], 2))),colors = ('black', 'green', 'blue', 'brown', 'red', 'yellow'),  baseline = 'zero' )
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
ax.yaxis.tick_right()           
plt.grid(which = 'major', axis = 'y')
plt.text(1965, 410, 'Total Energy Consumption as of 2019: {}ExJoules'.format(round(pec['PEC(exj)'].iloc[-1], 2)), fontsize = 12)
plt.legend(loc = 'upper left', fontsize = 13, ncol = 2, title = '2019 Total Primary Energy in ExJoules by:', title_fontsize = 15)
plt.title('Increase in Primary Energy Shares over the past 50 Years', fontsize = 15, fontweight = 'bold')
plt.show()



#Total Primary Energy past 10 years
pec['Year2'] = pec['Year']
pec = pec.set_index(pec['Year2'])
plt.rc('font', family = 'serif' )
fig, ax = plt.subplots(figsize = (10,7))
ax.stackplot(pec['Year'].loc[2010:],  pec['Coal_C(exj)'].loc[2010:], pec['Renw(exj)'].loc[2010:], pec['Hydro(exj)'].loc[2010:], pec['Oil_C(exj)'].loc[2010:], pec['Gas_C(exj)'].loc[2010:],
       pec['Nuclear_C(exj)'].loc[2010:], labels = ('Coal = {}'.format(round(pec['Coal_C(exj)'].iloc[-1], 2)), 'Renewables = {}'.format(round(pec['Renw(exj)'].iloc[-1], 2)), 'Hydro = {}'.format(round(pec['Hydro(exj)'].iloc[-1], 2)), 'Oil = {}'.format(round(pec['Oil_C(exj)'].iloc[-1], 2)), 'Gas = {}'.format(round(pec['Gas_C(exj)'].iloc[-1], 2)), 'Nuclear = {}'.format(round(pec['Nuclear_C(exj)'].iloc[-1], 2))),colors = ('black', 'green', 'blue', 'brown', 'red', 'yellow'),  baseline = 'zero' )
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
ax.yaxis.tick_right()           
plt.grid(which = 'major', axis = 'y')
plt.text(2010, 410, 'Total Energy Consumption as of 2019: {}ExJoules'.format(round(pec['PEC(exj)'].iloc[-1], 2)), fontsize = 13)
plt.legend(loc = 'upper left', fontsize = 13, ncol = 2, title = '2019 Total Primary Energy in ExJoules by:', title_fontsize = 15)
plt.title('Increase in Primary Energy Shares over the last 10 Years', fontsize = 15, fontweight = 'bold')
plt.show()




#Carbon Emissions
fig, ax = plt.subplots(figsize = (10,7))
ax.stackplot(ems['year'],  ems['Coal_Emissions'], ems['Oil_Emissions'], ems['Gas_Emissions'],
       labels = ('Coal = {}'.format(round(ems['Coal_Emissions'].iloc[-1], 2)), 'Oil = {}'.format(round(ems['Oil_Emissions'].iloc[-1], 2)), 'Gas = {}'.format(round(ems['Gas_Emissions'].iloc[-1], 2))), colors = ('red', 'brown', 'blue'), baseline = 'zero' )
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
ax.yaxis.tick_right()           
plt.grid(which = 'major', axis = 'y')
plt.text(1970, 26010, 'Total CO2 Emissions as of 2019: {}mto of Co2'.format(int(round(pec['C02(mt)'].iloc[-1], 2))), fontsize = 12)
plt.text(1970, 24000, 'mto = million tonne', fontsize = 12)
plt.legend(loc = 'upper left', fontsize = 13, ncol = 2, title = '2019 Total CO2 Emissions in mto of Co2 by:', title_fontsize = 15)
plt.title('Increase in Co2 Emissions over the past 50 Years', fontsize = 15, fontweight = 'bold')
plt.show()


#Correlations between Carbon Emissions and Energy Consumption
fig, ax = plt.subplots(figsize = (10,7))
ax.scatter(ems['Emissions'], ems['TotalEnergy'], s = 100, edgecolors=(0, 0, 0))
ax.plot([ems['Emissions'].min(), ems['Emissions'].max()],[ems['TotalEnergy'].min(), ems['TotalEnergy'].max()], 'k--',lw=4)
plt.xlabel('Carbon Emissions in MTOE', fontsize = 15, fontweight = 'bold')
plt.ylabel('Total Energy Consumed in  MTOE', fontsize = 15, fontweight = 'bold')
ax.spines['right'].set_visible(False)                        
ax.spines['top'].set_visible(False)     
plt.grid(which = 'major', axis = 'y')        
plt.title('Correlation between Energy Consumption vs Carbon Emissions', fontsize = 15, fontweight = 'bold')
plt.show()

#Correlations between Carcon Emissions and Energy Consumption with Years
ax = ems.plot(kind="scatter", x="Emissions", y="TotalEnergy",
             alpha=0.8, s = 100, label="Emissions",
             figsize=(12,10),    c="year", cmap=plt.get_cmap("Reds"),
             colorbar=True,    sharex=False) 
plt.plot([ems['Emissions'].min(), ems['Emissions'].max()],[ems['TotalEnergy'].min(), ems['TotalEnergy'].max()], 'k--',lw=4)
plt.xlabel('Carbon Emissions in MTOE', fontsize = 15, fontweight = 'bold')
plt.ylabel('Total Energy Consumed in  MTOE', fontsize = 15, fontweight = 'bold')
ax.spines['right'].set_visible(False)                        
ax.spines['top'].set_visible(False)     
plt.grid(which = 'major', axis = 'y')        
plt.show()



#Pie Chart of Emissions
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return '{:.1f}%'.format(pct, absolute)

fig, ax = plt.subplots(figsize =(10,7))
wedges, texts, autotexts = ax.pie(eml1, autopct = lambda pct: func(pct, eml1),
                                  labels = lab1, shadow = False, explode = explode,
                                  colors = color1, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab1, title = 'Emissions by:', loc = 'center left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('Primary Energy Emissions', fontsize = 15, weight = 'bold')
plt.show()



#Pie charts of Total Primary Energy
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return '{:.1f}%'.format(pct, absolute)

fig, ax = plt.subplots(figsize =(12,9))
wedges, texts, autotexts = ax.pie(eml2, autopct = lambda pct: func(pct, eml2),
                                  labels = lab2, shadow = False, explode = explode2,
                                  colors = color2, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab2, fontsize = 15, title = 'Total Primary Consumption:', loc = 'center left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 13, weight = 'bold')
texts[0].set_fontsize(15)
ax.set_title('World Primary Energy Consumption', fontsize = 15, weight = 'bold')
plt.show()



#Top 10 Carbon Emissions
cco3 = cco2[['Country', '2019', 'G10', 'S2019']].sort_values(by = '2019', ascending = True)
cco3 = cco3[-(cco2['2019'].isna())]
cco3 = cco3.set_index('Country')
rx = cco3.tail(15)
rx1 = rx.drop(['G10', 'S2019'], axis = 1)
rx1.columns = ['Carbon Emissions']
ax = rx1.plot(kind = 'barh', figsize = (12,10), color = 'beige')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Highest Carbon Emitters', fontweight = 'bold')
for i, v in enumerate(rx1['Carbon Emissions']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TCE)*100, 2))))
plt.show()



#Top 15 coal consumers
coal2 = coal[['Country', 2019]].sort_values(by = 2019, ascending = True)
coal2 = coal2[-(coal[2019].isna())]
coal2 = coal2.set_index('Country')
rx = coal2.tail(15)
rx.columns = ['COAL']
ax = rx.plot(kind = 'barh', figsize = (8,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Coal Consumption', fontweight = 'bold')
for i, v in enumerate(rx['COAL']):
    ax.text(v + 3, i + 0.25, str('{}%'.format(round((v/TCOAL)*100, 2))))
plt.show()



#Top 15 Oil Consumers
oilc2 = oilc[['Country', 2019]].sort_values(by = 2019, ascending = True)
oilc2 = oilc2[-(oilc2[2019].isna())]
oilc2 = oilc2.set_index('Country')
rx = oilc2.tail(15)
rx.columns = ['OIL']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Oil Consumption', fontsize = 15, fontweight = 'bold')
for i, v in enumerate(rx['OIL']):
    ax.text(v + 5, i + 0.25, str('{}%'.format(round((v/TOIL)*100, 2))), fontsize = 13)
plt.show()



#Top 15 Gas Consumers
gasc2 = gasc[['Country', 2019]].sort_values(by = 2019, ascending = True)
gasc2 = gasc2[-(gasc2[2019].isna())]
gasc2 = gasc2.set_index('Country')
rx = gasc2.tail(15)
rx.columns = ['GAS']
ax = rx.plot(kind = 'barh', figsize = (8,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Gas Consumption', fontweight = 'bold')
for i, v in enumerate(rx['GAS']):
    ax.text(v + 1, i + 0.25, str('{}%'.format(round((v/TGAS)*100, 2))))
plt.show()


#Top 15 Renewable Consumers
renc2 = renc[['Country', 2019]].sort_values(by = 2019, ascending = True)
renc2 = renc2[-(renc2[2019].isna())]
renc2 = renc2.set_index('Country')
rx = renc2.tail(15)
rx.columns = ['RENEWABLES']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = 'green')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Renewables Consumption', fontweight = 'bold')
for i, v in enumerate(rx['RENEWABLES']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TREN)*100, 2))))
plt.show()



#Total Primary Energy Consumers
tpec2 = tpec[['Country', 2019]].sort_values(by = 2019, ascending = True)
tpec2 = tpec2[-(tpec2[2019].isna())]
tpec2 = tpec2.set_index('Country')
rx = tpec2.tail(15)
rx.columns = ['Primary Energy']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Energy Consumption', fontweight = 'bold')
for i, v in enumerate(rx['Primary Energy']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TPEC)*100, 2))))
plt.show()



#Top 15 Nuclear Energy Consumers
nuc2 = nuc[['Country', 2019]].sort_values(by = 2019, ascending = True)
nuc2 = nuc2[-(nuc2[2019].isna())]
nuc2 = nuc2.set_index('Country')
rx = nuc2.tail(15)
rx.columns = ['NUCLEAR']
ax = rx.plot(kind = 'barh', figsize = (8,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Nuclear Consumption', fontweight = 'bold')
for i, v in enumerate(rx['NUCLEAR']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TNUC)*100, 2))))
plt.show()



#Top 15 Hydro Energy Consumers
hyc2 = hyc[['Country', 2019]].sort_values(by = 2019, ascending = True)
hyc2 = hyc2[-(hyc2[2019].isna())]
hyc2 = hyc2.set_index('Country')
rx = hyc2.tail(15)
rx.columns = ['HYDRO']
ax = rx.plot(kind = 'barh', figsize = (8,10), color = '#86bf91')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Hydro Consumption', fontweight = 'bold')
for i, v in enumerate(rx['HYDRO']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/THYD)*100, 2))))
plt.show()



#Top 15 Solar Energy Consumers
soc2 = soc[['Country', 2019]].sort_values(by = 2019, ascending = True)
soc2 = soc2[-(soc2[2019].isna())]
soc2 = soc2.set_index('Country')
rx = soc2.tail(15)
rx.columns = ['SOLAR']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = 'gold')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Solar Energy Consumption', fontweight = 'bold')
for i, v in enumerate(rx['SOLAR']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TSE)*100, 2))))
plt.show()



#Top 15 Wind Consuming Nations
wec2 = wec[['Country', 2019]].sort_values(by = 2019, ascending = True)
wec2 = wec2[-(wec2[2019].isna())]
wec2 = wec2.set_index('Country')
rx = wec2.tail(15)
rx.columns = ['WIND']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = 'blue')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Wind Energy Consumption', fontweight = 'bold')
for i, v in enumerate(rx['WIND']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TWE)*100, 2))))
plt.show()



#Top 15 Biofuels Consuming Nations
bio2 = bio[['Country', 2019]].sort_values(by = 2019, ascending = True)
bio2 = bio2[-(bio2[2019].isna())]
bio2 = bio2.set_index('Country')
rx = bio2.tail(15)
rx.columns = ['BIOFUELS']
ax = rx.plot(kind = 'barh', figsize = (12,10), color = 'red')
ax.spines['right'].set_visible(False)             
ax.spines['top'].set_visible(False)             
ax.spines['left'].set_visible(False)             
ax.spines['bottom'].set_visible(False)
plt.grid(which = 'major', axis = 'y')
plt.ylabel('')
plt.title('Countries with Highest Biofuels Consumption', fontweight = 'bold')
for i, v in enumerate(rx['BIOFUELS']):
    ax.text(v+0.1, i + 0.25, str('{}%'.format(round((v/TBE)*100, 2))))
plt.show()




#Increase in the rise shares 
fig, ax = plt.subplots(figsize = (10,7))
plt.ylim(-1, 15)
ax.bar(lab2, oren1, color = 'black', label = 'Coal')
ax.bar(lab2, oren2, color = 'green', label = 'Renewables')
ax.bar(lab2, oren3, color = 'blue', label = 'Hydro')
ax.bar(lab2, oren4, color = 'brown', label = 'Oil')
ax.bar(lab2, oren5, color = 'red', label = 'Gas')
ax.bar(lab2, oren6, color = 'yellow', label = 'Nuclear')
#ax.plot([(lab2[0]-3),(lab2[-1]+5)], [0,0], 'k--', lw = 3)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper right', fontsize = 15)
plt.grid(which = 'major', axis = 'y')
plt.title('10 Years % increase in Primary Energy Shares', fontsize = 15, fontweight = 'bold')
for i, v in cast.items():
    ax.text(i, v+0.8, str('{}%'.format(v)), fontsize = 13, fontweight = 'bold')
plt.show()







#Estimated Co2 from Energy consumption scenarios
fig, ax = plt.subplots(figsize = (10,7))
plt.plot(est['Year'], est['ET'], 'k')
plt.plot(est['Year'], est['ET'], 'ks', markersize = 3, label = 'Evolving Transition')
plt.plot(est['Year'], est['ME'], 'r')
plt.plot(est['Year'], est['ME'], 'rH', markersize = 3, label = 'More Energy')
plt.plot(est['Year'], est['LG'], 'y')
plt.plot(est['Year'], est['LG'], 'yD', markersize = 3, label = 'Less Globalization')
plt.plot(est['Year'], est['RT'], 'g')
plt.plot(est['Year'], est['RT'], 'go', markersize = 3, label = 'Rapid Transition')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
ax.yaxis.tick_right()                        
plt.grid(which = 'major', axis = 'y')
plt.legend(loc = 'upper left', fontsize = 12, ncol = 2, title = 'Energy Scenarios:', title_fontsize = 13, markerfirst = True, fancybox = True)
plt.text(1965, 39000, 'Evolving Transition: A steady rise in the shares of Renewables',  fontsize = 11, fontweight = 'bold')
plt.text(1965, 35500, 'More Energy: More Energy is being consumed globally,\nthis can be marked by an increase in Global Economic growth', fontsize = 11, fontweight = 'bold')
plt.text(1965, 31000, 'Less Globalization: Lesser Energy is being consumed,\nthis can be marked by lower economic growth', fontsize = 11, fontweight = 'bold')
plt.text(1965, 27000, 'Rapid Transition: This scenario is marked \nby a sharp increase in Renewables shares',  fontsize = 11, fontweight = 'bold')
plt.title('Forecasted Co2 Emissions for different Energy Scenarios', fontsize = 15, fontweight = 'bold')
plt.show()



#African renewables Consumption
fig, ax = plt.subplots(figsize = (12,10))
ax.bar(lab3, afc1, width = 0.5, color = 'yellow', label = 'North America')
ax.bar(lab3, afc2, color = 'pink', label = 'South & Central America')
ax.bar(lab3, afc3, width = 0.5,  color = 'green', label = 'Europe')
ax.bar(lab3, afc4, color = 'red', label = 'CIS(Russia)')
ax.bar(lab3, afc5, color = 'red', label = 'Middle East')
ax.bar(lab3, afc6, color = 'red', label = 'Africa')
ax.bar(lab3, afc7, width = 0.5, color = 'green', label = 'Asia Pacific')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper left', ncol = 3, fontsize = 10)
plt.grid(which = 'major', axis = 'y')
plt.xticks(lab3, rotation = 45, fontsize = 12, fontweight = 'bold')
plt.title('Consumption of Renewable Energy by Continents', fontsize = 15, fontweight = 'bold')
for i, v in cast2.items():
    ax.text(i, v+0.2, str('{}exJ'.format(v)), fontsize = 10, fontweight = 'bold')
plt.text(0, 9, 'Asia Pacific has the highest Renewables consumption, this includes countries\nlike China and india while Africa lags behind in the consumption of any \nform of renewable sources consuming just 0.41ExJoules', fontsize = 13)
plt.show()



#African Prmary Energy Consumption
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return '{:.1f}%'.format(pct, absolute)

fig, ax = plt.subplots(figsize =(10,7))
wedges, texts, autotexts = ax.pie(ape, autopct = lambda pct: func(pct, ape),
                                  labels = lab3, shadow = False, explode = explode3,
                                  colors = color3, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab3, title = 'Continents:', loc = 'lower left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('Primary Energy Consumption by Continents', fontsize = 15, weight = 'bold')
plt.show()





#Africa Carbon Emissions
fig, ax = plt.subplots(figsize =(10,7))
wedges, texts, autotexts = ax.pie(ape2, autopct = lambda pct: func(pct, ape2),
                                  labels = lab3, shadow = False, explode = explode3,
                                  colors = color3, startangle = 90, wedgeprops = wp,
                                  textprops = dict(color = 'black'))
ax.legend(wedges, lab3, title = 'Continents:', loc = 'lower left', bbox_to_anchor = (1,0,0.5,1))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('Co2 Emissions by Continents', fontsize = 15, weight = 'bold')
plt.show()




#Afica Electricity Generation
fig, ax = plt.subplots(figsize = (12,10))
ax.bar(lab3, eg1, width = 0.5, color = 'yellow', label = 'North America')
ax.bar(lab3, eg2, color = 'pink', label = 'South & Central America')
ax.bar(lab3, eg3, width = 0.5,  color = 'green', label = 'Europe')
ax.bar(lab3, eg4, color = 'red', label = 'CIS(Russia)')
ax.bar(lab3, eg5, color = 'red', label = 'Middle East')
ax.bar(lab3, eg6, color = 'red', label = 'Africa')
ax.bar(lab3, eg7, width = 0.5, color = 'green', label = 'Asia Pacific')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)             
ax.spines['top'].set_visible(False)  
plt.legend(loc = 'upper left', ncol = 3, fontsize = 10)
plt.grid(which = 'major', axis = 'y')
plt.xticks(lab3, rotation = 45, fontsize = 12, fontweight = 'bold')
plt.title('Electricity Generation by Continents', fontsize = 15, fontweight = 'bold')
for i, v in cast3.items():
    ax.text(i, v+100, str('{}exJ'.format(v)), fontsize = 10, fontweight = 'bold')
plt.text(0, 8700, 'Africa has the lowest Cummulative Electricity Generation recording a total of\n870exJoules, this comes as no suprise as most of the countries in Africa are\nstill very much underdeveloped', fontsize = 13)
plt.show()

