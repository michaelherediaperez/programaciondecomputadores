# Solving Eq systems. Excercise #2.
# ------------------------------------------------------------------------------
# Writed by : Michael Heredia Pérez
# Date      : Mar/2018
# e-mail    : mherediap@unal.edu.co
# Universidad Nacional de Colombia, Manizales field.
# ------------------------------------------------------------------------------

# Libraries.
import numpy as np 

# Defining coefficients matrix.
AA = np.array([[ 2, -1,  4,  1, -1],
              [-1,  3, -2, -1,  2],
              [ 5,  1,  3, -4,  1],
              [ 3, -2, -2, -2,  3],
              [-4, -1, -5,  3, -4]])

# Defining the right-sided vector.
bb = np.array([7, 1, 33, 24, -49])

# Calculatting the inverse of A.
inv_AA = np.linalg.inv(AA)

# The solution AX = b -> X = A^(-1) * b
XX = np.matmul(inv_AA, bb)  

# Showing the answer.
x, y, z, t, u = XX
print('x = {:.1f}'.format(x))
print('y = {:.1f}'.format(y))
print('z = {:.1f}'.format(z))
print('t = {:.1f}'.format(t))
print('u = {:.1f}'.format(u))