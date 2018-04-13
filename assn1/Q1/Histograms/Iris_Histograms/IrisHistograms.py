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

#precondition:
#postcondition:
def Histogram(data,numbins,Title,Ylabel,Xlabel):
 
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
 plt.title(Title)
 filename= Title+Xlabel+str(numbins)
 plt.savefig(filename)
 #pdf.savefig()  # saves the current figure into a pdf page
 plt.close()
 return

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

#precondition: folowing contain; 
# classes(class column)
# headers (Attribute titles)
# classranges (beginning and ending of where  class rows end)
# Allbinsizes(array of bin sizes) 
#postcondition:Histogram graphs exported 
def GenerateHistograms(data,AllbinSizes,headers,classes,classranges):
 classes = data.iloc[:,4].values
 labelY='Occuance'
 numAttributes=len(headers)
 for everyflower in range(len(classranges)-1):
  flower=classes[classranges[everyflower]]
  for Attribute in range(numAttributes):
   df=data.iloc[classranges[everyflower]:classranges[everyflower+1],Attribute].values
   for count in range(len(AllbinSizes)):
    Histogram(df,AllbinSizes[count],flower,labelY,headers[Attribute])
 return


#----------- Question 1: Feature distribution ----------
# 1)
#import the data set
data=pd.read_csv('IrisDataSet.csv')
headers=list(data) # get every column(attribute) title
headers.pop() #remove the class column
classes=[]
classranges=[]
Gatherclasses(data,classes,classranges)
GenerateHistograms(data,AllbinSizes,headers,classes,classranges)
























