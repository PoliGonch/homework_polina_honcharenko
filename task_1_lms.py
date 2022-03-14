import re
from string import ascii_letters, digits


class Authorization:

    def __init__(self, email):
        self._email = None
        self.validate(email)

    @classmethod
    def validate(cls, email):
        # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        printable_characters = "+-_."
        allowed_chars_left = ascii_letters + digits + printable_characters
        allowed_chars_right = ascii_letters + digits + '-'

        match = re.search('@', email)
        if match is None:
            raise ValueError('Wrong email 1')

        try:
            left, right = email.split('@')
            right_start, right_end = right.split('.', 1)
        except ValueError:
            print('Wrong email 2')
            raise

        if left[0] in printable_characters or left[0] == ' ':
            raise ValueError('Wrong email 3')

        if left[-1] in printable_characters or left[-1] == ' ':
            raise ValueError('Wrong email 3')

        for char in left:
            if char not in allowed_chars_left:
                raise ValueError('Wrong email 4')

        for char in right_start:
            if char not in allowed_chars_right:
                raise ValueError('Wrong email 5')

        if len(right_end) < 2:
            raise ValueError('Wrong email 6')

        for char in right_end:
            if char not in ascii_letters and char != '.':
                raise ValueError('Wrong email 7')
            if char == '.' and right_end.find(char) > len(right_end) - 3:
                raise ValueError('Wrong email 8')

        # temp_list = list(left)
        #
        # if temp_list[0] in [' ', punctuation]:
        #     raise ValueError('Wrong email 2')
        # if temp_list[-1] in [' ', punctuation]:
        #     raise ValueError('Wrong email 3')
        #
        # match_left = re.fullmatch(r'[a-zA-Z0-9._%+-]{1,}', left)
        #
        # if match_left is None:
        #     raise ValueError('Wrong email')
        #
        # right_pattern = r'[A-Za-z0-9.-]+\.+[A-Z|a-z]{2,}\b'
        # match_right = re.fullmatch(right_pattern, right)
        # print(match_right)
        #
        # if match_right is None:
        #     raise ValueError('Wrong email')

        cls.get_email = email

    @property
    def get_email(self):
        return self._email

    @get_email.setter
    def get_email(self, email):
        self._email = email

    @get_email.deleter
    def get_email(self):
        del self._email


def main():
    b = Authorization
    d = Authorization('foo_23@example.com.ua')
    print(d.get_email)


if __name__ == '__main__':
    main()

# print(re.fullmatch(r'[\w\d]+\s\d+', 'Super 205'))
# print(re.fullmatch(r'[a-zA-Z0-9._%+-]{1,}', 'foo_23'))
# email = 'no-reply@pythontutorial.net'
# print(re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', 'no-reply@pythontutorial.net'))
