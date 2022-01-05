def check_answer(result: int, answer: int) -> None:
    if result == answer:
        print('This is correct!')
    else:
        print('Try again')


def main():
    math_expression = '3+2'
    result = eval(math_expression)
    answer = int(input(f'What is your answear for {math_expression}? Put it here:\n'))
    check_answer(result=result, answer=answer)


if __name__ == '__main__':
    main()
