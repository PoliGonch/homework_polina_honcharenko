import operator
from typing import Generic, TypeVar, List, Callable

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def parse_exp_to_tokens(math_exp: str) -> list:
    tokens_list = []
    char: str = ''
    for sign in math_exp:
        if not sign.isspace():
            if sign not in ['(', ')']:
                if char == '':
                    char = sign
                else:
                    if char.title() in ['True', 'False']:
                        tokens_list.append(char.title())
                        char = ''
                        char += sign
                    if char.lower() in ['and', 'or', 'not']:
                        tokens_list.append(char.lower())
                        char = ''
                        char += sign
                    else:
                        char = char + sign
            else:
                if char.title() in ['True', 'False']:
                    tokens_list.append(char.title())
                if char.lower() in ['and', 'or', 'not']:
                    tokens_list.append(char.lower())
                tokens_list.append(sign)
                char = ''
        else:
            if char.title() in ['True', 'False']:
                tokens_list.append(char.title())
                char = ''
            if char.lower() in ['and', 'or', 'not']:
                tokens_list.append(char.lower())
                char = ''
            char = ''
    return tokens_list


def normalize_token(token: str):
    token_dict = {'True': True,
                  'False': False}
    return token_dict.get(token, token)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = parse_exp_to_tokens(math_exp)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()


        elif i.lower() in ['and', 'or', 'not']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['and', 'or', 'not']:
            try:
                current_tree.set_root_val(normalize_token(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates: dict[str, Callable] = {'and': operator.and_, 'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    elif left_c:
        return evaluate(left_c)
    elif right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(right_c))
    else:
        # print(parse_tree.get_root_val())
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val += str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    return s_val


if __name__ == "__main__":
    expression = '((TRUE or FALSE) OR Not TRUE )'
    # expression = '(not (not False))'
    pt: BinaryTree = build_parse_tree(expression)
    print(evaluate(pt))
    print(expression)
    # print(print_exp(pt))
