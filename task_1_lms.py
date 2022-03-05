from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper_accepting_arguments(*args):
        inner_args = ','.join([str(arg) for arg in args])
        print(f'{func.__name__} called with {inner_args}')

    return wrapper_accepting_arguments


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


def main():
    add(4, 5)
    square_all(2, 3)


if __name__ == '__main__':
    main()
