from sympy import symbols, nsolve

x = symbols('x')
equation = x**5 - 4*x + 2
solutions = nsolve(equation, x, (-5, 5))  # Предположим, что корни находятся в интервале от -5 до 5
print(solutions)

res = float(508 ** 5 - 4 * 0.508 + 2)
print(res)