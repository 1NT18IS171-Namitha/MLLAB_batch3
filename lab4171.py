#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('data.csv')


# In[3]:


x1=dataset["x1"].values


# In[4]:


x1


# In[5]:


x2=dataset["x2"].values


# In[6]:


x2


# In[7]:


x=np.array(list(zip(x1,x2)))
c_x=[2.3,6.8,9.2]
c_y=[1.4,7.5,9.1]


# In[8]:


x


# In[9]:


centroid=np.array(list(zip(c_x,c_y)))


# In[10]:


centroid


# In[11]:


k=3


# In[12]:


for i in x:
    for j in centroid:
        dist = np.linalg.norm(i-j)
        print(dist)


# In[5]:


import numpy as np
import pandas as pd
from copy import deepcopy


def euclidean(a,b, ax=1):
    return np.linalg.norm(a-b, axis=ax)

    k = 3
    X = pd.read_csv('data.csv',index_col=False)
    print(X)

    x1 = X['X1'].values
    x2 = X['X2'].values
    X = np.array(list(zip(x1, x2)))
    print(X)
    C_x = [6.2, 6.6 ,6.5]
    C_y = [3.2, 3.7, 3.0]
    Centroid = np.array(list(zip(C_x, C_y)), dtype=np.float32)
    print("Initial Centroids")
    print(Centroid.shape)

    Centroid_old = np.zeros(Centroid.shape)
    print(Centroid_old)
    # Cluster Lables(0, 1, 2)
    clusters = np.zeros(len(X))
    print(clusters)
    error = euclidean(Centroid, Centroid_old, None)
    print(error)
    iterr = 0
    # Loop will run till the error becomes zero
    while error != 0:
        # Assigning each value to its closest cluster
        iterr = iterr + 1
        for i in range(len(X)):
            #print(X[i])
            distances = euclidean(X[i], Centroid)
            #print(distances)
            cluster = np.argmin(distances)
            clusters[i] = cluster

        Centroid_old = deepcopy(Centroid)
        
        # Finding the new centroids by taking the Mean
        for p in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == p]
            Centroid[p] = np.mean(points, axis=0)
        print(" Centre of the clusters after ", iterr," Iteration \n", Centroid)
        error = euclidean(Centroid, Centroid_old, None)
        print("Error  ... ",error) 


# In[4]:


import numpy as np
import pandas as pd
from copy import deepcopy


# In[6]:


dataset = pd.read_csv('data.csv')


# In[20]:


def euclidean(a,b, ax=1):
    return np.linalg.norm(a-b, axis=ax)
k = 3
print(dataset)


# In[21]:


x1 = dataset['x1'].values
x2 = dataset['x2'].values
X= np.array(list(zip(x1, x2)))
print(dataset)
C_x = [6.2, 6.6 ,6.5]
C_y = [3.2, 3.7, 3.0]
Centroid = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(Centroid.shape)


# In[22]:


Centroid_old = np.zeros(Centroid.shape)
print(Centroid_old)
# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))
print(clusters)
error = euclidean(Centroid, Centroid_old, None)
print(error)


# In[23]:


iterr = 0
    # Loop will run till the error becomes zero
while error != 0:
    iterr = iterr + 1
    for i in range(len(dataset)):
        distances = euclidean(X[i], Centroid)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    Centroid_old = deepcopy(Centroid)
        
    for p in range(k):
        points = [X[j] for j in range(len(dataset)) if clusters[j] == p]
        Centroid[p] = np.mean(points, axis=0)
    print(" Centre of the clusters after ", iterr," Iteration \n", Centroid)
    error = euclidean(Centroid, Centroid_old, None)
    print("Error  ... ",error)


# In[ ]:




