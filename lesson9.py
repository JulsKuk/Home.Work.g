DICT = {'jul': 1234, 'ttt': 5555}


def chec(username, password):
    for key, value in DICT.items():
        if key == username and value == password:
            return True
        else:
            return False


def authenticate():
    return True


def decorate(login_func):
    def wrapper(username, password):
        if not chec(username, password):
            return False
        if not authenticate():
            return False
        return login_func
    return wrapper


@decorate
def login(username, password):
    return True


def main():
    count = 0
    while count < 4:
        username = (input('введите имя :  '))
        password = int(input('введите пароь :  '))
        count += 1
        if chec(username, password) == False:
            print('Неправильный пароль , осталось попыток:', 4 - count)
        else:
            print('Пароль верный, Вы в системе')
            break
        login(username, password)


if __name__ == '__main__':
    main()
