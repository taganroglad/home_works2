from fractions import Fraction

# Ввод дробей от пользователя
fraction_str1 = input("Введите первую дробь в формате a/b: ")
fraction_str2 = input("Введите вторую дробь в формате a/b: ")

# Преобразование строк в объекты Fraction
numerator1, denominator1 = map(int, fraction_str1.split('/'))
numerator2, denominator2 = map(int, fraction_str2.split('/'))

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

# Вычисление суммы и произведения дробей
sum_result = fraction1 + fraction2
multy = fraction1 * fraction2

print("Сумма дробей:", sum_result)
print("Произведение дробей:", multy)
