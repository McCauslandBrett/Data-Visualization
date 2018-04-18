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
 
 return arraycounter

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

def GenerateBoxplots(data,headers,classes,classranges):
 print('Generate Boxplots')
 
 classes = data.iloc[:,0].values #good
 print('classes:', classes)
 
 numAttributes=len(headers) #good
 print(numAttributes)
 
 #print(title)
 print(headers) #good
 print(numAttributes) #good
 print(classranges) #good
 p = (len(classranges)-1)
 #print(p)
 for everyclass in range(p):
  title=classes[classranges[everyclass]]
  print(title)
  for Attribute in range(1,4):
   df=data.iloc[classranges[everyclass]:classranges[everyclass+1],Attribute].values
   print('df',df)
   Boxplots(df,title,'Occurance',headers[Attribute])
 return

#precondition:
#postcondition:
def Boxplots(data,Title,Ylabel,Xlabel):
 
 filename = 'BoxPlot'+ str(Title) + str(Xlabel)   
 plt.boxplot(data)
 plt.title(Title)
 plt.xlabel(Xlabel) 
 plt.ylabel(Ylabel)
 plt.savefig(filename)
 plt.show()
 plt.close()
 return


#import the data set
data=pd.read_csv('Wine.csv')

headers=list(data) # get every column(attribute) title
headers.pop(0) #remove the class column
classes=[]
classranges=[]
AllbinSizes=[5,10,50,100]
Gatherclasses(data,classes,classranges)
#df = data.iloc[classranges[0]:classranges[1],0].values 
#Boxplots(df,'title','ylabel','xlabel')
GenerateBoxplots(data,headers,classes,classranges)
























