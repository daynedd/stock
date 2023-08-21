#alogrithm 
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import scipy as sci
from utt import peak
from utt import raw_data
import dyml as dl
plt.style.use('./deeplearning.mplstyle')

####################################################################################################################################################
comp = filedialog.askdirectory()
comp_1 = filedialog.askopenfilename()
data_1 = np.loadtxt(comp_1,
                 delimiter=",", dtype=str)
####################################################################################################################################################

price_1 = np.asarray(data_1[1:,4], dtype=float)
time = np.asarray(data_1[1:,0], dtype='datetime64[s]')



x_train = np.arange(0,len(price_1))

w_init = 0
b_init = 0
# some gradient descent settings
iterations = 100000
tmp_alpha = 7.0e-6
# run gradient descent
w_final, b_final, J_hist, p_hist = dl.gradient_descent(price_1,x_train, w_init, b_init, tmp_alpha, 
                                                    iterations, dl.compute_cost, dl.compute_gradient)
#print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")

z= w_final*x_train+b_final

plt.plot(x_train,price_1)
plt.plot(x_train,z)
plt.title('Bili')
plt.xlabel("date")
plt.xticks(rotation=90)
plt.ylabel('Price(USD)')
plt.show()

'''
key1=peak(price_1)
lensee1 = time[key1 [0]:key1[1]+1]

plt.plot(lensee1,price_1[key1[0]:key1[1]+1],label="VIX: S&P 500")
plt.xticks(rotation = 45)
plt.xlabel("days")
plt.ylabel('Price(USD)')
plt.legend()
plt.grid('on')

plt.show()'''
