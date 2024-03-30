import os
# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии
def split_path(file_path):
    path, filename = os.path.split(file_path)
    filename, ext = os.path.splitext(filename)
    return path, filename, ext

file_path = "C:/Users/tagan/Documents/moi_doci.txt"
path, filename, ext = split_path(file_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", ext)
