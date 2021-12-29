import random


def get_string():
    return input('Give me string: ')


def create_strings(given_string):
    new_strings_list = []
    string_length = len(given_string)
    chars = list(given_string)
    for j in range(string_length):
        random.shuffle(chars)
        new_strings_list.append(''.join(chars))
    return new_strings_list


def create_strings_1(given_string):
    new_strings_list = []
    string_length = len(given_string)
    for j in range(string_length):
        x = random.sample(given_string, string_length)
        new_strings_list.append(''.join(x))
    return new_strings_list


def create_strings_2(given_string):
    strings_list = []
    for i in given_string:
        chars = list(given_string)
        new_list = []
        while len(chars) > 0:
            r = random.randint(0, len(chars) - 1)
            new_list.append(chars[r])
            del chars[r]
        strings_list.append(''.join(new_list))
    return strings_list


if __name__ == '__main__':
    print(create_strings_2(get_string()))
