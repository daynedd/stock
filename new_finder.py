import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import scipy as sci
from utt import peak
from utt import raw_data
import dyml as dl
plt.style.use('./deeplearning.mplstyle')
from time import sleep
from tqdm import tqdm
import time as at

start = at.time()
####################################################################################################################################################
data_1 = np.loadtxt('BILI.csv',delimiter=",", dtype=str)
####################################################################################################################################################

price_1 = np.asarray(data_1[1:,4], dtype=float)
time = np.asarray(data_1[1:,0], dtype='datetime64[s]')

length = len(price_1)

map = np.zeros((length,length),dtype=float)

pbar = tqdm(range(length),bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
for i in range(length):
        for j in range(length):
            map[i,j]=-(price_1[i]-price_1[j])
            pbar.update(1)
pbar.close()
print(map)
buy_day = map.argmax(axis=1)
sell_day = map.argmax(axis=0)

print(price_1)
print("the best day to buy is:",time[buy_day][0])
print("the best day to sell is:",time[sell_day][0])
end = at.time()
print("The time of execution of above program is :",
      (end-start) , "s")