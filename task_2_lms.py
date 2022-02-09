from typing import TypeAlias

from node import Node

ItemType: TypeAlias = int


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

    def push(self, item: ItemType) -> bool:
        temp = Node(item)
        previous = None

        if self._head is None:
            self._head = temp

        current = self._head
        while current is not None:
            previous = current
            current = current.get_next()
        previous.set_next(temp)
        temp.set_next(current)
        return True

    def pop(self) -> bool | str:
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
    my_list = UnorderedList()

    my_list.push(1)
    my_list.push(2)
    my_list.push(3)
    my_list.push(4)
    my_list.push(5)
    print(my_list)
    my_list.pop()
    print(my_list)
