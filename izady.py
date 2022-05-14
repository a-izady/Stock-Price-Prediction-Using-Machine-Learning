import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
#%matplotlib inline
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
import math




dataset_total = pd.read_csv(r'C:\Files\EURUSD1440.csv', sep = ',')
dataset_total.head()



rows_need=500
#print('split-------------',rows_need)
total_size=len(dataset_total)
print('Total=',total_size)
tempd=dataset_total.tail(rows_need)
train_size=math.floor(0.77*rows_need)
Start_arr=total_size-rows_need
print('Start_arr=',Start_arr)
#dataset_train=tempd.head(train_size)
#dataset_test=tempd.tail(rows_need -train_size)
#dataset_train.to_csv('train.csv')
#dataset_test.to_csv('test.csv')


#dataset_train.head()
#print(dataset_train)
#tarining_set=dataset_train.iloc[:,2:3].values
#print('tarining_set')
#print(tarining_set)
#print(tarining_set.shape)

total_set=dataset_total.iloc[:,2:3].values
scaler = MinMaxScaler(feature_range=(0,1))

scaled_total_set = scaler.fit_transform(total_set)
print('scaled_training_set')
print(scaled_total_set)
#input("Press Enter to continue...izady")
x_train = []
y_train = []
x_test2 = []
for i in range(Start_arr+60,Start_arr+train_size):
    x_train.append(scaled_total_set[i-60:i,0])
    y_train.append(scaled_total_set[i,0])
for i in range(Start_arr,total_size):
    x_test2.append(scaled_total_set[i-60:i,0])
x_train=np.array(x_train)
y_train=np.array(y_train)
x_test2=np.array(x_test2)
print('x_train.shape')
print(x_train)
print(x_train.shape)
print('y_train.shape')
print(y_train)
print(y_train.shape)
#input("Press Enter to continue...izady")
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
x_test2=np.reshape(x_test2,(x_test2.shape[0],x_test2.shape[1],1))
print(x_train.shape)


print('start trining---------------------')
regressor = Sequential()
regressor.add(LSTM(units=50,return_sequences=True,input_shape = (x_train.shape[1],1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50,return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units=1))

regressor.compile(optimizer='adam',loss='mean_squared_error')
regressor.fit(x_train,y_train,epochs=100,batch_size=32)


actual_stock_price=tempd.iloc[:,2:3].values

#inputs=tempd.values

#inputs = inputs.reshape(-1,1)
#inputs=scaler.transform(inputs)

#x_test = []
#for i in range(60,rows_need):
#    x_test.append(inputs[i-60:i,0])

#x_test=np.array(x_test)
#x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
#print('x_test')
#print(x_test)
#input("Press Enter to continue...izady")
predict_stock_Price = regressor.predict(x_test2)
predict_stock_Price = scaler.inverse_transform(predict_stock_Price)




print('plot-------------------------------------')
plt.plot( actual_stock_price,color='red',label='Actual EURUSD')
plt.plot(predict_stock_Price,color='blue',label='Prdicted EURUSD')
plt.xlabel('Time')
plt.ylabel('EURUSD Price')
plt.legend()
plt.show()

