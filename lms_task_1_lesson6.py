def string_manipulation(sample_string):
    if len(sample_string) >= 2:
        expected_string = sample_string[:2] + sample_string[-2:]
    else:
        expected_string = ''
    return expected_string


def string_input():
    return input('write something: ')


if __name__ == '__main__':
    print(string_manipulation(string_input()))