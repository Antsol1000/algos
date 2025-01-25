from structures.base import Queue, Stack


class SinglyLinkedNode:

    def __init__(self, item):
        self.item = item
        self.next = None

    def __repr__(self):
        return f"({self.item})"


class ListStack(Stack):

    def size(self):
        return self._size

    def last(self):
        return self._head.item

    def push(self, item):
        self._size += 1
        n = SinglyLinkedNode(item)
        n.next = self._head
        self._head = n

    def pop(self):
        self._size -= 1
        n = self._head
        self._head = self._head.next
        return n.item

    def __init__(self):
        self._head = None
        self._size = 0

    def __repr__(self):
        result = ""
        n = self._head
        while n:
            result += f"{n}->"
            n = n.next
        return result.rstrip("->")


class ListQueue(Queue):

    def size(self):
        return self._size

    def first(self):
        return self._head.item

    def push(self, item):
        self._size += 1
        n = SinglyLinkedNode(item)
        if self._head is None:
            self._head = self._tail = n
        else:
            self._tail.next = n
            self._tail = n

    def pop_first(self):
        self._size -= 1
        n = self._head
        self._head = self._head.next
        return n.item

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        result = ""
        n = self._head
        while n:
            result += f"{n}->"
            n = n.next
        return result.rstrip("->")


if __name__ == '__main__':
    q: Stack = ListStack()
    for i in range(10):
        q.push(i)
    print(q)
    assert q.size() == 10
    for i in range(10, 0, -1):
        assert q.pop() == i - 1
    assert q.size() == 0

    q: Queue = ListQueue()
    for i in range(10):
        q.push(i)
    print(q)
    assert q.size() == 10
    for i in range(10):
        assert q.pop_first() == i
    assert q.size() == 0
