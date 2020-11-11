# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
plt.rc('font', family = 'serif' )


price = [0.08, 0.153, 0.2, 0.395, 0.42, 0.6, 0.7, 5, 3.25, 15, 11, 25, 20, 30, 22, 26, 65, 145, 97, 87, 145, 143] 
year = [1970, 1978, 1982, 1986, 1988, 1989, 1990, 1993, 1993.5, 1994, 1994.5, 1998, 1999, 2000, 2000.5, 2002, 2007, 2012, 2012.5, 2015, 2016, 2019]
events = ['', 'Military Regime by Obasanjo', 'Fall in Oil price', 'Fiscal Crisis', '',  '', 'Babangida Regime', 'Derugation of the price of fuel', 'Subsidy Protest', 'Spike', 'More Protests', 'General Abdulsalami Abubakar', 'Protest', 'Obasanjo Civilian Governement Begins', 'Protest', '', 'Yar\'Adua Administration', 'Goodluck Administration tries to deregulate', 'Mass Protests', '', 'Increase by Buhari Administration', ''] 

price1 = [0.08, 0.153, 0.2, 0.395, 0.42, 0.6, 0.7, 5, 3.25, 15, 11, 25, 20]
year1 = [1970, 1978, 1982, 1986, 1988, 1989, 1990, 1993, 1993.5, 1994, 1994.5, 1998, 1999]
events1 = ['', 'Military Regime by Obasanjo', 'Fall in Oil price', 'Fiscal Crisis', '',  '', 'Babangida\nRegime', 'Derugation of the price of fuel', 'Subsidy Protest', 'Spike', 'More Protests', 'General Abdulsalami\nAbubakar Regime', 'Protest']

price2 = [30, 22, 26, 65, 145, 97, 87, 145, 143]
year2 = [2000, 2000.5, 2002, 2007, 2012, 2012.5, 2015, 2016, 2019]
events2 = ['Obasanjo Civilian Governement Begins', 'Protest', '', 'Yar\'Adua Administration', 'Goodluck Administration tries to deregulate', 'Mass Protests', '', 'Increase by Buhari Administration', '']

#Military Rule
fig, ax = plt.subplots(figsize = (20,10))
ax.axis([1968, 2000, -5, 60])
ax.plot(year1, price1, 'bo', markersize = 8)
ax.plot(year1, price1, 'b')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)   
plt.ylabel('Price in N/litre', fontsize = 12, fontweight = 'bold')                          
plt.grid(which = 'major', axis = 'y')
plt.title('Spike in Fuel Pump Prices during the Military Regime (1970 - 1999)', fontsize = 15, fontweight = 'bold')
for i, v, m in list(zip(year1, price1, events1)):
    ax.text(i, v+1, m, rotation = 25, fontsize = 11, fontweight = 'bold', withdash = True, bbox = dict(facecolor = 'red', alpha = 0.5))
plt.show()    


#Civilian Rule
fig, ax = plt.subplots(figsize = (20,10))
ax.axis([1998, 2020, 0, 200])
ax.plot(year2, price2, 'rs', markersize = 8)
ax.plot(year2, price2, 'r')
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
#plt.yticks(price2)
plt.tick_params(labeltop = False, labelright = True)   
plt.ylabel('Price in N/litre', fontsize = 12, fontweight = 'bold')                          
plt.grid(which = 'major', axis = 'y')
plt.title('Spike in Fuel Pump Prices during the Fourth Repulblic (2000 - 2020)', fontsize = 15, fontweight = 'bold')
for i, v, m in list(zip(year2, price2, events2)):
    ax.text(i, v+3, m, rotation = 25, fontsize = 11, fontweight = 'bold', withdash = True, bbox = dict(facecolor = 'blue', alpha = 0.5))
plt.show()

