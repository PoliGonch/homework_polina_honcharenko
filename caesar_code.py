import operator
import string
from typing import Final, Callable

ALPHABET: Final[str] = ''.join([
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    string.punctuation,
    ' ',
])


def get_key_and_data(input_data: str) -> tuple[str, str, str]:
    action, key, data_string = input_data.split('|', 2)
    return action, key, data_string


def encrypt_decrypt_data(data: str) -> str:
    action, key, data_string = get_key_and_data(data)
    # alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '
    operates: dict[str, Callable] = {'+': operator.add, '-': operator.sub}
    function_to_eval = operates[action]

    new_key = int(key) % len(ALPHABET)
    new_list = []

    for char in data_string:
        alpha_index = ALPHABET.find(char)

        if alpha_index != -1:
            alpha_index = function_to_eval(alpha_index, new_key)
            new_char_index = alpha_index % len(ALPHABET)
            char = ALPHABET[new_char_index]
        new_list.append(char)

    return ''.join(new_list)

# print(encrypt_decrypt_data('+|2|adHi_хаха 3'))
# print(encrypt_decrypt_data('-|2|cfJk{хахаb5'))
