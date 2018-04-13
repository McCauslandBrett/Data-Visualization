# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#precondition:
#postcondition:
def BinData(data,numbins,bins):

 print(data)
 set=data
 set.sort()

 print(set) #debugger

 Size= set.size-1
 largest=set[Size]
 print('largest =',largest)
 smallest=set[0]
 
 
 print('smallest =',smallest)
 binwidth= ((largest-smallest)/numbins)
 print('binwidth=',binwidth)
 arraycounter=[] 
 arraycounter.append(0)
 binValue=binwidth+smallest
 
 bins.append(binValue)
 print('binValue=',binValue)
 index = 0
 for counter in range(Size):
   if(set[counter]<=binValue):
    arraycounter[index]=  arraycounter[index]+1
   else:
    arraycounter.append(0)
    index=index+1
    binValue=binValue+binwidth
    bins.append(binValue)
   
 return arraycounter

#precondition: data is the entire table data set,classes[],classranges[]
#postcondition: variables contain; classes(class column)
#classranges (beginning and ending of where  class rows end)
def Gatherclasses(data,classes,classranges):
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

def GenerateBoxplots(data,headers,classes,classranges):
 classes = data.iloc[:,4].values   
 numAttributes=len(headers)
 #print(title)
 print(headers)
 print(numAttributes)
 print(classranges)
 p=len(classranges)-1
 print(p)
 for everyflower in range(len(classranges)-1):
  title=classes[classranges[everyflower]]
  print(title)
  for Attribute in range(numAttributes):
   df=data.iloc[classranges[everyflower]:classranges[everyflower+1],Attribute].values
   Boxplots(df,title,'Occurance',headers[Attribute])
 return

#precondition:
#postcondition:
def Boxplots(data,title,Ylabel,Xlabel):
 filename = 'BoxPlot'+title+Xlabel
 plt.boxplot(data)
 plt.title(title)
 plt.xlabel(Xlabel) 
 plt.ylabel(Ylabel)
 plt.savefig(filename)
 plt.close()
 return


#import the data set
data=pd.read_csv('IrisDataSet.csv')
classes=[]
classranges=[]
headers=list(data) # get every column(attribute) title
Gatherclasses(data,classes,classranges)
df = data.iloc[classranges[0]:classranges[1],0].values 
Boxplots(df,'title','ylabel','xlabel')
GenerateBoxplots(data,headers,classes,classranges)
























