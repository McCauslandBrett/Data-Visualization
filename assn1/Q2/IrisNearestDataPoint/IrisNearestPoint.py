# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def NearestDist(data,p):
    #get the number of columns
    numcol=len(data)
    #matrix = pd.DataFrame(np.zeros((numcol,numcol)))
    min_dist = 100000000000000000000
    for i in range (numcol):
     for j in range(i+1,numcol):
        x=data.iloc[i,0:3].values
        y=data.iloc[j,0:3].values
        d = minkowskiDist(x,y,p)
        if(d < min_dist):
            min_p1 = i
            min_p2 = j
            min_dist = d
        
    
    return min_p1,min_p2


def minkowskiDist(x,y,p):
  sum=0
  count=len(x)
  for i in range(count):
    sum = sum + pow((abs(x[i]-y[i])),p)
  fp= 1/p
  return pow(sum,fp)
  

#-----------  ----------
# 
   #import the data set
data=pd.read_csv('IrisDataSet.csv')
p1,p2 = NearestDist(data,1)
print('for a p value of 1 Nearest points are, p1:',p1,' and p2:',p2 )
p1,p2 = NearestDist(data,2)
print('for a p value of 2 Nearest points are, p1:',p1,' and p2:',p2 )


















