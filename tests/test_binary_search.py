"""
Tests on binary search functions.
Both implementations have identical input and output,
so same tests are used for both functions.
"""
import pytest
from binary_search import binary_search_iterative, binary_search_recursive


@pytest.fixture(params=[binary_search_iterative, binary_search_recursive])
def binary_search_function(request):
    return request.param


@pytest.mark.parametrize('array, value', [
    ([2], 2),
    ([1, 4], 1),
    ([1, 4], 4),
    ([2, 3, 7], 2),
    ([2, 3, 7], 3),
    ([2, 3, 7], 7),
    ([0, 4, 5, 9], 0),
    ([0, 4, 5, 9], 4),
    ([0, 4, 5, 9], 5),
    ([0, 4, 5, 9], 9),
    ([3, 12, 14, 15, 19], 15),
    ([-4, -1, 0, 2, 6, 9, 11, 13], -4)
])
def test_value_in_list(binary_search_function, array, value):
    assert binary_search_function(array, value) == array.index(value)


@pytest.mark.parametrize('array, value', [
    ([], 3),
    ([2, 9], 0),
    ([2, 9], 4),
    ([2, 9], 14),
    ([1, 5, 7], -2),
    ([1, 5, 7], 3),
    ([1, 5, 7], 6),
    ([1, 5, 7], 12),
    ([-4, -3, 16, 20, 25, 36], 37),
    ([4, 8, 9, 11, 12, 32, 41, 65], 7)
])
def test_value_not_in_list(binary_search_function, array, value):
    assert binary_search_function(array, value) is None
