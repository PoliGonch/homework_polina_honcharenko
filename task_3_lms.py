def make_operation(operator: str, *args: int) -> int:
    result = args[0]
    args = args[1:]

    if operator == "+":
        for arg in args:
            result += arg
    elif operator == "-":
        for arg in args:
            result -= arg
    elif operator == "*":
        for arg in args:
            result *= arg

    return result


if __name__ == '__main__':
    make_operation('*', 3, 2, 5)
