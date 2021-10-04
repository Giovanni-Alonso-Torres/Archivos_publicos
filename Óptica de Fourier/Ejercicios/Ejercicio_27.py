#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftshift


# In[2]:


w = 1
N = 100

Bx = 2*3*np.sqrt(2)*w
Δx = Bx/N
x = np.linspace(-Bx/2, Bx/2, N)   # Espacio real

Bf = 1/Δx                         # Ancho de banda en frecuencia
Δf = Bf/N                         # Muestreo en frecuencia
f = np.linspace(-Bf/2, Bf/2, N)   # Espacio de Fourier


# In[3]:


g = np.exp(-x**2/w**2)/np.sqrt(np.pi*w)   # Función en el espacio real
Ga = np.sqrt(w)*np.exp(-(np.pi*w*f)**2)   # Transformada analítica
Gn = abs(fftshift(fft(g)))*Δx             # Transformada numérica


# In[4]:


plt.plot(x, g)


# In[5]:


plt.plot(f, Ga, '.', color='red')
plt.plot(f, Gn, color='orange')


# In[6]:


Gn = abs(fft(g))*Δx # Transformada numérica sin fftshift


# In[7]:


plt.plot(f, Ga, '.', color='red')
plt.plot(f, Gn, color='orange')
plt.show()


# Se observa que la función implementada `fft` primero entrega las frecuencias positivas y luego las negativas en orden ascendente. Por ello es necesario utilizar `fftshift` para desplazar el 0 al centro.
