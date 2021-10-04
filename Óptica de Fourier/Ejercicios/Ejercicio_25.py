#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


λ = 1
k = 2*np.pi/λ
x0 = 2
y0 = 5


# In[3]:


y = np.linspace(-10, 10, 1000)
z = np.linspace(0, 5, 1000)
Y, Z = np.meshgrid(y, z)


# In[4]:


s1 = np.sqrt(x0**2+(Y-y0)**2+Z**2)
s2 = np.sqrt(x0**2+(Y+y0)**2+Z**2)


# In[5]:


I = (Z**2/(4*np.pi**2*s1**4))*(k**2+1/s1**2)+(Z**2/(4*np.pi**2*s2**4))*(k**2+1/s2**2)+(Z**2/(2*np.pi**2*s1**2*s2**2))*np.sqrt(k**2+1/s1**2)*np.sqrt(k**2+1/s2**2)*np.cos(k*(s1-s2)-(np.arctan(k*s1)-np.arctan(k*s2)))


# In[6]:


plt.figure(figsize=(6,6))
plt.pcolormesh(Z,Y,I,shading='auto')


# In[7]:


z = np.linspace(0, 100, 1000)
Y, Z = np.meshgrid(y, z)


# In[8]:


s1 = np.sqrt(x0**2+(Y-y0)**2+Z**2)
s2 = np.sqrt(x0**2+(Y+y0)**2+Z**2)


# In[9]:


I = (Z**2/(4*np.pi**2*s1**4))*(k**2+1/s1**2)+(Z**2/(4*np.pi**2*s2**4))*(k**2+1/s2**2)+(Z**2/(2*np.pi**2*s1**2*s2**2))*np.sqrt(k**2+1/s1**2)*np.sqrt(k**2+1/s2**2)*np.cos(k*(s1-s2)-(np.arctan(k*s1)-np.arctan(k*s2)))


# In[10]:


plt.figure(figsize=(6,6))
plt.pcolormesh(Z,Y,I,shading='auto')
plt.show()