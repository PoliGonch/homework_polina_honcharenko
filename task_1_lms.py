import concurrent.futures
import logging
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Optional


def init_logging(is_verbose: bool = False):
    logging.basicConfig(
        stream=sys.stdout,
        format='[%(asctime)s.%(msecs)03d] '
               '[PROCESS %(process)d %(processName)s] '
               '[THREAD %(thread)d %(threadName)s] '
               '%(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG if is_verbose else logging.INFO,
    )


def square_num(number: int) -> int:
    logging.info('Logging square')
    return number ** 2


def cubic_num(number: int) -> int:
    logging.info('Logging cubic')
    return number ** 3


def fibonacci_num(number: int) -> int:
    if not (isinstance(number, int) and number >= 0):
        raise ValueError(f'Positive integer number expected, got "{number}"')

    if number in {0, 1}:
        return number

    previous, fib_number = 0, 1
    for _ in range(2, number + 1):
        previous, fib_number = fib_number, previous + fib_number

    logging.info('Logging fibbonacci')

    return fib_number


def factorial_num(number: int) -> int:
    factorial = 1
    if number != 0:
        for i in range(1, number + 1):
            factorial *= i
    logging.info('Logging factorial')
    return factorial


def sequentially(function_list: list[Callable], input_list: list[int]) -> list[list[int]]:
    list_of_results = []
    for function in function_list:
        result_func = list(map(function, input_list))
        list_of_results.append(result_func)
    return list_of_results


def thread_pool_executor(function_list: list[Callable], input_list: list[int]) -> list[list[int]]:
    logging.info('Logging thread')
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(function_2, function_list, generator(input_list)))
    return results


def function_2(function: Callable, input_list: list[int]) -> list[int]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        logging.info('Logging function 2')
        result = list(executor.map(function, input_list))
    return result


def process_pool_executor(function_list: list[Callable], input_list: list[int]) -> list[list[int]]:
    logging.info('Logging thread')
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(function_3, function_list, generator(input_list)))
    return results


def function_3(function: Callable, input_list: list[int]) -> list[int]:
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        logging.info('Logging function 2')
        result = list(executor.map(function, input_list))
    return result


def generator(input_list: list[int]):
    while True:
        yield input_list


@dataclass
class Benchmark:
    start_time: Optional[datetime] = None

    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start_time)


def main():
    function_list = [
        square_num,
        cubic_num,
        fibonacci_num,
        factorial_num,
    ]

    list_of_nums = list(range(9000, 25000, 1000))
    # print(sequentially(function_list, list_of_nums))
    # print(thread_pool_executor(function_list, list_of_nums))
    # print(process_pool_executor(function_list, list_of_nums))

    for function in [sequentially, thread_pool_executor, process_pool_executor]:
        with Benchmark():
            function(function_list, list_of_nums)


if __name__ == '__main__':
    # init_logging()
    main()
