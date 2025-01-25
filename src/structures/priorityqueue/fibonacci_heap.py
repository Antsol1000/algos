import math

from structures.priorityqueue.priority_queue import PriorityQueue


class FibonacciHeap(PriorityQueue):

    def __init__(self):
        self.root = None
        self.total_nodes = 0

    class _Node:
        def __init__(self, item):
            self.item = item
            self.degree = 0
            self.marked = False
            self.parent = self.child = None
            self.left = self.right = self

        def __repr__(self):
            return str(self.item)

        def push_child(self, n):
            if self.child is None:
                self.child = n
            else:
                n.left = self.child
                n.right = self.child.right
                self.child.right.left = n
                self.child.right = n
            n.parent = self
            self.degree += 1

        def get_neighbors(self):
            result = [self]
            n = self.right
            while n != self:
                result.append(n)
                n = n.right
            return result

    def is_empty(self):
        return self.root is None

    def top(self):
        return self.root.item

    def push(self, item):
        n = self._Node(item)
        if self.root is None:
            self.root = n
        else:
            n.left = self.root
            n.right = self.root.right
            self.root.right.left = n
            self.root.right = n
            if item < self.root.item:
                self.root = n
        self.total_nodes += 1

    def pop(self):
        n = self.root
        if n is not None:
            self.total_nodes -= 1
            if n.child is not None:
                for child in n.child.get_neighbors():
                    self._add_to_roots(child)
                    child.parent = None

            self._remove_from_roots(n)
            if n == n.right:
                self.root = None
            else:
                self.root = n.right
                self._consolidate()

        return n.item

    def _add_to_roots(self, n):
        if self.root is None:
            self.root = n
        else:
            n.left = self.root
            n.right = self.root.right
            self.root.right.left = n
            self.root.right = n

    def _remove_from_roots(self, n):
        if n == self.root:
            self.root = n.right
        n.left.right = n.right
        n.right.left = n.left

    def _consolidate(self):
        max_degree = int(math.log2(self.total_nodes)) + 2
        arr = [None] * max_degree

        for node in self.root.get_neighbors():
            d = node.degree
            if d >= len(arr):
                print(1)
            while arr[d] is not None:
                y = arr[d]
                if node.item > y.item:
                    node, y = y, node
                self._link(node, y)
                arr[d] = None
                d += 1
            arr[d] = node

        self.root = None
        for a in arr:
            if a is not None:
                if self.root is None:
                    self.root = a
                    self.root.left = self.root.right = self.root
                    self.root.parent = None
                else:
                    self._add_to_roots(a)
                    if self.root.item > a.item:
                        self.root = a

    def _link(self, x, y):
        self._remove_from_roots(y)
        y.left = y.right = y
        y.mark = False
        x.push_child(y)
