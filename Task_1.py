# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = int(input("Введите номер дня недели = "))
while a<1 or a>7:
    print('Такого дня недели не существует')
    a = int(input('Введите номер дня недели = '))

if a == 6 or a == 7:
    print("Это выходной день!")
else:
    print("Это НЕ выходной день!")
