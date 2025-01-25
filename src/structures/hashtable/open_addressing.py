from structures.hashtable.base import HashTable


class OpenAddressingHashTable(HashTable):

    def __init__(self, capacity=16, load_factor=0.66):
        super().__init__(capacity)
        self._load_factor = load_factor
        self._table = [None] * capacity

    def get(self, key):
        i = self._find_slot(key)
        kv = self._table[i]
        if kv:
            return kv[1]
        return None

    def insert(self, key, value):
        i = self._find_slot(key)
        if self._table[i]:
            self._table[i] = (key, value)
            return

        if self._size + 1 > self._capacity * self._load_factor:
            self._resize()
            i = self._find_slot(key)
        self._table[i] = (key, value)
        self._size += 1

    def remove(self, key):
        pass

    def _find_slot(self, key):
        i = self._hash(key)
        while self._table[i] is not None and self._table[i][0] != key:
            i = (i + 1) % self._capacity
        return i

    def _resize(self):
        pass
