from structures.hashtable.base import HashTable


class SeparateChainingHashTable(HashTable):

    def __init__(self, capacity=16, load_factor=0.75):
        super().__init__(capacity)
        self._load_factor = load_factor
        self._table = [None] * capacity

    def get(self, key):
        index = self._hash(key)
        node = self._table[index]
        if node:
            for n in node:
                if n.key == key:
                    return n.value
        return None

    def insert(self, key, value):
        n = self._Node(key, value)
        index = self._hash(key)
        if self._table[index]:
            n.next = self._table[index]
        self._table[index] = n

        self._size += 1
        if self._size > self._capacity * self._load_factor:
            self._resize()

    def remove(self, key):
        index = self._hash(key)
        n = self._table[index]
        if n:
            if n.key == key:
                self._table[index] = n.next
                self._size -= 1
            while n.next:
                if n.next.key == key:
                    n.next = n.next.next
                    self._size -= 1

    class _Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

        def __iter__(self):
            n = self
            while n:
                yield n
                n = n.next

    def _resize(self):
        # TODO: resize
        pass


if __name__ == '__main__':
    ht: HashTable = SeparateChainingHashTable(capacity=64)
    keys = list(range(32))
    values = list(range(32))
    for n in zip(keys, values):
        ht.insert(n[0], n[1])
    for n in keys:
        assert ht.contains(n)
    for n in zip(keys, values):
        assert ht.get(n[0]) == n[1]
    assert ht.size() == 32
    for n in keys[::2]:
        ht.remove(n)
    for n in keys[::2]:
        assert not ht.contains(n)
    for n in keys[1::2]:
        assert ht.contains(n)
