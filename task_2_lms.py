def fibonacci_search(lys, val):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2

    while fib < len(lys):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
    index = -1

    while fib > 1:
        i = min(index + fib_minus_2, (len(lys) - 1))

        if lys[i] < val:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            index = i
        elif lys[i] > val:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            return i

    if fib_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val:
        return index + 1
    return -1


print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
