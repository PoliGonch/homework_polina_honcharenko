class Author:

    def __init__(self, name: str, country: str, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Author: {self.name}, country: {self.country}, birthday: {self.birthday}, books: {self.books}'

    def __str__(self):
        return f'Author: {self.name}, books: {self.books}'

    def check_type(self, name, year, ):
        if not isinstance(name, str) or not isinstance(year, int):
            raise TypeError('Wrong data type')


class Book:
    book_amount = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'{self.name, self.year, self.author.name}'

    def __str__(self):
        return f'Name: {self.name}, year: {self.year}, author: {self.author.name}'

    # def __str__(self):
    #     for index, item in enumerate(self.name)
    #     return f'Name: {self.name}, year: {self.year}, author: {self.author.name}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.books)

    def check_type(self, name, year, author):
        if isinstance(name, str) and isinstance(year, int) and isinstance(author, Author):
            pass
        else:
            raise TypeError('Wrong data type')

    def new_book(self, name: str, year: int, author: Author) -> Book:
        self.check_type(name=name, year=year, author=author)
        new_book = Book(name=name, year=year, author=author)
        Book.book_amount += 1
        author.books.append(new_book)
        self.books.append(new_book)
        self.authors.append(author)
        return new_book

    def group_by_author(self, author: Author):
        if not isinstance(author, Author):
            raise TypeError('There is no such author')
        try:
            new_book = list(filter(lambda book: book.author == author, self.books))
            if not new_book:
                print(f'No books found for author {author.name}')
            else:
                print(new_book)
                return new_book
        except TypeError as exc:
            print(exc)

    def group_by_year(self, year: int):
        new_book = list(filter(lambda book: book.year == year, self.books))
        if not new_book:
            print(f'No books found by year {year}')
        else:
            print(new_book)
            return new_book


def main():
    arthur = Author(name='Arthur Conan Doyle', country='England', birthday='22.05.1859')

    library_1 = Library('Library 1')
    library_1.new_book(name='A Scandal in Bohemia', year=1891, author=arthur)
    library_1.new_book(name="A Case of Identity", year=1891, author=arthur)

    agatha = Author(name='Agatha Christie', country='England', birthday='15.09.1890')

    library_1.new_book(name='Murder on the Orient Express', year=1933, author=agatha)
    library_1.new_book(name='And Then There Were None', year=1939, author=agatha)
    print(library_1)

    library_1.group_by_author(author=arthur)
    library_1.group_by_author(author=agatha)
    library_1.group_by_year(1933)
    print(Book.book_amount)


if __name__ == '__main__':
    main()
