def list_creator() -> list:
    numbers_list = list(range(101))
    return numbers_list


def extract_num(numbers_list: list) -> list:
    new_num_list = []
    i = 0
    while i < len(numbers_list):
        if numbers_list[i] % 7 == 0 and numbers_list[i] % 5 != 0:
            new_num_list.append(numbers_list[i])
        i += 1
    return new_num_list


def main():
    extract_num(list_creator())


if __name__ == '__main__':
    main()
