# Запрашиваем ввод первой строки и приводим её к нижнему регистру
str1 = str(input("Введите первую строку: ")).lower()

# Запрашиваем ввод второй строки и приводим её к нижнему регистру
str2 = str(input("Введите вторую строку: ")).lower()

# Проверяем, если длины строк не равны, то они не могут быть анаграммами
if len(str1) != len(str2):
    print("Строки не являются анаграммами.")
# Если отсортированные символы строк совпадают, то строки являются анаграммами
elif sorted(str1) == sorted(str2):
    print("Строки являются анаграммами.")
# В противном случае строки не являются анаграммами
else:
    print("Строки не являются анаграммами.")
