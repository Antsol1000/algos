from structures.base import MapOperations


class HashTable(MapOperations):

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity

    def _hash(self, key):
        return hash(key) % self._capacity
