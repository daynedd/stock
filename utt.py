
import numpy as np
import matplotlib.pyplot as plt

def peak(list):
    '''

    Parameters
    ----------
    list : list
    DESCRIPTION: raw data of price
    
    inl: increasing days
    days: collection of continue increasing days
    
    Returns
    start :the day start to increase
    end :the day stop to increase
    -------
    None.

    '''
    inl = []

    
###############################################################################  
    for i in range(len(list)):
        if list[i]-list[i-1]>0:
            inl.append(i)
            
            i +=1
            
        else:
            i+=1
            
###############################################################################
    j = 1
    a = 1 
    days=[]
    
    while j < len(inl):
        if inl[j] - inl[j-1] ==1 :
            days.append(a)
            a += 1
            j += 1
        else:
            days.append(a)
            a = 1
            j += 1
        
    
    start=inl[ days.index(max(days))-max(days)+1]-1
    end= inl[days.index(max(days))]
    return start,end

def raw_data(data_1):
    y1 = np.array(data_1[1:,4])
    x1 = np.array(data_1[1:,0], dtype='datetime64[s]')
    return x1,y1
    