def name_check():
    name = 'anton'
    user_name = input('Enter your name: ')
    return name == user_name.lower()


if __name__ == '__main__':
    print(name_check())
