#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:47:57 2021

@author: tawaneiei
"""

import pandas as pd

titanic = pd.read_csv('titanic2.csv')
data = titanic[['Fare']]
# plot_data = {}
# for i in data.loc[:, 'Fare']:
#     fare = (i // 10)*10
#     if fare in plot_data.keys():
#         plot_data.update({fare: plot_data[fare]+1})
#     else:
#         plot_data.update({fare: 1})
# data = pd.DataFrame(data=[plot_data.keys(), plot_data.values()], index=['Fare', 'Frequency']).T
#data = data.set_index('Fare')
# data = data.sort_index()
ax = data.plot.hist(bins=100)
ax.set_xlim(0, 600)
ax.set_ylim(0, 350)

x = set()
x.