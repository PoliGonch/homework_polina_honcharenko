import random


def generate_number() -> int:
    number = random.randint(0, 9)
    return number


def input_number() -> int:
    your_input = input("Try to guess the number: ")
    your_number = int(your_input)
    return your_number


def compare_number(generated_number: int, guessed_number: int) -> bool:
    return generated_number == guessed_number


def massage_print():
    is_equal = compare_number(generated_number=generate_number(), guessed_number=input_number())
    print(generate_number())
    if is_equal:
        print("Wow! You guessed")
    else:
        print("Oops, try again")


if __name__ == '__main__':
    massage_print()
