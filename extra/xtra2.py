import sympy as sp

# Объявляем переменные
x, y, z = sp.symbols('x y z')

# Задаем уравнения
eq1 = sp.Eq(sp.sqrt(x - 4*y) - 2*sp.sqrt(x + 3*y), 1)
eq2 = sp.Eq(7*sp.sqrt(x + 3*y) - 5*x + 22*y, 13)
eq3 = sp.Eq(x**4 - y**4, 15)
eq4 = sp.Eq(x**3 * y - x * y**3, 6)
eq5 = sp.Eq(x + y + z, 2)
eq6 = sp.Eq(x**2 + y**2 + z**2, 6)
eq7 = sp.Eq(x**3 + y**3 + z**3, 8)
eq8 = sp.Eq(x/y + y/z + z/x, 3)
eq9 = sp.Eq(y/x + z/y + x/z, 3)
eq10 = sp.Eq(x + y + z, 3)

# Решаем систему уравнений
solutions = sp.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10), (x, y, z))

print(solutions)