import multiprocessing
from datetime import datetime


def is_prime(number):
    if number in [2, 3]:
        return True
    if number % 2 == 0 or number < 2:
        return False
    return all(number % i != 0 for i in range(3, int(number ** 0.5) + 1, 2))


if __name__ == '__main__':
    t = datetime.now()

    numbers = [1570341764013157, 1637027521802551, 1893530391196711, 4350190374376723]
    pool = multiprocessing.Pool(processes=4)
    res = pool.map(is_prime, numbers)

    print(res)
    print(datetime.now() - t)
