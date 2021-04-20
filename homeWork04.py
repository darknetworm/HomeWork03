def my_func1(arg, stp):
    '''
    Возведение в степень с помощью оператора **
    :param arg: возводимое в степень число
    :param stp: степень
    :return: возвращает результат
    :rtype float
    '''
    exponent = arg ** stp
    return exponent


def my_func2(arg, stp):
    '''
    Возведение в степень с помощью цикла
    :param arg: возводимое в степень число
    :param stp: степень
    :return: возвращает результат
    :rtype float
    '''
    exponent = 1
    for i in range(stp, 0, 1):
        exponent = exponent * 1 / arg
    return exponent


try:
    userNum = float(input('Введите число для возведения в степень: '))
    userStep = int(input('Введите степень: '))
    if userStep > 0:
        userStep = 0 - userStep
        print(f'Введено положительное число, поэтому будем использовать число {userStep}')
except ValueError:
    exit(print('Было введено не число'))

print(f'Используем оператор "**" >>> {my_func1(userNum, userStep)}')
print(f'Используем цикл >>> {my_func2(userNum, userStep)}')
