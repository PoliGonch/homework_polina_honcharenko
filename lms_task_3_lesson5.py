from typing import Union, TypeAlias

T_NUMBER: TypeAlias = int | float
T_RESULT: TypeAlias = dict[str, T_NUMBER]


def operator(x: Union[float, int], y: T_NUMBER) -> T_RESULT:
    results = {
        'addition': x + y,
        'substraction': x - y,
        'division': x / y,
        'multiplication': x * y,
        'exponent': x ** y,
        'Modulus': x % y,
        'floor division': x // y,
    }
    return results


def dict_print(data: T_RESULT) -> None:
    for operation, result in data.items():
        print(f'Result for {operation} is {result}')


if __name__ == '__main__':
    dict_print(operator(5, 2))
