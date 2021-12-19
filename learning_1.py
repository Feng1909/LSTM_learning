import paddle
import paddle.fluid as fluid
import paddle.fluid.layers as layers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('dataset.csv')
# data.info()
# print([data['pm2.5'].isna()])
data = data.iloc[24:].copy()
data.fillna(method='ffill', inplace=True)
data.drop('No', axis=1, inplace=True)

data['time'] = data.apply(lambda x: datetime.datetime(year=x['year'],
                                                      month=x['month'],
                                                      day=x['day'],
                                                      hour=x['hour']),
                          axis=1)
data.set_index('time', inplace=True)
data.drop(columns=['year', 'month', 'day', 'hour'], inplace=True)
data.head()

data.columns = ['pm2.5', 'dew', 'temp', 'press', 'cbwd', 'iws', 'snow', 'rain']
data.cbwd.unique()
del data['cbwd']
data['pm2.5'][-1000:].plot()
data['temp'][-1000:].plot()