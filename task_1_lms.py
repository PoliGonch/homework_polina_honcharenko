def oops() -> None:
    raise IndexError("Wrong index!")


def another_func() -> None:
    list = [1, 2, 3]
    try:
        print(list[50])
    except:
        oops()


if __name__ == '__main__':
    another_func()
