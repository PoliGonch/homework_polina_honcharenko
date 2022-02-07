class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for item in self._items:
            representation += f"{str(item)}"
        return representation

    def __str__(self):
        return self.__repr__()


def reverse(input_string: str) -> None:
    stack = Stack()
    for item in input_string:
        stack.push(item)
    while len(stack._items) > 0:
        char = stack.pop()
        print(char)


reverse('Hello')
