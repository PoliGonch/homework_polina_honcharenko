def dict_of_string(example_string):
    translator = str.maketrans('', '', ',.!:;-<>=')
    new_string = example_string.translate(translator)

    divided_string = new_string.title().split()
    new_dict = {world: divided_string.count(world) for world in divided_string}
    return new_dict


def main():
    example_string = input('Give me a string:\n')
    dict_of_string(example_string=example_string)


if __name__ == '__main__':
    main()
