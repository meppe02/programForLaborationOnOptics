import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

data_poins = 10000


L = 750e-9  # Lambda
a = 100e-9  # Hålets radie
k = 2 * np.pi / L  # Konstant
span = 10*np.pi
t = np.linspace(-span, span, data_poins)
x = k * a * np.sin(t)
x = np.linspace(-10, 10, data_poins)
y = lambda x: ((2 * jv(1, x)) / x) ** 2
# array_of_x=[x*i for i in range(1,10)]
# array_of_lambda_y=[y(x) for x in array_of_x]
# Create a figure and subplots
fig, axs = plt.subplots(2)

# Plot on the first subplot
axs[0].plot(t, y(x))
axs[0].set_xlabel("x")
axs[0].set_ylabel("Intensity")
axs[0].set_title("Intensity of Bessel Function Squared")
axs[0].grid(True)
axs[0].legend(["Subplot 1"])

# Plot on the second subplot
axs[1].plot(x, y(t))
axs[1].set_xlabel("t")
axs[1].set_ylabel("Intensity")
axs[1].set_title("Intensity of Bessel Function Squared")
axs[1].grid(True)
axs[1].legend(["Subplot 2"])

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
