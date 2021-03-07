from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor

import pandas as pd
import numpy as np

import pickle

## read the file

df=pd.read_csv('newdata1.csv')


## preprocess



df = df[['hour','month','holiday', 'weekday','Member type','count']]

df.columns = [ 'hour','month','holiday','weekday','Member_type','count']


df.holiday = df.holiday.astype('category')
df.weekday = df.weekday.astype('category')
df.month = df.month.astype('category')
df.Member_type = df.Member_type.astype('category')

df = pd.get_dummies(df)

## modelling

x = df.drop(columns = ['count'])
y = df['count']



ada = AdaBoostRegressor()
ada.fit(x,y)
pickle.dump(ada, open('model.pkl','wb'))
# line

