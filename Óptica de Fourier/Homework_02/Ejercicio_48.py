#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.linspace(-1.5,1.5,1000)
def rect(x, w):
    return np.abs(x)<w/2


# In[3]:


S = (1-abs(x))*rect(x,2)   # OTF sin el obstáculo
O = (4/3)*(1-np.abs(x))*rect(x,2)+(1/3)*(1-np.abs(2*x))*rect(x,1)-(1-np.abs(1/6+2*x/3)-np.abs(1/6-2*x/3))*rect(x,3/2)


# In[4]:


plt.figure(figsize=(12,6))
plt.plot(x,S, label='Sin obstáculo')
plt.plot(x,O, label='Con obstáculo')
plt.legend(fontsize=18)
plt.xlabel(r'$f_{x}/f_{c}$', fontsize=20)
plt.ylabel(r'$\mathcal{H}(f_{x},0)$   [OTF]', fontsize=20)


# In[5]:


w = 2
ϵ = 10e-3
a = w*(1-ϵ)
L = (w**2*(1-np.abs(x))*rect(x,2)+a**2*(1-(w/a)*np.abs(x))*rect(x,2*a/w)-2*a*w*((1/2+a/(2*w)-np.abs(1/4-a/(4*w)-x/2)-np.abs(1/4-a/(4*w)+x/2)))*rect(x,(w+a)/w))/(w**2-a**2)


# In[6]:


plt.figure(figsize=(12,6))
plt.plot(x,L, label='Obstaculo ancho $a=w(1-\epsilon)$', color='darkgreen')
plt.legend(fontsize=18)
plt.xlabel(r'$f_{x}/f_{c}$', fontsize=20)
plt.ylabel(r'$\mathcal{H}(f_{x},0)$   [OTF]', fontsize=20)
plt.show()