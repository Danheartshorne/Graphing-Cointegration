# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:19:06 2021

@author: danhe
"""

import numpy as np
import pandas as pd
#Data Source
import yfinance as yf
import os
#Data viz
import plotly.graph_objs as go


tick = ('BTC-GBP','ETH-GBP')
Data = yf.download(tickers=tick, period = '1y', interval = '1h')



Data = Data.fillna(method="ffill")
Data = Data.fillna(method="bfill")
Data = Data.iloc[:, 0:2] 
Data1 = Data.reset_index(level=0, inplace=True)

#Index
(Data.iloc[:,1]) = ((Data.iloc[:,1])/(Data.iat[0,1]))*100
(Data.iloc[:,2]) = ((Data.iloc[:,2])/(Data.iat[0,2]))*100

Data['Relative Value'] = (Data.iloc[:,1]) / (Data.iloc[:,2])


#log values
#(Data.iloc[:,3]) = np.log(Data.iloc[:,3])


y = Data['Relative Value']
x = Data['index']

fig = go.Figure()


fig = go.Figure(data=go.Scatter(x=x, y=y))


#Show
fig.write_html('first_figure.html', auto_open=True)