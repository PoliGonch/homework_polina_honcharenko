class CustomException(Exception):

    def __init__(self, msg):
        self.msg = str(msg)
        with open('logs.txt', 'a') as log_file:
            log_file.write(f'{self.msg}\n')


def main():
    raise CustomException("test exc")


if __name__ == '__main__':
    main()
