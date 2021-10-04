#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.linspace(-4, 4, 1000)


# In[3]:


Λ = (1-abs(x))*(abs(x)<1)


# In[4]:


plt.figure()
plt.plot(x, Λ)


# In[5]:


f = np.linspace(-4, 4, 1000)
ftΛ = (np.sin(np.pi*f)/(np.pi*f))**2


# In[6]:


plt.figure()
plt.plot(f, abs(ftΛ), color='red')
plt.show()