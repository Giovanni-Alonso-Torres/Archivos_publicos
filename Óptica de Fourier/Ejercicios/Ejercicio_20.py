#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.fft import fft2, ifft2, fftfreq, fftshift
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


Lx = 3
Ly = 2


# In[3]:


lim = 5
N = 1000
x = np.linspace(-lim, lim, N)
Δx = x[1]-x[0]
y = np.linspace(-lim, lim, N)
Δy = y[1]-y[0]
X, Y = np.meshgrid(x, y)


# In[4]:


def rect(x, n, L):
    return abs(x-n*L) < L/4


# In[5]:


p = 0
for n in range(-5,6):
    for m in range(-5,6):
        p += rect(X,n,Lx)*rect(Y,m,Ly)


# In[6]:


plt.figure(figsize=(6,6))
plt.axes(projection='3d').plot_surface(X,Y,p,cmap='viridis')
plt.show()

