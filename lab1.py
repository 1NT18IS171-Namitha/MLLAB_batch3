#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10


# In[2]:


a


# In[3]:


print(a)


# In[4]:


a="hello"


# In[5]:


a


# In[6]:


a='helo'


# In[7]:


a


# In[8]:


arr=[1,2,3,4,5]


# In[9]:


arr


# In[10]:


arr[2]


# In[11]:


arr[1]=20


# In[12]:


arr[1]


# In[13]:


arr[2]=2.5


# In[14]:


arr


# In[15]:


arr[5]="string"


# In[17]:


arr.pop(2)

arr
# In[18]:


arr


# In[19]:


arr1[6]=[1,2,3,4,5,6]


# In[20]:


arr1=[1,2,3,4,5,6]


# In[21]:


arr+arr1


# In[22]:


arr2=arr+arr1


# In[23]:


arr2


# In[24]:


for i in arr2:
    print(i)
    


# In[2]:


e=int(input("enter operand"))
z=int(input("enter operand2"))
q=input("enter operand ")
if(q=='+'):
    print(e+z)
elif(q=='-'):
    print(e-z)
elif(q=='*'):
    print(e*z)
else:
    print(e/z)


# In[20]:


list=[1,2,3,4,5]
mean=0
min=list[0]
max=list[0]
a=len(list)
for i in list:
    mean=mean+i
    if(i<min):
        min=i
    if(i>max):
        max=i
m=int(a/2)
if (a%2==0):
    n=(list[m]+list[m-1])/2
    median=n
    print(median)
else:
    print(list[m])
    
print(min)
print(max)
print(mean/5)


# In[ ]:




