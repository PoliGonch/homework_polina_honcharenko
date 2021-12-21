def valid_prone(phone_number: str) -> bool:
    return phone_number.isdigit()


def print_massage():
    example_string = '0123456789'

    if valid_prone(example_string):
        if len(example_string) == 10:
            print("Okey, it's a correct number")
        else:
            print("You numer must be 10 characters long")
    else:
        print("It's not a number!")


if __name__ == '__main__':
    print_massage()
