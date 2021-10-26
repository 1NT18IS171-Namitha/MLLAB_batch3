#!/usr/bin/env python
# coding: utf-8
import math

list1=[1,2,3,4,5]
mean= sum( list1 )/len(list1)
var=sum(pow(i-mean,2) for i in list1 )/len(list1)
std=math.sqrt(var)
print("var:",var)
print("std:",std)


# In[2]:


arr=[23,51,90,1,4]
n=len(arr)
for i in range(n-1):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(n):
    print("%d" %arr[i])


# In[ ]:




