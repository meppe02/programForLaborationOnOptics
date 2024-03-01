import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv


data_points = 10000

L = 750e-9  # Lambda
a = 100e-9  # Hålets radie
k = 2 * np.pi / L  # Konstant
span = 10 * np.pi
x = np.linspace(-10, 10, data_points)
y = lambda x: ((2 * jv(1, x)) / x) ** 2

plt.plot(x, y(x))
plt.xlabel("x")  # Corrected method call
plt.ylabel("Intensity")  # Corrected method call
plt.title("Intensity of Bessel Function Squared")  # Corrected method call
plt.grid(True)
plt.show()
