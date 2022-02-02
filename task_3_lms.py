def nsd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction
        try:
            self.top, self.bottom = self.find_top_and_bottom(fraction)
            if self.bottom == 0:
                raise ZeroDivisionError('You can not divide by zero')
        except ValueError as exc:
            print('Give me fraction with / division sign')
            raise
        except TypeError as exc:
            print('Wrong type')
            raise
        except Exception as exc:
            print(exc)
            raise

    def __str__(self):
        return f'Fraction({self.top}/{self.bottom})'

    def find_top_and_bottom(self, fraction):
        try:
            temp_list = fraction.split('/')
            top = int(temp_list[0])
            bottom = int(temp_list[1])
            if top is None and bottom is None:
                raise ValueError('Wrong division sign')
            return top, bottom
        except ValueError as exc:
            print(exc)
            raise
        except TypeError as exc:
            raise
            # sys.exit('Wrong division sign')

    def check_type(self, other):
        if not isinstance(other, Fraction):
            raise TypeError('Wrong type')

    def __add__(self, other):
        try:
            self.check_type(other)
            new_top = self.top * other.bottom + other.top * self.bottom
            new_bottom = self.bottom * other.bottom
            common = nsd(new_top, new_bottom)
            new_num = str(new_top // common) + '/' + str(new_bottom // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __sub__(self, other):
        try:
            self.check_type(other)
            new_top = self.top * other.bottom - other.top * self.bottom
            new_bottom = self.bottom * other.bottom
            common = nsd(new_top, new_bottom)
            new_num = str(new_top // common) + '/' + str(new_bottom // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __mul__(self, other):
        try:
            self.check_type(other)
            new_top = self.top * other.top
            new_bottom = self.bottom * other.bottom
            common = nsd(new_top, new_bottom)
            new_num = str(new_top // common) + '/' + str(new_bottom // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)

    def __truediv__(self, other):
        try:
            self.check_type(other)
            new_top = self.top * other.bottom
            new_bottom = self.bottom * other.top
            common = nsd(new_top, new_bottom)
            new_num = str(new_top // common) + '/' + str(new_bottom // common)
            return Fraction(new_num)
        except TypeError:
            print('Wrong type')
        except ValueError as exc:
            print(exc)


def main():
    x = Fraction('1/2')
    y = Fraction('1/4')
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)


if __name__ == '__main__':
    main()

# def find_top(self, fraction):
#     self._temp_fraction = list(''.join(fraction))
#     top = []
#
#     while self._temp_fraction:
#         if self._temp_fraction[0] == '/':
#             break
#         top.append(self._temp_fraction[0])
#         self._temp_fraction.remove(self._temp_fraction[0])
#     return int(''.join(top))
#
#
# def find_bottom(self, fraction):
#     bottom = [char for char in fraction if char != '/']
#     return int(''.join(bottom))
