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
def Gatherclasses(data,classes,classranges):
 classes = data.iloc[:,0].values
 #print(classes)
 length = data.iloc[:,0].size
 classranges.append(0)
 classType =classes[0]

 for count in range(length):
  if(classType!=classes[count]):
    classranges.append(count)
    classType=classes[count]
 classranges.append(length)
 return

def GenerateAllCorrelationMatrix(data):
  #seperate the rows to there distinct class
  classes = data.iloc[:,0].values #good
  classranges=[]
  Gatherclasses(data,classes,classranges)
  
  #Get the Atribute names excluding class name 
  headers=list(data)
  headers.pop(0)
  print('HHHHHHHHHHEEEEEAAAADDDDDDERRRRRS')
  print(headers)
  #get the number of columns
  numcol=len(headers)
  
  #get the number of distinct classes
  numRowranges=(len(classranges)-1)
 
 #for every class of class
  for k in range(len(classranges)-1):
   #generate a matrix initialized to zero
   correlation_matrix = pd.DataFrame(np.zeros((4,4)))
   for i in range (1,5):
    for j in range(i+1,5):
     x=data.iloc[classranges[k]:classranges[k+1],i].values
     print(x)
     y=data.iloc[classranges[k]:classranges[k+1],j].values
     print(y)
     correlation_matrix[i-1][j-1] = correlation(x,y)
     title='Correlation Matrix of '+ str(classes[classranges[k]])
   PlotCorrelationMatrix(correlation_matrix,headers,title)
  return correlation_matrix

def PlotCorrelationMatrix(corMatrix,headers,title):
 mask = np.zeros_like(corMatrix)
 mask[np.triu_indices_from(mask)] = True

 with sns.axes_style("white"):
  plt.figure()
  plot = sns.heatmap(corMatrix,mask=mask, vmin = 0, vmax = 1, square = True,annot=True,cmap=sns.diverging_palette(220,10, as_cmap = True))
  plot.set_xticklabels(labels = headers, rotation=20)
  plot.set_yticklabels(labels = headers, rotation=20)
  plot.set_title(title)
  plt.savefig(title)
  
  return

def correlation(x,y):
    meanX= np.mean(x)
    meanY = np.mean(y)
    #calculate deviation scores
    DevScoresX=[]
    DevScoresY=[]
    count= len(x)
    for i in range(count):
        DevScoresX.append(x[i]-meanX)
        DevScoresY.append(y[i]-meanY)
    #calculate the sum products(sp)& sumSquares(SSx,SSy)
    Sp=SSx=SSy=0
    for i in range(count):
        Sp=Sp+(DevScoresY[i]*DevScoresX[i])
        SSx=SSx+np.power(DevScoresX[i],2)
        SSy=SSy+np.power(DevScoresY[i],2)
    Sx= np.sqrt(SSx)
    Sy= np.sqrt(SSy)
    return (Sp /(Sx * Sy))

#----------- Question 1: Feature distribution ----------
# 1)
   #import the data set
data=pd.read_csv('Wine.csv')
GenerateAllCorrelationMatrix(data)



















