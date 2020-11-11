# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 06:34:45 2020

@author: Hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
sns.set_style('white')
plt.rc('font', family = 'serif' )

cop = pd.read_csv('COP.csv')
bp = pd.read_csv('BP.csv')
cvx = pd.read_csv('CVX.csv')
eni = pd.read_csv('E.csv')
she = pd.read_csv('RDS-B.csv')
tot = pd.read_csv('TOT.csv')
xom = pd.read_csv('XOM.csv')



lb = [2015, 2016, 2017, 2018, 2019, 2020]
v1 = [43, 70, 24, 28, 42, 23]
v2 = [39, 72, 52, 12, 21, 18]
#US OIL and gas shale bankruptcies
#sources: Haynes and Boone, LLP.,Insolvency insider


def month(x):
    if x == '12':
        return 'Dec'
    elif x == '01':
        return 'Jan'
    elif x == '02':
        return 'Feb'
    elif x == '03':
        return 'March'
    elif x == '04':
        return 'April'
    elif x == '05':
        return 'May'
    elif x == '06':
        return 'June'
    elif x == '07':
        return 'July'
    elif x == '08':
        return 'Aug'
    elif x == '09':
        return 'Sep'
    elif x == '10':
        return 'Oct'
    elif x == '11':
        return 'Nov'




cop['date2'] = cop['Date']
cop = cop.set_index(cop['date2'])
cop['monthno'] = cop['Date'].str.split('-', 2).str[1]
cop['month'] = cop['monthno'].apply(month)
cop['dayno'] = cop['Date'].str.split('-', 2).str[2]
cop['year'] = cop['Date'].str.split('-', 2).str[0]
cop['main'] = cop['month']+' '+cop['dayno']




 
    



bp['date2'] = bp['Date']
bp = bp.set_index(bp['date2'])
bp['monthno'] = bp['Date'].str.split('-', 2).str[1]
bp['month'] = bp['monthno'].apply(month)
bp['dayno'] = bp['Date'].str.split('-', 2).str[2]
bp['year'] = bp['Date'].str.split('-', 2).str[0]
bp['main'] = bp['month']+' '+bp['dayno']




cvx['date2'] = cvx['Date']
cvx = cvx.set_index(cvx['date2'])
cvx['monthno'] = cvx['Date'].str.split('-', 2).str[1]
cvx['month'] = cvx['monthno'].apply(month)
cvx['dayno'] = cvx['Date'].str.split('-', 2).str[2]
cvx['year'] = cvx['Date'].str.split('-', 2).str[0]
cvx['main'] = cvx['month']+' '+cvx['dayno']


she['date2'] = she['Date']
she = she.set_index(she['date2'])
she['monthno'] = she['Date'].str.split('-', 2).str[1]
she['month'] = she['monthno'].apply(month)
she['dayno'] = she['Date'].str.split('-', 2).str[2]
she['year'] = she['Date'].str.split('-', 2).str[0]
she['main'] = she['month']+' '+she['dayno']


eni['date2'] = eni['Date']
eni = eni.set_index(eni['date2'])
eni['monthno'] = eni['Date'].str.split('-', 2).str[1]
eni['month'] = eni['monthno'].apply(month)
eni['dayno'] = eni['Date'].str.split('-', 2).str[2]
eni['year'] = eni['Date'].str.split('-', 2).str[0]
eni['main'] = eni['month']+' '+eni['dayno']


tot['date2'] = tot['Date']
tot = tot.set_index(tot['date2'])
tot['monthno'] = tot['Date'].str.split('-', 2).str[1]
tot['month'] = tot['monthno'].apply(month)
tot['dayno'] = tot['Date'].str.split('-', 2).str[2]
tot['year'] = tot['Date'].str.split('-', 2).str[0]
tot['main'] = tot['month']+' '+tot['dayno']


xom['date2'] = xom['Date']
xom = xom.set_index(xom['date2'])
xom['monthno'] = xom['Date'].str.split('-', 2).str[1]
xom['month'] = xom['monthno'].apply(month)
xom['dayno'] = xom['Date'].str.split('-', 2).str[2]
xom['year'] = xom['Date'].str.split('-', 2).str[0]
xom['main'] = xom['month']+' '+xom['dayno']

