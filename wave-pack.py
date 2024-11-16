import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
def choose(n, k):
  """
  Return number of combinations for n by k
  """

  if k < n-k:
    return np.prod(np.arange(n, n-k, -1)/np.arange(k, 0, -1))
  return np.prod(np.arange(n, k, -1)/np.arange(n-k, 0, -1))

def psi(x, t, El, Eh, N, Bt):
  """
  Calculate wave function
  for wave packet of N number
  with energy in range [El, Eh]
  """
  
  E = np.linspace(El, Eh, N)
  k = np.sqrt(E)
  return np.sum([Bt[l]*np.exp(1j*k[l]*x-1j*E[l]*t) for l in np.arange(N)], axis = 0)

def betas(N):
  """
  Return array of betes
  """
  
  Bt = np.array([choose(N-1, k)/2**(N-1) for k in np.arange(N)])
  return Bt
 
def animPsi(Xmin = -3, Xmax = 5, Tmax = 100, El = 3, Eh = 5, N = 2, Bt = 1, dx = 1e-2, dt = 1e-2):
  """
  Draw evolution of wave packet constructed from N modes
  with energy in range [El, Eh]
  """
  
  xx = np.arange(Xmin, Xmax+dx, dx)
  y1 = -1.0
  y2 = 1.0
  tm_tmpl = "t = %03.2f"
  ps = lambda x,t: psi(x, t, El, Eh, N, Bt)
  lbl = "Time development of"

  lbl += r" $|\Psi|^{2}$"
  f = lambda t: np.abs(ps(xx,t))**2
  y1 = 0.
  y2 = 1.1*np.amax(f(0))
  lbl += f" with {N} modes"
  
  fig, ax = plt.subplots()
  line, = ax.plot(xx, f(0))
  tm_x = 0.45
  tm_y = 0.10
  tm_txt = ax.text(tm_x, tm_y, '', transform = ax.transAxes)

  def init():
    ax.set_xlim(Xmin, Xmax)
    ax.set_ylim(y1, y2)
    return line,

  def animate(t):
    line.set_ydata(f(t))
    tm_txt.set_text(tm_tmpl % t)
    return line, tm_txt

  ani = anim.FuncAnimation(fig, animate, frames = np.arange(0, Tmax+dt, dt), init_func = init, interval = 10, repeat = False, blit = True, save_count = 1500)
 # lbl += f"\n{text}"
  plt.title(lbl)
  plt.grid(True)
  plt.show()

  return ani
 
