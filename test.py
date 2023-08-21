import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = pd.read_csv("BILI.csv")
print('Raw data from Yahoo Finance : ')
print(data.head())

data = data.drop('Date',axis=1) 
data = data.drop('Adj Close',axis = 1)
print('\n\nData after removing Date and Adj Close : ')


#Split into train and test data

data_X = data.loc[:,data.columns !=  'Close' ]
data_Y = data['Close']
train_X, test_X, train_y,test_y = train_test_split(data_X,data_Y,test_size=0.25)
''''
print('\n\nTraining Set')
print(train_X.head())
print(train_y.head())
'''

regressor = LinearRegression()
regressor.fit(train_X,train_y)
###

predict_y = regressor.predict(data_X)
print('Prediction Score : ' , regressor.score(test_X,test_y))

'''
error = mean_squared_error(test_y,predict_y)
print('Mean Squared Error : ',error)
'''

#Plot the predicted and the expected values

z= np.arange(0,len(data_X))


fig = plt.figure()
ax = plt.axes()
ax.grid()
ax.set(xlabel='dates',ylabel='Close ($)', title='Bilibili Stock Prediction using Linear Regression')
ax.plot(z,data_Y)
ax.plot(z,predict_y)
fig.savefig('LRPlot.png')
plt.show()