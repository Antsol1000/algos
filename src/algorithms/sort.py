import random

from structures.priorityqueue import BinaryHeap


def bubble_sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def insertion_sort(A):
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
        i += 1


def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[min_index], A[i] = A[i], A[min_index]


def merge_sort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        _merge(A, left, mid, right)


def _merge(A, left, mid, right):
    left_part, right_part = A[left:mid + 1], A[mid + 1:right + 1]
    i = j = 0
    for k in range(left, right + 1):
        if i < len(left_part) and (j >= len(right_part) or left_part[i] <= right_part[j]):
            A[k] = left_part[i]
            i += 1
        else:
            A[k] = right_part[j]
            j += 1


def quick_sort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left < right:
        pivot = _partition(A, left, right)
        quick_sort(A, left, pivot - 1)
        quick_sort(A, pivot + 1, right)


def _partition(A, left, right):
    pivot = A[right]
    i = left
    for j in range(left, right):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i


def heap_sort(A):
    bh = BinaryHeap.heapify(A.copy())
    i = 0
    while not bh.is_empty():
        A[i] = bh.pop()
        i += 1


if __name__ == '__main__':
    a = list(range(0, 6))
    random.shuffle(a)
    for sort in [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort]:
        print("Testing", sort.__name__)
        a_copy = a.copy()
        sort(a_copy)
        assert a_copy == sorted(a)
