from structures.base import Stack, Deque


class ArrayListBase:

    def size(self):
        return self._size

    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def __repr__(self):
        return f"{[x for x in self._array if x is not None]}"


class ArrayStack(ArrayListBase, Stack):

    def last(self):
        return self._array[self._size - 1]

    def push(self, item):
        if self._size == self._capacity:
            raise Exception("stack overflow")
        self._array[self._size] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Exception("empty stack")
        self._size -= 1
        item = self._array[self._size]
        self._array[self._size] = None
        return item

    def __init__(self, capacity):
        super().__init__(capacity)


class Buffer(ArrayListBase, Deque):

    def first(self):
        return self._array[self._head]

    def last(self):
        return self._array[self._tail]

    def push(self, item):
        if self._size == self._capacity:
            raise Exception("buffer overflow")
        self._tail = (self._tail + 1) % self._capacity
        self._array[self._tail] = item
        self._size += 1

    def push_first(self, item):
        if self._size == self._capacity:
            raise Exception("buffer overflow")
        self._head = (self._head - 1) % self._capacity
        self._array[self._head] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Exception("empty buffer")
        self._tail = (self._tail - 1) % self._capacity
        item = self._array[self._tail]
        self._array[self._tail] = None
        self._size -= 1
        return item

    def pop_first(self):
        if self._size == 0:
            raise Exception("empty buffer")
        item = self._array[self._head]
        self._array[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def __init__(self, capacity):
        super().__init__(capacity)
        self._head = self._tail = 0


if __name__ == '__main__':
    q: Stack = ArrayStack(10)
    for i in range(10):
        q.push(i)
    print(q)
    assert q.size() == 10
    for i in range(10, 0, -1):
        assert q.pop() == i - 1
    assert q.size() == 0

    q: Deque = Buffer(10)
    for i in range(9):
        q.push(2*i)
        q.push(2*i+1)
        q.pop_first()
    print(q)
    assert q.size() == 9
    for i in range(16, 7, -1):
        assert q.pop() == i
    assert q.size() == 0
