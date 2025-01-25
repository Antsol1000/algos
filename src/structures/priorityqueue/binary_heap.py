from structures.priorityqueue.priority_queue import PriorityQueue


class BinaryHeap(PriorityQueue):

    def __init__(self):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def top(self):
        return self.heap[0]

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._heapify_down(0)
        return item

    @staticmethod
    def heapify(arr):
        h = BinaryHeap()
        h.heap = list(arr)
        for i in reversed(range(len(arr))):
            h._heapify_up(i)
        return h

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[parent] > self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        l, r = 2 * i + 1, 2 * i + 2
        if l < len(self.heap):
            if r < len(self.heap) and self.heap[r] < self.heap[i] and self.heap[r] < self.heap[l]:
                self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                self._heapify_down(r)
            elif self.heap[l] < self.heap[i]:
                self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                self._heapify_down(l)


if __name__ == '__main__':
    bh = BinaryHeap.heapify([6, 4, 1, 3, 2, 0, 5])
    while not bh.is_empty():
        print(bh.pop())
