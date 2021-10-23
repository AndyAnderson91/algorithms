"""
Tests for Stack and Queue classes.
Inherited methods are tested in 'test_linked_lists' module.
"""

import pytest
from algorithms.stack_and_queue import Stack, Queue


# Constants.

INITIAL_VALUES = ['Hello', 21, True, (1, 2, 3)]


# Local fixtures.

@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def filled_stack():
    return Stack(INITIAL_VALUES)


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def filled_queue():
    return Queue(INITIAL_VALUES)


# Stack tests.

def test_create_empty_stack():
    assert Stack().top is None


def test_create_stack_with_values():
    assert Stack(INITIAL_VALUES).top.value == INITIAL_VALUES[-1]


def test_stack_length(filled_stack):
    assert filled_stack._length == len(INITIAL_VALUES)


def test_stack_iter(filled_stack):
    values = []
    for value in filled_stack:
        values.append(value)
    assert values == list(reversed(INITIAL_VALUES))


def test_stack_repr(filled_stack):
    correct = '«' + ' -- '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in INITIAL_VALUES]) + '»'
    assert filled_stack.__repr__() == correct


def test_last_pushed_to_stack_value_becomes_top(filled_stack):
    filled_stack.push('Last value')
    assert filled_stack.top.value == 'Last value'


def test_push_value_to_stack_increase_length(filled_stack):
    filled_stack.push('Last value')
    assert filled_stack._length == len(INITIAL_VALUES) + 1


def test_pop_return_last_value_from_stack(filled_stack):
    assert filled_stack.pop() == INITIAL_VALUES[-1]


def test_pop_decrease_length_of_stack(filled_stack):
    filled_stack.pop()
    assert filled_stack._length == len(INITIAL_VALUES) - 1


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_pop_the_only_element_from_stack_redirects_top_link_to_none(value):
    single_element_stack = Stack([value])
    single_element_stack.pop()
    assert single_element_stack.top is None


def test_pop_from_empty_stack_raise_error(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_stack_is_empty_true(empty_stack):
    assert empty_stack.is_empty()


def test_stack_is_empty_false(filled_stack):
    assert not filled_stack.is_empty()


def test_peek_return_none_from_empty_stack(empty_stack):
    assert empty_stack.peek() is None


def test_peek_return_top_value_of_stack(filled_stack):
    assert filled_stack.peek() == INITIAL_VALUES[-1]


# Queue tests.

def test_create_empty_queue():
    assert Queue()._length == 0


def test_create_queue_with_values():
    assert Queue(INITIAL_VALUES)._length == len(INITIAL_VALUES)


def test_first_link_in_queue(filled_queue):
    assert filled_queue.first.value == INITIAL_VALUES[0]


def test_last_link_in_queue(filled_queue):
    assert filled_queue.last.value == INITIAL_VALUES[-1]


def test_queue_repr(filled_queue):
    correct = '«' + ' <-- '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in INITIAL_VALUES]) + '»'
    assert filled_queue.__repr__() == correct


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_first_enqueued_value_becomes_first(empty_queue, value):
    empty_queue.enqueue(value)
    assert empty_queue.first.value == value


def test_enqueued_value_always_becomes_last(filled_queue):
    filled_queue.enqueue('Last value')
    assert filled_queue.last.value == 'Last value'


def test_enqueue_increase_length(filled_queue):
    filled_queue.enqueue('Last value')
    assert filled_queue._length == len(INITIAL_VALUES) + 1


def test_dequeue_return_first_value(filled_queue):
    assert filled_queue.dequeue() == INITIAL_VALUES[0]


def test_first_link_redirect_to_next_value_after_dequeue(filled_queue):
    filled_queue.dequeue()
    assert filled_queue.first.value == INITIAL_VALUES[1]


def test_last_link_redirect_to_none_after_dequeue_the_only_value_in_queue(empty_queue):
    empty_queue.enqueue('The one and only')
    empty_queue.dequeue()
    assert empty_queue.last is None


def test_dequeue_decrease_length(filled_queue):
    filled_queue.dequeue()
    assert filled_queue._length == len(INITIAL_VALUES) - 1


def test_dequeue_from_empty_queue_raise_error(empty_queue):
    with pytest.raises(IndexError):
        empty_queue.dequeue()


def test_queue_is_empty_true(empty_queue):
    assert empty_queue.is_empty()


def test_queue_is_empty_false(filled_queue):
    assert not filled_queue.is_empty()


def test_front_return_first_value_in_queue(filled_queue):
    assert filled_queue.front() == INITIAL_VALUES[0]


def test_front_return_none_from_empty_queue(empty_queue):
    assert empty_queue.front() is None


def test_rear_return_last_value_of_queue(filled_queue):
    assert filled_queue.rear() == INITIAL_VALUES[-1]


def test_rear_return_none_from_empty_queue(empty_queue):
    assert empty_queue.rear() is None
