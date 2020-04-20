#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:05:58 2018

@author: Brettmccausland
""""""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#precondition:
#postcondition:
def BinData(data,numbins,bins):


 set=data
 set.sort()

 Size= set.size-1
 largest=set[Size]
 smallest=set[0]
 
 
 #print('smallest =',smallest)
 binwidth= ((largest-smallest)/numbins)
 #print('binwidth=',binwidth)
 arraycounter=[] 
 arraycounter.append(0)
 binValue=binwidth+smallest
 
 bins.append(binValue)

 index = 0
 for counter in range(Size):
   if(set[counter]<=binValue):
    #print('set value:',set[counter],'fell under ','Binvalue:',binValue,'added to index loc:',index)
    arraycounter[index]=  arraycounter[index]+1
   else:
    #find the correct bin position
     while(set[counter]>binValue):
      #increment the bin value and save it
      binValue=binValue+binwidth
      bins.append(binValue)
      #add value to arraycounter and increment its index
      arraycounter.append(0)
      index=index+1
      if(set[counter]<=binValue):
       #print('set value:',set[counter],'fell under ','Binvalue:',binValue,'added to index loc:',index)
       arraycounter[index]=  arraycounter[index]+1
    
# print(arraycounter) 
 return arraycounter

#precondition:
#postcondition:
def Histogram(data,numbins,Title,Ylabel,Xlabel):
 #print('hist')
 bins=[]
 #returns accurances array & bins stores array of bin labels
 binedData=BinData(data,numbins,bins) 
 
 #setting up graph structure
 x=np.arange(len(binedData))
 bar_width=1
 opacity=0.5
 
 plt.bar(x,binedData,bar_width,color='green',alpha=opacity,align="edge",linewidth=0.5,edgecolor="black")
 plt.xticks(x+bar_width,bins)
 plt.ylabel(Ylabel)
 plt.xlabel(Xlabel)
 T= str(Title)+' '+str(Xlabel)+' '+str(numbins)+' bins'
 plt.title(T)
 filename=T
 
 plt.savefig(filename)
 plt.show()
 plt.close()
 return

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

#precondition: folowing contain; 
# classes(class column)
# headers (Attribute titles)
# classranges (beginning and ending of where  class rows end)
# Allbinsizes(array of bin sizes) 
#postcondition:Histogram graphs exported 
def GenerateHistograms(data,AllbinSizes,headers,classes,classranges):
 #print('generateHist')
 classes = data.iloc[:,0].values
 #print(classes)
 #print(classranges)
 labelY='Occuance'
 #print('classranges', classranges)
 numAttributes=len(headers)
 #print(numAttributes)
 
 for everyclass in range(len(classranges)-1):
  cur_class=classes[classranges[everyclass]]
  # print(cur_class) is selecting the classes correctly
  for Attribute in range(1,4):
   df=data.iloc[classranges[everyclass]:classranges[everyclass+1],Attribute].values
   #print('data:',df)
   for count in range(len(AllbinSizes)):
    print(cur_class)
    print(df)
    Histogram(df,AllbinSizes[count],cur_class,labelY,headers[Attribute])
 return


#----------- Question 1: Feature distribution ----------
# 1)
#import the data set
data=pd.read_csv('Wine.csv')
headers=list(data) # get every column(attribute) title
headers.pop() #remove the class column
classes=[]
classranges=[]
AllbinSizes=[5,10,50,100]
Gatherclasses(data,classes,classranges)
#print(classranges)
GenerateHistograms(data,AllbinSizes,headers,classes,classranges)
