#2ecc71, e74c3c, 34495e
#Conoco Phillips
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(cop['main'].loc['2020-01-01':], cop['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(cop['main'].loc['2020-01-01':], cop['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(cop['main'].loc['2020-03-01':'2020-05-01'], cop['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(cop['main'].loc['2020-03-01':'2020-05-01'], cop['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(cop['main'].loc['2020-05-01':], cop['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(cop['main'].loc['2020-05-01':], cop['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('ConocoPhillips\nNYSE: COP', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()


#BP
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(bp['main'].loc['2020-01-01':], bp['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(bp['main'].loc['2020-01-01':], bp['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(bp['main'].loc['2020-03-01':'2020-05-01'], bp['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(bp['main'].loc['2020-03-01':'2020-05-01'], bp['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(bp['main'].loc['2020-05-01':], bp['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(bp['main'].loc['2020-05-01':], bp['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('BP plc\nNYSE: BP', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()



#CVX
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,120)
plt.xlim(5,140)
ax.plot(cvx['main'].loc['2020-01-01':], cvx['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(cvx['main'].loc['2020-01-01':], cvx['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(cvx['main'].loc['2020-03-01':'2020-05-01'], cvx['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(cvx['main'].loc['2020-03-01':'2020-05-01'], cvx['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(cvx['main'].loc['2020-05-01':], cvx['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(cvx['main'].loc['2020-05-01':], cvx['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Chevron Corporation\nNYSE: BP', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()



#SHELL
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(she['main'].loc['2020-01-01':], she['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(she['main'].loc['2020-01-01':], she['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(she['main'].loc['2020-03-01':'2020-05-01'], she['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(she['main'].loc['2020-03-01':'2020-05-01'], she['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(she['main'].loc['2020-05-01':], she['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(she['main'].loc['2020-05-01':], she['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Royal Dutch Shell Plc\nAMS: RDSA', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()



#Total
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(tot['main'].loc['2020-01-01':], tot['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(tot['main'].loc['2020-01-01':], tot['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(tot['main'].loc['2020-03-01':'2020-05-01'], tot['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(tot['main'].loc['2020-03-01':'2020-05-01'], tot['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(tot['main'].loc['2020-05-01':], tot['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(tot['main'].loc['2020-05-01':], tot['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Total SE\nEPA: FP', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()


#Exxon
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(xom['main'].loc['2020-01-01':], xom['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(xom['main'].loc['2020-01-01':], xom['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(xom['main'].loc['2020-03-01':'2020-05-01'], xom['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(xom['main'].loc['2020-03-01':'2020-05-01'], xom['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(xom['main'].loc['2020-05-01':], xom['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(xom['main'].loc['2020-05-01':], xom['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('Exxon Mobil Corporation\nNYSE: XOM', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()

#ENI
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(15,80)
plt.xlim(5,140)
ax.plot(eni['main'].loc['2020-01-01':], eni['Close'].loc['2020-01-01':], 'r', lw = 2)
ax.fill_between(eni['main'].loc['2020-01-01':], eni['Close'].loc['2020-01-01':], color = 'red', alpha = 0.2)
ax.plot(xom['main'].loc['2020-03-01':'2020-05-01'], eni['Close'].loc['2020-03-01':'2020-05-01'], 'r', lw = 5, label = 'Effect of Coronavirus')
ax.fill_between(eni['main'].loc['2020-03-01':'2020-05-01'], eni['Close'].loc['2020-03-01':'2020-05-01'], color = 'red', alpha = 0.8)
ax.plot(eni['main'].loc['2020-05-01':], eni['Close'].loc['2020-05-01':], 'r', lw = 3)
ax.fill_between(eni['main'].loc['2020-05-01':], eni['Close'].loc['2020-05-01':], color = 'red', alpha = 0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('Price in USD', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, title = '2020 Significant events:', title_fontsize = 15, markerfirst = True, fancybox = True)
plt.title('E - ENI S.p.A.', fontsize = 25, fontweight = 'bold', loc = 'left')
plt.title('Source: YahooFinance.com', fontsize = 10, loc = 'right')
plt.show()


#US BANKRUPCIES hatch: {'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
fig, ax = plt.subplots(figsize = (18,12))
plt.ylim(0,80)
ax.plot(lb, v1, 'r', lw = 3)
ax.plot(lb, v1, 'wo', markersize = 10, markeredgecolor = 'red', markeredgewidth = 3, label = 'Oil and Gas Producer')
ax.plot(lb, v2, 'm', lw = 3)
ax.plot(lb, v2, 'wo', markersize = 10, markeredgecolor = 'magenta', markeredgewidth = 3, label = 'Oilfield Services')
ax.fill_between(lb, v1, color = 'red', alpha = 0.2, hatch = '.',in_layout = True)
ax.fill_between(lb, v2, color = 'magenta', alpha = 0.2, hatch = '.',in_layout = True)
for i,v in list(zip(lb, v1)):
    ax.text(i, v+3, str(v), fontsize = 15, fontweight = 'bold')
for i,v in list(zip(lb, v2)):
    ax.text(i, v-4, str(v), fontsize = 15, fontweight = 'bold')
plt.xticks(fontsize = 12, fontweight = 'bold')
plt.yticks(fontsize = 15)
ax.spines['right'].set_visible(False)                        
ax.spines['left'].set_visible(False)
#plt.tick_params(labeltop = False, labelright = True)                             
plt.grid(which = 'major', axis = 'y')
plt.ylabel('', fontsize = 12, fontweight = 'bold')
plt.legend(loc = 'upper right', fontsize = 14, markerfirst = True, fancybox = True)
plt.title('US OIL AND GAS BANKRUPTICES', fontsize = 20, fontweight = 'bold', loc = 'left')
plt.title('Source: Haynes and Boone, LLP.,Insolvency insider', fontsize = 10, loc = 'right')
plt.show()


