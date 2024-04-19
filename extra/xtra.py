import numpy as np
from numpy import cos
import sympy as sp
# 2 пример
t = sp.symbols('t')
c = sp.Matrix([
    [(1-t**2)/(1+t**2), 2*t/(1+t**2)],
    [-2*t/(1+t**2), (1-t**2)/(1+t**2)]
])
# 4 пример
a = np.array([[5., 2., 0.],
              [7., 3., 0.],
              [0., 0., 1.]])
# 1 пример
b = np.array([[np.cos(np.pi/3), -np.sin(np.pi/3)], [np.sin(np.pi/3), np.cos(np.pi/3)]])
# 3 пример
h, z = sp.symbols('a b')
matrix = sp.Matrix([[h**2, h*z],
                    [h*z, z**2]])
det_d = matrix.det()
det_a = np.linalg.det(a)
det_b = np.linalg.det(b)
det_c = c.det()
print(det_a)
print(det_b)
print(det_c)
print(det_d)