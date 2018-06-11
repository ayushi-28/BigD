#!/usr/bin/python2

from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pyplot

import numpy as np

fl=open('/collectdata.txt','r')
data=fl.read()
fl.close()
#reading data from downloaded hive file

spl=data.splitlines()
#removing /n

str1=','.join(spl)
#converting into list elements with separartor ','

lst=str1.split(',')




dic= dict(Counter(lst))
#counting occurence of each word and saving as key-value pair

nke=list(dic.keys())
print nke
nkey=np.arange(len(nke))
nvalu=list(dic.values())
nval=map(int,nvalu)
#print nkey
print nval

#creating two lists for keys and their values
plt.title('Plotting repitition of words')
plt.xlabel("words")
plt.ylabel("no. of occurences")
#labels x-axis and y-axis

plt.bar(nkey,nval,label="occurences of words",align='center')
#creates a bar graph

plt.xticks(nkey,nke)
 # Set locations and labels

plt.legend()
plt.show()
