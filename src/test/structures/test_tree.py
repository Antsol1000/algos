import random
import sys
import time

from structures.tree import BinarySearchTree, RedBlackTree, AVLTree, SplayTree


def create_trees():
    return [BinarySearchTree(), RedBlackTree(), AVLTree(), SplayTree()]


def test_trees():
    for size in range(1, 101):
        print(f"Test {size}")
        trees = create_trees()

        x = list(range(size))
        random.shuffle(x)

        print("Adds")
        for t in trees:
            print("Verifying", t.get_name())
            verify_adds(t, size, x)

        random.shuffle(x)

        print("Deletes")
        for t in trees:
            print("Verifying", t.get_name())
            verify_deletes(t, size, x)


def test_performance_worst_case():
    sys.setrecursionlimit(10_000)
    numbers = list(range(5_000))
    trees = create_trees()

    verify_performance(trees, numbers, "add", add_all)
    verify_performance(trees, numbers, "contains_single", lambda t, _: find_single(t, max(numbers)))
    verify_performance(trees, numbers, "contains_random", find_random)
    verify_performance(trees, numbers, "delete", lambda t, _: delete_all(t, numbers[::-1]))


def test_performance_random():
    numbers = list(range(5_000))
    random.shuffle(numbers)
    trees = create_trees()

    verify_performance(trees, numbers, "add", add_all)
    verify_performance(trees, numbers, "contains_single", lambda t, _: find_single(t, max(numbers)))
    verify_performance(trees, numbers, "contains_random", find_random)
    random.shuffle(numbers)
    verify_performance(trees, numbers, "delete", delete_all)


def verify_adds(bst, size, x):
    for i, xx in enumerate(x):
        bst.insert(xx)
        for j in range(size):
            assert bst.contains(x[j]) == (j <= i)
        assert list(bst) == sorted(x[:i + 1])


def verify_deletes(bst, size, x):
    for i, xx in enumerate(x):
        bst.remove(xx)
        for j in range(size):
            if bst.contains(x[j]) != (j > i):
                print(1)
            assert bst.contains(x[j]) == (j > i)
        assert list(bst) == sorted(x[i + 1:])


def add_all(tree, numbers):
    for n in numbers:
        tree.insert(n)


def delete_all(tree, numbers):
    for n in numbers:
        tree.remove(n)


def find_single(tree, number):
    for _ in range(10_000):
        tree.contains(number)


def find_random(tree, numbers):
    for n in numbers:
        tree.contains(n)


def verify_performance(trees, numbers, name, fn):
    for t in trees:
        print()
        print(f"Testing {name}", t.get_name())
        start_time = time.time()
        fn(t, numbers)
        end_time = time.time()
        print(f"Done in {end_time - start_time:.3f}s")
    print("-" * 80)
