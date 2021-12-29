def get_name_and_age() -> tuple[str, int]:
    get_name = input("What is your name?")
    get_age = input('How old are you?')
    return get_name, int(get_age)


def greeting_program(name: str, age: int) -> None:
    print(f'Hello {name}, on your next birthday you’ll be {age + 1} years')


def main() -> None:
    name, age = get_name_and_age()
    greeting_program(name=name, age=age)


if __name__ == "__main__":
    main()
