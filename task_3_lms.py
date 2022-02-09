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
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e):
        try:
            new_element = []
            temp_list = []
            for _ in range(len(self._items)):
                stack_element = self._items.pop()
                # print(stack_element)
                if stack_element == e:
                    new_element.append(stack_element)
                    continue
                temp_list.append(stack_element)
            # print(temp_list)
            for _ in range(len(temp_list)):
                self.push(temp_list.pop())
            if len(new_element) > 0:
                return new_element[0]
            raise ValueError('Element not found')
        except ValueError:
            raise


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e):
        try:
            new_element = []
            iter_len = len(self._items)
            for _ in range(iter_len):
                element = self._items.pop()
                if element == e:
                    new_element.append(element)
                    iter_len += 1
                    continue
                self.enqueue(element)
            if len(new_element) > 0:
                return new_element[0]
            raise ValueError('Element not found')
        except ValueError:
            raise


if __name__ == "__main__":
    # q = Queue()
    # q.enqueue(4)
    # q.enqueue('dog')
    # q.enqueue(True)
    # q.enqueue(5)
    # q.enqueue('Wow')
    # q.enqueue('Star')
    # print(q.size())
    # print(q)
    # print(q.get_from_stack('Wow'))
    # print(q.get_from_stack('Haha'))
    # print(q)

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    print(s.get_from_stack(3))
    print(s.get_from_stack('haha'))
    print(s)
