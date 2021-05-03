#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:32:02 2021

@author: tawaneiei
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titanic = pd.read_csv('titanic.csv')
data = titanic[['Fare', 'Age', 'Sex']].copy()
# data.loc[data['Sex']=='male', 'Sex'] = 'Green'