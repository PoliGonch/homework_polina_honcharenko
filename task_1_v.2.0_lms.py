import concurrent
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def is_prime(que: multiprocessing.Queue, result: multiprocessing.Queue):
    while not que.empty():
        number = que.get()
        if number in [2, 3]:
            result.put(f'{number} True')
        if number % 2 == 0 or number < 2:
            result.put(f'{number} False')
        result.put(f'{number} {all(number % i != 0 for i in range(3, int(number ** 0.5) + 1, 2))}')


def main():
    t = datetime.now()
    manager = multiprocessing.Manager()
    que = multiprocessing.Queue()
    que_result = multiprocessing.Queue()
    result = manager.dict()

    numbers = [1570341764013157, 1637027521802551, 1893530391196711, 4350190374376723]
    for number in numbers:
        que.put(number)

    p1 = multiprocessing.Process(target=is_prime, args=(que, que_result))
    p1.start()
    p2 = multiprocessing.Process(target=is_prime, args=(que, que_result))
    p2.start()
    p1.join()
    p2.join()

    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        processes = []
        elements = []
        for number in numbers:
            processes.append(executor.submit(is_prime, que, que_result))

        for process in concurrent.futures.as_completed(processes):
            try:
                elements.append(process.result())
            except StopIteration:
                break

    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        threads = []
        elements = []
        for _ in numbers:
            threads.append(executor.submit(is_prime, que, que_result))

        for thread in concurrent.futures.as_completed(threads):
            try:
                elements.append(thread.result())
            except StopIteration:
                break

    while not que_result.empty():
        print(que_result.get())

    print(datetime.now() - t)


if __name__ == '__main__':
    main()
