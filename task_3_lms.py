def is_name_valid(name_from_storage: str, name_from_input: str) -> bool:
    return name_from_storage == name_from_input.lower()


def name_check() -> None:
    name = 'anton'
    user_name = input('Enter your name: ')

    is_equal = is_name_valid(name_from_storage=name, name_from_input=user_name)

    massage_about_state = '' if is_equal else 'not'
    massage = f'Name {name} is {massage_about_state} equal to name {user_name}'
    print(massage)


if __name__ == '__main__':
    name_check()
