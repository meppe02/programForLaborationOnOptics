import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv
from scipy.optimize import minimize

lambd = 750e-9  # Lambda
radius = 1e-5  # Diameter of hole
dist = 1e-3


class Labb:
    def __init__(self):
        ###Plotting###
        pass
        ###Labb parameters###
        # Difraction and interferance
        # self.lambd, self.radius, self.dist= lambd, radius, dist #Wave lenght, hole radius, distance from whole

    def setPlot(nrPlots):
        pass

    def FresnelvsFraunhofer(self, lambd, radi, dis, printing=True):
        N_f = (radi**2) / (lambd * dist)
        if printing:
            print(
                f'\nF>>1:Fresnel diffraction (near-field)\nF<<1:Fraunhofer diffraction(far-field)\nYour ans:{N_f} => prob:{"Fresnel" if (N_f>=1) else "Fraunhofer"}\n'
            )
        return N_f

    def Fresnel(self):
        # KOLLA LADRIG PÅ DETTA IGEN, DET VAR HEMSKT!!!
        return 0

    def Fraunhofer(self, lambd, radi):
        func = lambda x: ((2 * jv(1, x)) / x) ** 2
        angle = np.arcsin((1.22 * lambd) / (2 * radius))
        deg = 180 * angle / np.pi
        return func, [deg, f"{deg} degrees"]


labb = Labb()
# labb.FresnelvsFraunhofer( lambd, radius, dist)
Fraunfunc, angle = labb.Fraunhofer(lambd, radius)
print(angle[1])
x = np.linspace(-10, 10, 10000)
plt.plot(x, Fraunfunc(x))
plt.grid(True)
plt.show()
