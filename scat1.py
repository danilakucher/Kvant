#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def findZero(fn, l=-1, r=1, b=-1, t = 1, eps = 1e-12):
  """
  Find zero of  given function in given window. 
  """
  
  N = 10
  dx = (r-l)/(N-1)
  dy = (t-b)/(N-1)
  while dx > eps or dy > eps:
    x = np.linspace(l, r, N)
    y = np.linspace(b, t, N)
    XX,YY = np.meshgrid(x,y)
    W = fn(XX,YY)
    mn = np.min(W)
    ij = (W == mn)
    x0,y0 = XX[ij],YY[ij]
    x0,y0 = x0[0],y0[0] 

    if mn < eps:
      return np.array([x0,y0])

    l = x0 - 0.5*dx
    r = x0 + 0.5*dx
    b = y0 - 0.5*dy
    t = y0 + 0.5*dy  
    dx = (r-l)/(N-1)
    dy = (t-b)/(N-1)

  print(f"[ERROR] function seems doesn't have zero in given range")
  return(0,0) 
    

def ampD(E,a=1,u0=20):
  """
  compute scattering amplitude for giving energy and set width and depth of the well
  """
  
  k = np.emath.sqrt(E)
  kp = np.emath.sqrt(E+u0)
  return 2*np.exp(-1j*k*a)/(2*np.cos(kp*a)-1j*(k/kp+kp/k)*np.sin(kp*a))
 
def ampD2(E,a=1,u0=20):
  """
  compute scattering amplitude for giving energy and set width and depth of the well
  """
  
  k = np.emath.sqrt(E)
  kp = np.emath.sqrt(E+u0)
  return 2*np.exp(1j*k*a)/(2*np.cos(kp*a)+1j*(k/kp+kp/k)*np.sin(kp*a))



def spectre(E,a=1,u0=20):
  kap = np.emath.sqrt(-E)
  kp = np.emath.sqrt(u0+E)

  return 2*np.cos(kp*a)+(kap/kp-kp/kap)*np.sin(kp*a)

def plotAmp(l=-1, r=1, b=-1,t=1,Nx=100,Ny=100,a=1,u0=20):
  """
  Plot 3d graph of D amplitude within given window
  """
  x = np.linspace(l,r,Nx)
  y = np.linspace(b,t,Ny)
  X,Y = np.meshgrid(x,y)
  Z = X + 1j*Y
  w1 = ampD(Z,a,u0)
  w2 = ampD2(Z,a,u0)
  fig,ax = plt.subplots(subplot_kw = {"projection":"3d"})
  ax.scatter(X,Y,np.abs(w1)**2,label = r'$|D_{1}(E)|^{2}$')
  ax.scatter(X,Y,np.abs(w2)**2,label = r'$|D_{2}(E)|^{2}$')
  ax.set_xlabel(r'$\mathrm{Re}(E)$')
  ax.set_ylabel(r'$\mathrm{Im}(E)$')
  ax.legend()
   

def psi(x):
  """
  Plot wave function.
  """
  pass
  
