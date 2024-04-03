__all__ = ['check_date']

def is_leap(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def check_date(full_date: str) -> bool:
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in {4, 6, 9, 11} and day > 30:
        return False
    if month == 2:
        if is_leap(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    if day > 31:
        return False
    return True

# Тестирование
date1 = '29.02.2020'
date2 = '31.04.2021'

print(check_date(date1))
print(check_date(date2))
