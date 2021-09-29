"""
Tests for sorting algorithms.
"""
import pytest
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort


# Constants

SEQUENCES = [
    # Using tuples to keep base sequences unsorted.
    (),
    (3, ),
    (1, 2),
    (0, 9, 0),
    (3, 0, 5, 5),
    (1, 4, 3, 2, 0),
    (7, -5, 3, 1, 8, 3),
    ('ah', 'ak', 'abc', 'a'),
    (9, -4, -3, 0, 12, 2, 7, 5, -3),
    (5, 2, 1, 0, 12, 4, -3, -2, 18, -14, 1),
]


# Fixtures

@pytest.fixture(params=[
    bubble_sort,
    selection_sort,
    insertion_sort,
])
def in_place_sorting_function(request):
    return request.param


@pytest.fixture(params=[
    merge_sort,
    quick_sort,
])
def out_of_place_sorting_function(request):
    return request.param


# Tests

@pytest.mark.parametrize('sequence', SEQUENCES)
def test_in_place_sorting_functions(in_place_sorting_function, sequence):
    array = list(sequence)
    in_place_sorting_function(array)
    assert array == sorted(array)


@pytest.mark.parametrize('sequence', SEQUENCES)
def test_out_of_place_sorting_functions(out_of_place_sorting_function, sequence):
    array = list(sequence)
    assert out_of_place_sorting_function(array) == sorted(array)
