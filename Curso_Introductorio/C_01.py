# -*- coding: utf-8 -*-
# 
# # Minimizing mean squared error. Excercise #1.
# ------------------------------------------------------------------------------
# Writed by : Michael Heredia Pérez
# Date      : Mar/2018
# e-mail    : mherediap@unal.edu.co
# Universidad Nacional de Colombia, Manizales field.
# ------------------------------------------------------------------------------

# Libraries.
import numpy as np 
import matplotlib.pyplot as plt

# Loading .dat file.
X, Y = np.loadtxt("data_ej_01.dat", unpack = True)

# %% ploting y as a x function
plt.figure()
plt.plot(X, Y, 'b*')
plt.grid()
plt.xlabel(r'$x$', fontsize = 15)
plt.ylabel(r'$y$', fontsize = 15)
plt.show()

# Knowing the graph, the I asume the polynomial degree.
n = 3 # polynomial grade.

# Looking for the coeficientes.
coeffs_3 = np.polyfit(X, Y, n)
print("The optimal coefficients are:", coeffs_3)

# Seting up the polynomial values.
fit_3 = np.polyval(coeffs_3, X)

# Ploting the adjusted polynomial and the points.
plt.figure()
plt.plot(X, Y, label = 'Data')
plt.plot(X, fit_3, 'r--', label = 'Fit, N = {}'.format(n))
plt.legend(loc = 'best')
plt.xlabel(r'$x$', fontsize = 15)
plt.ylabel(r'$y$', fontsize = 15)
plt.show()

# Computing the error 'r' for n = 3.
r_3 = np.sum((fit_3 - Y)**2)
print('The error for n = 3 is:', r_3)

# %% Now, let's change the polynomioal degree n.
n = 5

# Looking for the coeficientes.
coeffs_5 = np.polyfit(X, Y, n)
print("The optimal coefficients are:", coeffs_5)

# Seting up the polynomial values.
fit_5 = np.polyval(coeffs_5, X)

# Ploting the adjusted polynomial and the points.
plt.figure()
plt.plot(X, Y, label = 'Data')
plt.plot(X, fit_5, 'r--', label = 'Fit, N = {}'.format(n))
plt.legend(loc = 'best')
plt.xlabel(r'$x$', fontsize = 15)
plt.ylabel(r'$y$', fontsize = 15)
plt.show()

# Computing the error 'r' for n = 3.
r_5 = np.sum((fit_5 - Y)**2)
print('The error for n = 5 is:', r_5)