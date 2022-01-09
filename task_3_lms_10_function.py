def list_comprehension() -> list:
    new_list = [(i, i ** 2) for i in range(1, 11)]
    print(new_list)
    return new_list


if __name__ == '__main__':
    list_comprehension()
