#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def H(x):
    h = []
    for x0 in x:
        if np.abs(x0)<=2:
            h.append((2/np.pi)*(np.arccos(np.abs(x0)/2)-np.abs(x0)/2*np.sqrt(1-(x0/2)**2)))
        else:
            h.append(0)
    return h


# In[3]:


x = np.linspace(-2.5,2.5,1000)
Hx = H(x)


# In[4]:


plt.figure(figsize=(12,6))
plt.plot(x,Hx, color='darkred')
plt.xlabel(r'$f_{x}/f_{0}$', fontsize=20)
plt.ylabel(r'$\mathcal{H}(f_{x},0)$   [OTF]', fontsize=20)


# In[5]:


w = 3
d = 9
y = np.linspace(-10,10,1000)
Hp = H(y+2*d/w)
H0 = H(y)
Hm = H(y-2*d/w)
Hy = []
for i in range(len(y)):
    Hy.append(0.5*Hp[i]+H0[i]+0.5*Hm[i])


# In[6]:


plt.figure(figsize=(12,6))
plt.plot(y,Hy, color='darkblue')
plt.xlabel(r'$f_{x}/f_{0}$', fontsize=20)
plt.ylabel(r'$\mathcal{H}(0,f_{y})$   [OTF]', fontsize=20)
plt.show()