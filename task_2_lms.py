def price_count(stock: dict, prices: dict) -> int:
    total_price = sum(stock[fruit] * prices[fruit] for fruit in stock if fruit in prices)
    print(total_price)
    return total_price


def main():
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    price_count(stock=stock, prices=prices)


if __name__ == '__main__':
    main()
