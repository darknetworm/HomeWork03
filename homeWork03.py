def my_func(num1, num2, num3):
    '''
    Выводит сумму двух наибольших чисел из трех введенных пользователем
    :param num1: первое число
    :param num2: второе число
    :param num3: третье число
    :return: результат выводится на экран непосредственно из функции
    '''
    num = (num1, num2, num3)
    listNum = list(num)
    listNum.remove(min(listNum))
    print(f'Сумма чисел {listNum[0]} и {listNum[1]} составляет {sum(listNum)}')


try:
    userNum1 = float(input('Введите первое число: '))
    userNum2 = float(input('Введите второе число: '))
    userNum3 = float(input('Введите третье число: '))
except ValueError:
    exit(print('Были введены не числа'))

my_func(userNum1, userNum2, userNum3)
