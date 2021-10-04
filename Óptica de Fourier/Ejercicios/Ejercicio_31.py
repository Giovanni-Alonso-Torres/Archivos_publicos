#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc


# In[2]:


Nf= 1000                             # Número de Fresnel
S0, C0 = sc.fresnel(np.sqrt(2*Nf))   # Integrales de Fresnel en y = 0
I0 = np.sqrt(2)*(C0+1j*S0)           # I_y en y = 0


# In[3]:


x = np.linspace(-0.7, 0.7, 10000)               # Posición adimensional x/lx
Sm, Cm = sc.fresnel(np.sqrt(2*Nf)*(1-2*x))
Sp, Cp = sc.fresnel(np.sqrt(2*Nf)*(1+2*x))
Ix = (Cm+Cp)/np.sqrt(2)+1j*(Sm+Sp)/np.sqrt(2)   # I_x


# In[4]:


If = abs(Ix*I0)**2   # Intensidad en el regimen de Fresnel


# In[5]:


plt.figure(figsize=(8,6))
plt.plot(x, If, label=r'$N_{f}=1000$', color='orange')
plt.xlabel(r'$\dfrac{x}{l_{x}}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[6]:


Nf= 100                                         # Número de Fresnel
S0, C0 = sc.fresnel(np.sqrt(2*Nf))              # Integrales de Fresnel en y = 0
I0 = np.sqrt(2)*(C0+1j*S0)                      # I_y en y = 0
x = np.linspace(-0.7, 0.7, 10000)               # Posición adimensional x/lx
Sm, Cm = sc.fresnel(np.sqrt(2*Nf)*(1-2*x))
Sp, Cp = sc.fresnel(np.sqrt(2*Nf)*(1+2*x))
Ix = (Cm+Cp)/np.sqrt(2)+1j*(Sm+Sp)/np.sqrt(2)   # I_x
If = abs(Ix*I0)**2                              # Intensidad en el regimen de Fresnel


# In[7]:


plt.figure(figsize=(8,6))
plt.plot(x, If, label=r'$N_{f}=100$', color='purple')
plt.xlabel(r'$\dfrac{x}{l_{x}}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[8]:


Nf= 1                                           # Número de Fresnel
S0, C0 = sc.fresnel(np.sqrt(2*Nf))              # Integrales de Fresnel en y = 0
I0 = np.sqrt(2)*(C0+1j*S0)                      # I_y en y = 0
x = np.linspace(-0.7, 0.7, 10000)               # Posición adimensional x/lx
Sm, Cm = sc.fresnel(np.sqrt(2*Nf)*(1-2*x))
Sp, Cp = sc.fresnel(np.sqrt(2*Nf)*(1+2*x))
Ix = (Cm+Cp)/np.sqrt(2)+1j*(Sm+Sp)/np.sqrt(2)   # I_x
If = abs(Ix*I0)**2                              # Intensidad en el regimen de Fresnel


# In[9]:


plt.figure(figsize=(8,6))
plt.plot(x, If, label=r'$N_{f}=1$', color='darkred')
plt.xlabel(r'$\dfrac{x}{l_{x}}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)


# In[10]:


Nf= 0.01                                                   # Número de Fresnel
S0, C0 = sc.fresnel(np.sqrt(2*Nf))                        # Integrales de Fresnel en y = 0
I0 = np.sqrt(2)*(C0+1j*S0)                                # I_y en y = 0
x = np.linspace(-100, 100, 10000)                           # Posición adimensional x/lx
Sm, Cm = sc.fresnel(np.sqrt(2*Nf)*(1-2*x))
Sp, Cp = sc.fresnel(np.sqrt(2*Nf)*(1+2*x))
Ix = (Cm+Cp)/np.sqrt(2)+1j*(Sm+Sp)/np.sqrt(2)             # I_x
If = abs(Ix*I0)**2                                        # Intensidad en el regimen de Fresnel
x1 = np.linspace(-100, -25, 18)
x2 = np.linspace(-25, 25, 40)
x3 = np.linspace(25, 100, 18)
X = np.concatenate([x1,x2,x3])
Ifh = 16*Nf**2*(np.sin(4*np.pi*Nf*X)/(4*np.pi*Nf*X))**2   # Intensidad en el regimen de Fraunhofer


# In[11]:


plt.figure(figsize=(8,6))
plt.scatter(X, Ifh, marker='.', label=r'$I_{FH}$ con $N_{f}=0.01$', color='grey')
plt.plot(x, If, label=r'$I_{F}$ con $N_{f}=0.01$', color='darkgreen')
plt.xlabel(r'$\dfrac{x}{l_{x}}$', fontsize=16)
plt.ylabel(r'$I_{F}$', fontsize=16)
plt.legend(fontsize=20)
plt.show()