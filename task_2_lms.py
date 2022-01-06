import random


def list_generator() -> list:
    numbers_list = []
    while len(numbers_list) < 10:
        numbers_list.append(random.randint(1, 100))
    return numbers_list


def common_numbers(list_1: list, list_2: list) -> list:
    new_list = []
    new_list = [item for item in list_1 if item in list_2 and item not in new_list]
    return new_list


def main():
    first_list = list_generator()
    second_list = list_generator()
    common_numbers(list_1=first_list, list_2=second_list)


if __name__ == '__main__':
    main()
