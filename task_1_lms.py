import random


def greatest_number(list: list) -> int:
    return max(list)


def main() -> None:
    numbers_list = []
    while len(numbers_list) < 10:
        numbers_list.append(random.randint(1, 100))
    greatest_number(numbers_list)


if __name__ == '__main__':
    main()
