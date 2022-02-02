def count_function():
    x = 3
    a = 1
    foo = 'foo'
    print('A number of local variables:', count_function.__code__.co_nlocals)


def main():
    count_function()


if __name__ == '__main__':
    main()
   