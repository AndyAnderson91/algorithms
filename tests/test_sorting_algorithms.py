"""
Tests for sorting algorithms.
All functions have identical input and output,
so same tests are used for all functions.
"""
import pytest
from algorithms.sorting_algorithms import *


@pytest.fixture(params=[
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
])
def sorting_function(request):
    return request.param


@pytest.mark.parametrize('array', [
    [],
    [3],
    [1, 2],
    [0, 9, 0],
    [3, 0, 5, 5],
    [1, 4, 3, 2, 0],
    [7, -5, 3, 1, 8, 3],
    ['ah', 'ak', 'abc', 'a'],
    [9, -4, -3, 0, 12, 2, 7, 5, -3],
    [5, 2, 1, 0, 12, 4, -3, -2, 18, -14, 1]
])
def test_sorting_function(sorting_function, array):
    sorting_function(array)
    assert array == sorted(array)
