def userdata(name='Имя не указано', surname='Фамилия не указана', birthdate='Дата рождения не указана',
             citylive='Место проживания не указано', email='Электронная почта не указана', tlph='Телефон не указан'):
    '''
    Выводит в строку введенные пользователем пааметры
    :param name: Имя
    :param surname: Фамилия
    :param birthdate: Дата рождения
    :param citylive: Место проживания
    :param email: Электронная почта
    :param tlph: Телефон
    :return: результат выводится на экран непосредственно из функции
    '''
    print('| {} | {} | {} | {} | {} | {} |'.format(name, surname, birthdate, citylive, email, tlph))


userList = {}
userName = input('Введите имя: ')
if userName != '':
    userList['name'] = userName.title()
userSurname = input('Введите фамилию: ')
if userSurname != '':
    userList['surname'] = userSurname.title()
userBirthdate = input('Введите дату рождения: ')
if userBirthdate != '':
    userList['birthdate'] = userBirthdate
userCitylive = input('Введите место проживания: ')
if userCitylive != '':
    userList['citylive'] = userCitylive.title()
userEmail = input('Введите электронную почту: ')
if userEmail != '':
    userList['email'] = userEmail
userTlph = input('Введите телефон: ')
if userTlph != '':
    userList['tlph'] = userTlph

userdata(**userList)
