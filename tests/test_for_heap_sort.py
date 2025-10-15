from hypothesis import given
import hypothesis.strategies
from src.heap_sort import heap_sort

"""Обычные случаи"""


def test_heap_sort_usual_occasions():
    assert heap_sort([29, 32, 54, 11, 9]) == [9, 11, 29, 32, 54]
    assert heap_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]


def test_heap_sort_empty_list():
    assert heap_sort([]) == []


def test_heap_sort_one_element():
    assert heap_sort([1]) == [1]


def test_heap_sort_reverse_order():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_heap_sort_sorted_input():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


"""Крайние случаи"""


def test_heap_sort_double_pairs():
    assert heap_sort([5, 3, 4, 4, 3, 5]) == [3, 3, 4, 4, 5, 5]


def test_heap_sort_negative_numbers():
    assert heap_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


def test_heap_sort_negative_with_positive():
    assert heap_sort([-1, 2, -3, 4, -5]) == [-5, -3, -1, 2, 4]


def test_heap_sort_one_nuber_list():
    assert heap_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]


def test_heap_sort_very_big_reversed_array():
    assert heap_sort([i for i in range(100000, 0, -1)]) == [i for i in range(1, 100001)]


"""Property based tests"""


@given(hypothesis.strategies.lists(hypothesis.strategies.integers()))
def test_any_array_whether_it_is_sorted(arr):
    result = heap_sort(arr)
    assert result == sorted(arr)


@given(hypothesis.strategies.lists(hypothesis.strategies.integers()))
def test_if_all_elements_are_there(arr):
    assert all(i in arr for i in heap_sort(arr)) == True


@given(hypothesis.strategies.lists(hypothesis.strategies.integers()))
def test_len(arr):
    assert len(arr) == len(heap_sort(arr))


@given(hypothesis.strategies.lists(hypothesis.strategies.integers()))
def test_ascending_order(arr):
    result = heap_sort(arr)
    assert all((result[i] <= result[i + 1]) for i in range(len(result) - 1))
