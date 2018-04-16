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

def GenerateAllDatanMatrix(data,p):
  #seperate the rows to there distinct class
  classes = data.iloc[:,4].values 
  classranges=[]
  GatherClassRanges(data,classes,classranges)
  
  #Get the Atribute names excluding class name 
  headers=list(data)
  headers.pop()
  
  #get the number of columns
  numcol=len(headers)
  
  #get the number of distinct classes
  numRowranges=(len(classranges)-1)
 
 #for every class of flower
  for k in range(numRowranges):
   #generate a matrix initialized to zero
   dist_matrix = pd.DataFrame(np.zeros((numcol,numcol)))
   for i in range (numcol):
    for j in range(i+1,numcol):
     x=data.iloc[classranges[k]:classranges[k+1],i].values
     y=data.iloc[classranges[k]:classranges[k+1],j].values
     dist_matrix[i][j] = minkowskiDist(x,y,p)
     title='Data x Data distance Matrix of '+ classes[classranges[k]]
   PlotDistMatrix(dist_matrix,headers,title)
  return dist_matrix

def PlotDistMatrix(dist_matrix,headers,title):
 mask = np.zeros_like(dist_matrix)
 mask[np.triu_indices_from(mask)] = True

 with sns.axes_style("white"):
  plt.figure()
  plot = sns.heatmap(dist_matrix,mask=mask, vmin = 0, vmax = 200, 
  square = True,annot=True,cmap=sns.diverging_palette(220,10, as_cmap = True))
  plot.set_xticklabels(labels = headers, rotation=20)
  plot.set_yticklabels(labels = headers, rotation=20)
  plot.set_title(title)
  #plt.savefig(title)
  
  return

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
GenerateAllDatanMatrix(data,1)



















