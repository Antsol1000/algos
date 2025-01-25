import random
import time
from copy import copy

from structures.priorityqueue import BinaryHeap, BinomialHeap, FibonacciHeap


def create_queues():
    return [BinaryHeap(), BinomialHeap(), FibonacciHeap()]


def test_priority_queues():
    for t in range(1, 101):
        print(f"Test {t}")
        numbers = list(range(t))
        random.shuffle(numbers)

        for q in create_queues():
            print(f"Testing {q.__class__.__name__}")
            n = copy(numbers)
            for i in n:
                q.push(i)
            t = []
            while not q.is_empty():
                x, y = q.top(), q.pop()
                assert x == y
                t.append(x)
            assert t == sorted(numbers)


def test_performance():
    numbers = list(range(10_000))
    random.shuffle(numbers)
    queues = create_queues()

    verify_performance(queues, numbers, "push", pushes)
    verify_performance(queues, numbers, "pop", pops)


def verify_performance(queues, numbers, name, fn):
    for q in queues:
        print()
        print(f"Testing {name}", q.__class__.__name__)
        start_time = time.time()
        fn(q, numbers)
        end_time = time.time()
        print(f"Done in {end_time - start_time:.3f}s")
    print("-" * 80)


def pushes(q, numbers):
    for i in numbers:
        q.push(i)


def pops(q, numbers):
    for _ in numbers:
        q.pop()
