class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

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

    def __len__(self):
        return self.size()

    def get_from_stack(self, e):
        stack = Stack()
        try:
            while not self.is_empty():
                stack_element = self.pop()
                if stack_element == e:
                    break
                stack.push(stack_element)
            else:
                raise ValueError('Element not found')

        finally:
            while not stack.is_empty():
                self.push(stack.pop())

        return stack_element


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

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

    def __len__(self):
        return self.size()

    def get_from_queue(self, e):

        temp_queue = Queue()
        queue = Queue()

        while not self.is_empty():
            queue_element = self.dequeue()
            if queue_element == e:
                temp_queue.enqueue(queue_element)
                continue
            queue.enqueue(queue_element)

        while not queue.is_empty():
            self.enqueue(queue.dequeue())

        try:
            if not temp_queue.is_empty():
                return temp_queue.dequeue()
            raise ValueError('Element not found')
        except ValueError:
            raise

# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue('dog')
#     q.enqueue(True)
#     q.enqueue(5)
#     q.enqueue('Wow')
#     q.enqueue('Star')
#     print(q.size())
#     print(q)
#     print(q.get_from_queue('Wow'))
#     # print(q.get_from_queue('Haha'))
#     print(q)
#
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     print(s)
#     print(s.get_from_stack(4))
#     print(s)
# print(s.get_from_stack('haha'))
# print(s)

# @pytest.mark.parametrize(
#     ['input_value', 'searched_value', 'result_value'],
#     [
#         ('12345', '2', '1345'),
#         ('123456789', '6', '12345789'),
#         ('hello', 'e', 'hllo'),
#     ],
# )
#
# def test_normal(input_value, searched_value, result_value):
#     stack = Stack()
#     for item in input_value:
#         stack.push(item)
#
#     found_value = stack.get_from_stack(searched_value)
#
#     result = ''.join(reversed([stack.pop() for _ in range(len(stack))]))
#
#     assert found_value == searched_value
#     assert result == result_value
#
#
# @pytest.mark.parametrize(
#     ['input_value', 'searched_value', ],
#     [
#         ('12345', '6',),
#         ('123456789', 'x',),
#         ('hello', '1',),
#     ],
# )
# def test_exception(input_value, searched_value):
#     stack = Stack()
#     for item in input_value:
#         stack.push(item)
#
#     with pytest.raises(ValueError, match=f'Element not found'):
#         stack.get_from_stack(searched_value)
#
#     result = ''.join(reversed([stack.pop() for _ in range(len(stack))]))
#
#     assert result == input_value
#
#
# @pytest.mark.parametrize(
#     ['input_value', 'searched_value', 'result_value'],
#     [
#         ('12345', '2', '1345'),
#         ('123456789', '6', '12345789'),
#         ('hello', 'e', 'hllo'),
#     ],
# )
# def test_normal(input_value, searched_value, result_value):
#     queue = Queue()
#     for item in input_value:
#         queue.enqueue(item)
#
#     found_value = queue.get_from_queue(searched_value)
#
#     result = ''.join([queue.dequeue() for _ in range(len(queue))])
#
#     assert found_value == searched_value
#     assert result == result_value
#
#
# @pytest.mark.parametrize(
#     ['input_value', 'searched_value', ],
#     [
#         ('12345', '6',),
#         ('123456789', 'x',),
#         ('hello', '1',),
#     ],
# )
# def test_exception(input_value, searched_value):
#     queue = Queue()
#     for item in input_value:
#         queue.enqueue(item)
#
#     with pytest.raises(ValueError, match=f'Element not found'):
#         queue.get_from_queue(searched_value)
#
#     result = ''.join([queue.dequeue() for _ in range(len(queue))])
#
#     assert result == input_value
