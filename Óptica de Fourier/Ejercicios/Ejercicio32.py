#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
from scipy.integrate import quad_vec


# In[2]:


Nf = 1000
N = 1000
lim = 1
ρ = np.linspace(-lim, lim, N)


# In[3]:


f = lambda s: s*np.exp(1j*np.pi*s**2)*sc.jv(0,4*np.pi*np.sqrt(Nf)*ρ*s)
Uf, err = quad_vec(f, 0, np.sqrt(Nf))
If = 4*np.pi**2*abs(Uf)**2


# In[4]:


plt.figure(figsize=(8,6))
plt.plot(ρ, If, label=r'$N_{f}=1000$', color='orange')
plt.xlabel(r'$\dfrac{r}{l}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[5]:


Nf = 100
N = 1000
lim = 1
ρ = np.linspace(-lim, lim, N)


# In[6]:


f = lambda s: s*np.exp(1j*np.pi*s**2)*sc.jv(0,4*np.pi*np.sqrt(Nf)*ρ*s)
Uf, err = quad_vec(f, 0, np.sqrt(Nf))
If = 4*np.pi**2*abs(Uf)**2


# In[7]:


plt.figure(figsize=(8,6))
plt.plot(ρ, If, label=r'$N_{f}=100$', color='purple')
plt.xlabel(r'$\dfrac{r}{l}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[8]:


Nf = 1
N = 1000
lim = 1.5
ρ = np.linspace(-lim, lim, N)


# In[9]:


f = lambda s: s*np.exp(1j*np.pi*s**2)*sc.jv(0,4*np.pi*np.sqrt(Nf)*ρ*s)
Uf, err = quad_vec(f, 0, np.sqrt(Nf))
If = 4*np.pi**2*abs(Uf)**2


# In[10]:


plt.figure(figsize=(8,6))
plt.plot(ρ, If, label=r'$N_{f}=1$', color='darkred')
plt.xlabel(r'$\dfrac{r}{l}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[11]:


Nf = 0.01
N = 1000
lim = 60
ρ = np.linspace(-lim, lim, N)


# In[12]:


f = lambda s: s*np.exp(1j*np.pi*s**2)*sc.jv(0,4*np.pi*np.sqrt(Nf)*ρ*s)
Uf, err = quad_vec(f, 0, np.sqrt(Nf))
If = 4*np.pi**2*abs(Uf)**2
Ρ = np.linspace(-lim, lim, 100)
Ifh = (np.pi*Nf*2*sc.jv(1,4*np.pi*Nf*Ρ)/(4*np.pi*Nf*Ρ))**2


# In[13]:


plt.figure(figsize=(8,6))
plt.scatter(Ρ, Ifh, marker='.', label=r'$I_{FH}$ con $N_{f}=0.01$', color='grey')
plt.plot(ρ, If, label=r'$I_{F}$ con $N_{f}=0.01$', color='darkgreen')
plt.xlabel(r'$\dfrac{r}{l}$', fontsize=16)
plt.ylabel(r'$I$', fontsize=16)
plt.legend(fontsize=20)
plt.show()