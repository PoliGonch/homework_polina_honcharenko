def math_function() -> int:
    a = input('Give me first number:\n')
    b = input('Give me second number:\n')
    try:
        first_num = int(a)
        second_num = int(b)
        return (first_num ** 2 / second_num)

    except ValueError:
        print('Give me numbers')
    except ZeroDivisionError:
        print('Wrong operation')


if __name__ == '__main__':
    math_function()
