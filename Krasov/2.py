print('Точка в области')
a = float(input('Координаты центра круга:\n x = '))
b = float(input(' y = '))
R = float(input('Введите радиус круга: R = '))
if R > 0:
    x = float(input('Координаты точки:\n x = '))
    y = float(input(' y = '))
    if (( (x - a) ** 2 + (y - b) ** 2) <= (R ** 2)):
        print('Точка в курге')
    else:
        print('Точка не в круге')
else:
    print('Радиус круга должен быть положительным')