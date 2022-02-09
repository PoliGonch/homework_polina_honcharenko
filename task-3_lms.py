from typing import TypeAlias

from node import Node

ItemType: TypeAlias = int | str


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def enqueue(self, item: ItemType) -> bool:
        temp = Node(item)
        current = self._head

        temp.set_next(self._head)
        self._head = temp
        return True

    def dequeue(self):
        previous = None
        current = self._head

        if self._head is None:
            return 'No items found'

        while current.get_next():
            previous = current
            current = current.get_next()
        if previous is None:
            self._head = None
        else:
            previous.set_next(None)
        return True

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = UnorderedList()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    q.enqueue('Hi!')

    print(q.size())
    print(q)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
