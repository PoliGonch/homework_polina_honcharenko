class Mathematican:

    def square_nums(self, num_list: list[int]) -> list[int]:
        square_list = [i ** 2 for i in num_list]
        return square_list

    def remove_positives(self, num_list: list[int]) -> list[int]:
        negative_numbers = [i for i in num_list if i <= 0]
        return negative_numbers

    def filter_leaps(self, num_list: list[int]) -> list[int]:
        temp_list = list(filter(lambda item: item % 4 == 0, num_list))
        year_list = []
        for year in temp_list:
            if year % 100:
                year_list.append(year)
            elif year % 400 == 0:
                year_list.append(year)
        return year_list


def main():
    m = Mathematican()
    m.square_nums([7, 11, 5, 4])
    m.remove_positives([26, -11, -8, 13, -90])
    m.filter_leaps([2001, 1884, 1995, 2003, 2020, 1600, 1800])


if __name__ == '__main__':
    main()
