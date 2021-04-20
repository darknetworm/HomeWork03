def divide(num1, num2):
    '''
    Вычисление деления двух чисел
    :param num1: первое число, введенное пользователем
    :param num2: второе число, введенное пользователем
    :return: печатает результат деления непосредственно из функции
    '''
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('Попытка деления на 0')


try:
    userNum1 = float(input('Введите первое число: '))
    userNum2 = float(input('Введите второе число: '))
except ValueError:
    exit(print('Было введено не число'))

divide(userNum1, userNum2)
