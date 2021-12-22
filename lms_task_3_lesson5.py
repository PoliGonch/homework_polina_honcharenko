from typing import Union


def operator(x: Union[float, int], y: float | int) -> dict[str, float]:
    results = {''
               'addition': x + y,
               'substraction': x - y,
               'division': x / y,
               'multiplication': x * y,
               'exponent': x ** y,
               'Modulus': x % y,
               'floor division': x // y,
               }
    return results


if __name__ == '__main__':
    print(operator(5, 2))
