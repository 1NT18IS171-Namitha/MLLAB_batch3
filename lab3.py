#!/usr/bin/env python
# coding: utf-8


# In[2]:


minx =0
maxx =1
for k in arr:
    x=((k-minx)/(maxx-minx))
    print(x)


# In[3]:


import pandas as pd
from sklearn.cluster import KMeans
df=pd.read_csv('/home/root1/Downloads/Iris-PCA-Kmeans-AdaBoost.csv')
print(df.head(10))
x=df.iloc[:,[0,1,2,3]].values
from sklearn.preprocessing import StandardScaler
x=StandardScaler().fit_transform(x)
print("the standardized values are:",x)
kmeans5=KMeans(n_clusters=5)
#print(Kmeans5.cluster_center_)
y_kmeans5=kmeans5.fit_predict(x)
Error=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i).fit(x)
    b=kmeans.fit(x)
    Error.append(b.inertia_)
import matplotlib.pyplot as plt
plt.plot(range(1,11),Error)
plt.title('elbow method')
plt.xlabel('no of clusters')
plt.ylabel('Error')
plt.show()

