class Product:

    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product type: {self.product_type}, name: {self.name}'


class ProductStore:
    product_dict = {}

    def __init__(self, income=0):
        self.income = income

    def add(self, product: Product, amount: int):
        if product in self.product_dict:
            self.product_dict[product]['amount'] += amount
        else:
            self.product_dict[product] = {
                'name': product.name,
                'price': round(product.price * 1.3, 2),
                'amount': amount,
                'income': 0
            }
        return self.product_dict

    def set_discount(self, identifier, percent, identifier_type='name'):
        percent = percent.replace("%", "")
        if identifier_type not in ['name', 'type']:
            raise ValueError('Not correct identifier type')
        temp_list = []
        try:
            for product, product_info in self.product_dict.items():
                if (
                        identifier_type == 'name'
                        and product_info['name'] == identifier
                        or identifier_type == 'type'
                        and product.product_type == identifier
                ):
                    product_info['price'] = round(product_info['price'] * (1 - int(percent) / 100), 2)
                    temp_list.append(product)
            if temp_list == []:
                print('No products found')
        except ValueError as exc:
            print(exc)

    def sell_product(self, product_name, amount):
        try:
            for product, product_info in self.product_dict.items():
                if product.name == product_name:
                    if amount > product_info['amount']:
                        raise ValueError("We don't have enough products")
                    product_info['amount'] -= amount
                    product_info['income'] += round(amount * product_info['price'], 2)
                    self.income += amount * product_info['price']
        except KeyError:
            print('No products found')
        except ValueError as exc:
            print(exc)

    def get_income(self):
        print(f'Total income: {self.income}')
        return f'Total income: {self.income}'

    def get_all_products(self):
        if self.product_dict == []:
            print('There is no products')
        else:
            print('Info about all products in the Store:')
            for item, product_info in self.product_dict.items():
                print(
                    f"- {item}, price: {product_info['price']}, amount: {product_info['amount']}, income: {product_info['income']}.")

    def get_product_info(self, product_name):
        product_list = []
        try:
            for product, product_info in self.product_dict.items():
                if product_name == product_info['name']:
                    print((product_info['name'], product_info['amount']))
                    product_list.append((product_info['name'], product_info['amount']))
            if product_list == []:
                raise ValueError
        except ValueError:
            print('No products found')


def main():
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 50)
    s.add(p2, 300)
    s.set_discount(identifier='Ramen', percent='25%', identifier_type='name')
    s.sell_product('Ramen', 10)
    s.get_income()
    s.get_all_products()
    s.get_product_info('Ramen')


if __name__ == '__main__':
    main()
