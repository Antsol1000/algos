from structures.base import Deque
from structures.list.singly_linked_list import SinglyLinkedNode


class DoublyLinkedNode(SinglyLinkedNode):

    def __init__(self, item):
        super().__init__(item)
        self.prev = None


class LinkedList(Deque):

    def size(self):
        return self._size

    def first(self):
        return self._head.item

    def last(self):
        return self._tail.item

    def push(self, item):
        self._size += 1
        n = DoublyLinkedNode(item)
        if self._head is None:
            self._head = self._tail = n
        else:
            n.prev = self._tail
            self._tail.next = n
            self._tail = n

    def push_first(self, item):
        self._size += 1
        n = DoublyLinkedNode(item)
        if self._head is None:
            self._head = self._tail = n
        else:
            n.next = self._head
            self._head.prev = n
            self._head = n

    def pop(self):
        self._size -= 1
        n = self._tail
        self._tail = self._tail.prev
        if self._tail is not None:
            self._tail.next = None
        return n.item

    def pop_first(self):
        self._size -= 1
        n = self._head
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return n.item

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __iter__(self):
        n = self._head
        while n:
            yield n
            n = n.next

    def __reversed__(self):
        n = self._tail
        while n:
            yield n
            n = n.prev

    def __repr__(self):
        return "<->".join(str(item) for item in self)


if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.push_first(i)
        l.push(i)
        l.push(i)
        assert l.pop_first() == i
        assert l.pop() == i
    print(l)
    assert l.size() == 10
    assert [n.item for n in l] == list((range(10)))
    assert [n.item for n in reversed(l)] == list(reversed(range(10)))
    for i in range(10):
        assert l.pop_first() == i
