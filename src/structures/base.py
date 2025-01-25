import abc


class Stack(abc.ABC):

    def size(self) -> int:
        pass

    def last(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass


class Queue(abc.ABC):

    def size(self):
        pass

    def first(self):
        pass

    def push(self, item):
        pass

    def pop_first(self):
        pass


class Deque(Queue, Stack):

    def push_first(self, item):
        pass


class SetOperations(abc.ABC):

    def size(self):
        pass

    def contains(self, key):
        pass

    def insert(self, key):
        pass

    def remove(self, key):
        pass


class MapOperations(abc.ABC):

    def size(self):
        pass

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        pass

    def insert(self, key, value):
        pass

    def remove(self, key):
        pass
