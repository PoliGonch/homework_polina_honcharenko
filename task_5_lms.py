def sum_of_digits(digit_string: str) -> int:
    if not digit_string:
        return 0
    try:
        digit = int(digit_string[0])
    except ValueError:
        raise ValueError('input string must be digit string')

    if len(digit_string) == 1:
        return digit
    return sum_of_digits(digit_string[1:]) + digit


print(sum_of_digits('12345'))
