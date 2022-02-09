# Extend UnorderedList
#
# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`, and return a copy
# of the list starting at the position and going up to but not including the stop position.

from typing import TypeAlias

from node import Node

ItemType: TypeAlias = int


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self) -> bool:
        return self._head is None

    def add(self, item: ItemType) -> None:
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self) -> int:
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def is_exist(self, item: ItemType) -> bool:
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item: ItemType) -> bool:
        current = self._head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                if previous is None:
                    self._head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current
                current = current.get_next()
        return found

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

    def append(self, item: ItemType) -> None:
        temp = Node(item)

        if self._head is None:
            self._head = temp

        current = self._head
        while current.get_next():
            current = current.get_next()
        current.set_next(temp)

    def pop(self):
        previous = None

        if self._head is None:
            return 'No items found'

        current = self._head
        while current.get_next():
            previous = current
            current = current.get_next()
        if previous is None:
            self._head = None
        else:
            previous.set_next(None)

    def insert(self, index: int, item: ItemType) -> bool:
        temp = Node(item)
        current = self._head
        previous = None
        pos = 0

        if current is None or index == 0:
            temp.set_next(self._head)
            self._head = temp
            return True

        while pos < index and current is not None:
            previous = current
            current = current.get_next()
            pos += 1

        if current is None:
            previous.set_next(temp)
            return True

        temp.set_next(current)
        previous.set_next(temp)
        return True

    def index(self, item: ItemType) -> int | str:
        current = self._head
        found = False
        index = 0

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                index += 1
                current = current.get_next()

        if found:
            return index
        else:
            return "Not Found"

    def slice(self, start: ItemType, stop: ItemType) -> list[int] | str:
        current = self._head
        index = 0
        new_list = []

        while current is not None and index < stop:
            if index >= start:
                new_list.append(current.get_data())
            current = current.get_next()
            index += 1

        if new_list:
            return str(new_list)
        else:
            return "Not Found"


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.add(5)
    # my_list.append(6)
    print(my_list)
    # my_list.pop()
    print(my_list.size())
    my_list.insert(4, 17)
    print(my_list)
    print(my_list.index(17))
    print(my_list.slice(1, 6))
