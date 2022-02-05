def mult(a: int, n: int) -> int:
    try:
        if not isinstance(a, int) or not isinstance(n, int):
            raise TypeError("Give me integers")
        if a < 0 or n < 0:
            raise ValueError("This function works only with postive integers")
    except ValueError as exc:
        raise exc

    if a == 0 or n == 0:
        return 0
    elif a == 1:
        return n
    elif n == 1:
        return a
    else:
        return a + mult(a, n - 1)


print(mult(1, 8))

# """
# This function works only with positive integers
#
# >>> mult(2, 4) == 8
# True
#
# >>> mult(2, 0) == 0
# True
#
# >>> mult(2, -4)
# ValueError("This function works only with postive integers")
# """
