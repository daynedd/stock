import pandas as pd 
data = pd.read_csv("BILI.csv")


data = data.drop('Adj Close',axis = 1)
print(data.head())
close_price= data['Close']
date= data['Date']
i=1
value=[]
for i in range(len(date)):
    value.append((date[i],close_price[i]))

print(data['Close'][1])