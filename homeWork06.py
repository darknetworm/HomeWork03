def convertText(text):
    '''
    Преобразует слова из текста с заглавной буквы
    :param text: введенный пользователем текст
    :return: преобразованный текст
    '''
    return text.title()


userText = input('Введите предложение: ')
print(convertText(userText))
