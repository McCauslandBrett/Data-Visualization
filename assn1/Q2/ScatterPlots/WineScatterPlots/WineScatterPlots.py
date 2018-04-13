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

#precondition:
#postcondition:
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
def GenerateAllscatter(data,classes,classranges):
    classes = data.iloc[:,4].values  
    headers=list(data)
    #print(classes)
    headers.pop()
    
    numAttributes=len(headers)
    numcol=len(headers)
    numclass=(len(classranges)-1)
    print(numclass)
    for k in range(numclass):
      for i in range(numcol):
        for j in range(i+1,numcol):
            x=data.iloc[classranges[k]:classranges[k+1],i].values
            y=data.iloc[classranges[k]:classranges[k+1],j].values
            plt.scatter(x,y)
            plt.xlabel(headers[i])
            plt.ylabel(headers[j])
            plt.title(headers[i]+' & '+headers[j])
            print('class flower='+classes[classranges[k]])
            print('attribute pair='+headers[i]+','+headers[j])
            plt.savefig(classes[classranges[k]]+' '+headers[i]+' '+headers[j])
            plt.close()
    return
#----------- Question 1: Feature distribution ----------
# 1)
   #import the data set
#data=pd.read_csv('IrisDataSet.csv')
#headers=list(data) # get every column(attribute) title
#headers.pop() #remove the class column
#classes=[]
#classranges=[]
#Gatherclasses(data,classes,classranges)
#GenerateHistograms(data,AllbinSizes,headers,classes,classranges)


# 2) [20%] For the same data (organized in the same way as above), 
# plot their Box-plots. You may use a library function for this.
#classes=[]
#classranges=[]
#Gatherclasses(data,classes,classranges)
#df = data.iloc[classranges[0]:classranges[1],0].values 
#Boxplots(df,'title','ylabel','xlabel')
#(data,headers,classes,classranges)
#GenerateBoxplots(data,headers,classes,classranges)

# Question 2: Relations between features and data points  [60%]
# 1) [20%]  Correlation Plots 
data=pd.read_csv('IrisDataSet.csv')
headers=list(data) # get every column(attribute) title
headers.pop() #remove the class column
classes=[]
classranges=[]
Gatherclasses(data,classes,classranges)
GenerateAllscatter(data,classes,classranges)

