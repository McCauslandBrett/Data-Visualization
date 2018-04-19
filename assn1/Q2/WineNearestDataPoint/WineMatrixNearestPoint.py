# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#precondition: data is the entire table data set,classes[],classranges[]
#postcondition: variables contain; classes(class column)
#classranges (beginning and ending of where  class rows end)
def GatherClassRanges(data,classes,classranges):
 classes = data.iloc[:,4].values
 length = data.iloc[:,4].size
 classranges.append(0)
 flowertype=classes[0]

 for count in range(length):
  if(flowertype!=classes[count]):
    classranges.append(count)
    flowertype=classes[count]
 classranges.append(length)
 return

def GenerateDataMatrix(data,p):
  #seperate the rows to there distinct class
  classes = data.iloc[:,4].values 
  classranges=[]
  GatherClassRanges(data,classes,classranges)


  for i in range (1,numcol):
    for j in range(i+1,numcol):
     x=data.iloc[i,0:3].values
     y=data.iloc[j,0:3].values
     matrix[i][j] = minkowskiDist(x,y,p)
     title='p='+str(p)+'Data x Data distance Matrix'
  print(matrix)
  PlotDistMatrix(matrix,headers,title)
  return matrix

def PlotDistMatrix(matrix,headers,title):
 mask = np.zeros_like(matrix)
 mask[np.triu_indices_from(mask)] = True

 with sns.axes_style("white"):
  plt.figure()
  plot = sns.heatmap(matrix,mask=mask,cmap="YlGnBu")
  plot.set_title(title)
  plt.savefig(title)
  
  return
def NearestPos(matrix,numcol,i,j):
  for k in range(numcol):
   for e in range(numcol):
      d = (matrix[i]-x(j))^2+(y(i)-y(j))^2;
      if (d < min_dist and !(i == k and e ==j) ):
        min_p1 = p1
        min_p2 = p2
        min_dist = d
 return min_p1,min_p2,min_dist

def NearestDist(data,p):
  numcol=len(data)
  matrix = GenerateDataMatrix(data,p)
  min_dist = 100000000000000000000
  for i in range(numcol):
   for j in range(numcol):
     p1,p2,d = NearestPos(matrix,numcol,i,j)
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
data=pd.read_csv('Wine.csv')
GenerateDataMatrix(data,1)
GenerateDataMatrix(data,2)


















