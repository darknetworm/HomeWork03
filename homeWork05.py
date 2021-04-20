total = 0


def summary(nums):
    '''
    Возвращает сумму введенных пользователем чисел, игнорируя любые другие символы
    :param nums: введенные пользователем значения
    :return: сумму чисел в глобальную переменную
    '''
    newList = []
    for i in range(len(nums)):
        try:
            newList.append(float(nums[i]))
        except:
            pass
    global total
    total = total + sum(newList)

    return total


listNum = [' ']
while listNum[len(listNum) - 1] != 'q':
    userNums = input(
        'Введите числа через пробел (для окончания ввода нажмите "Enter", для завершения программы - "q + Enter") ')
    listNum = list(userNums)
    print(summary(listNum))
