import numpy as np
import matplotlib.pyplot as plt

L = 750e-9  # Lambda
d=1e-3 #Diameter of hole
d=np.linspace(1e-6,1e-4, 10000)
y=lambda x:np.arcsin(1.22*np.divide(L,x))*(180)/(np.pi)

plt.plot(d, y(d))
plt.xlabel("Diameter of hole")  # Corrected method call
plt.ylabel("Angle for first minimum")  # Corrected method call
plt.title("LOL")  # Corrected method call
plt.grid(True)
plt.show()