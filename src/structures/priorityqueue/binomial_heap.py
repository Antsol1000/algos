from typing import List

from structures.priorityqueue.priority_queue import PriorityQueue


class BinomialTree:

    def __init__(self, item):
        self.item = item
        self.children = []
        self.degree = 0

    def __repr__(self):
        if self.degree == 0:
            return f"({self.item})"
        return f"({self.item}-> {', '.join([str(x) for x in self.children])})"

    @staticmethod
    def merge(tree1, tree2):
        if tree1.degree != tree2.degree:
            raise ValueError("Cannot merge trees of different degrees!")
        if tree1.item > tree2.item:
            tree1, tree2 = tree2, tree1

        tree1.children = [tree2] + tree1.children
        tree1.degree += 1
        return tree1


class BinomialHeap(PriorityQueue):

    def __init__(self):
        self.root = None

    def __repr__(self):
        n = self.root
        result = "Heap:\n"
        while n:
            result += f"{n.tree}\n"
            n = n.next
        return result

    class _Node:

        def __init__(self, x):
            if not isinstance(x, BinomialTree):
                x = BinomialTree(x)
            self.tree = x
            self.next = None

        def __repr__(self):
            return str(self.tree)

    def is_empty(self):
        return self.root is None

    def top(self):
        return self._find_min().tree.item

    def push(self, item):
        if self.is_empty():
            self.root = self._Node(item)
        else:
            self._meld(BinomialHeap._create([BinomialTree(item)]))

    def pop(self):
        min_n = self._find_min()
        if min_n == self.root:
            self.root = self.root.next
        else:
            n = self.root
            while n.next != min_n:
                n = n.next
            n.next = min_n.next

        result = min_n.tree.item
        if min_n.tree.degree > 0:
            self._meld(BinomialHeap._create(min_n.tree.children))
        return result

    def _meld(self, h2):
        t1, t2 = self.root, h2.root
        if not t1 or t1.tree.degree > t2.tree.degree:
            t1, t2 = t2, t1
        n = t1
        t1 = t1.next
        new_root = n
        while t1 and t2:
            if t1.tree.degree <= t2.tree.degree:
                n.next = t1
                t1 = t1.next
            else:
                n.next = t2
                t2 = t2.next
            n = n.next

        if t1:
            n.next = t1
        if t2:
            n.next = t2

        self.root = new_root
        if self.root:
            n = self.root
            while n.next:
                nn = n.next
                if n.tree.degree == nn.tree.degree:
                    nnn = nn.next
                    n.tree = BinomialTree.merge(n.tree, n.next.tree)
                    n.next = nnn
                else:
                    n = n.next

    def _find_min(self):
        n, min_n = self.root, self.root
        while n:
            if n.tree.item < min_n.tree.item:
                min_n = n
            n = n.next
        return min_n

    @staticmethod
    def _create(trees: List[BinomialTree]):
        h = BinomialHeap()
        h.root = BinomialHeap._Node(trees[0])
        for tree in trees[1:]:
            n = BinomialHeap._Node(tree)
            n.next = h.root
            h.root = n
        return h


if __name__ == '__main__':
    import random

    numbers = list(range(120))
    random.shuffle(numbers)
    print(numbers)

    pq = BinomialHeap()
    for n in numbers:
        pq.push(n)
    print(pq)
    t1, t2 = [], []
    while not pq.is_empty():
        t1.append(pq.top())
        t2.append(pq.pop())

    assert t1 == sorted(numbers)
    assert t2 == sorted(numbers)
