"""
Tests for LLCommonMethods, LLItemsAccessMethods,
SinglyLinkedList and DoublyLinkedList classes.
Almost all methods in SinglyLinkedList and DoublyLinkedList
classes have slightly different implementation, but same purpose,
so most of the tests run both linked list objects at time.
"""
# ll - shortcut for linked list.
import pytest
from algorithms.linked_lists import SinglyLinkedList, DoublyLinkedList


# Values placed in filled linked list on creation.
INITIAL_VALUES = ['Hello', 21, True, (1, 2, 3)]


@pytest.fixture(params=range(-len(INITIAL_VALUES), len(INITIAL_VALUES)))
def in_range_index(request):
    # Set of indexes used to refer to the ll values.
    return request.param


@pytest.fixture(params=[-len(INITIAL_VALUES)-1, len(INITIAL_VALUES)])
def out_of_range_index(request):
    # Set of indexes too small or too big to refer to the ll values.
    return request.param


@pytest.fixture(params=[SinglyLinkedList, DoublyLinkedList])
def empty_ll(request):
    return request.param()


@pytest.fixture
def filled_singly_ll():
    # By default add() method inserts new value in the front of the list,
    # So to build linked list with similar indexing as in iterable argument,
    # It should be passed in class in reversed order.
    return SinglyLinkedList(reversed(INITIAL_VALUES))


@pytest.fixture
def filled_doubly_ll():
    # By default add() method inserts new value in the front of the list,
    # So to build linked list with similar indexing as in iterable argument,
    # It should be passed in class in reversed order.
    return DoublyLinkedList(reversed(INITIAL_VALUES))


@pytest.fixture(params=['filled_singly_ll',
                        'filled_doubly_ll'])
def filled_ll(request):
    return request.getfixturevalue(request.param)


# Tests on LLCommonMethod class.
@pytest.mark.parametrize('ll_class, arg', [
    (SinglyLinkedList, 123),
    (DoublyLinkedList, True),
])
def test_build_linked_list_with_not_iterable_argument(ll_class, arg):
    with pytest.raises(TypeError):
        ll_class(arg)


def test_iter(filled_ll):
    assert [value for value in filled_ll] == INITIAL_VALUES


def test_empty_ll_len(empty_ll):
    assert len(empty_ll) == 0


def test_filled_ll_len(filled_ll):
    assert len(filled_ll) == len(INITIAL_VALUES)


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_contains_true(filled_ll, value):
    assert value in filled_ll


@pytest.mark.parametrize('value', [3, 'word', False])
def test_contains_false(filled_ll, value):
    assert value not in filled_ll


def test_repr_empty_ll(empty_ll):
    assert empty_ll.__repr__() == '«»'


def test_repr_filled_singly_ll(filled_singly_ll):
    correct = '«' + ' --> '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in INITIAL_VALUES]) + '»'
    assert filled_singly_ll.__repr__() == correct


def test_repr_filled_double_ll(filled_doubly_ll):
    correct = '«' + ' <--> '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in INITIAL_VALUES]) + '»'
    assert filled_doubly_ll.__repr__() == correct


# Tests on LLItemsAccessMethods class.
def test_getitem_in_range(filled_ll, in_range_index):
    assert filled_ll[in_range_index] == INITIAL_VALUES[in_range_index]


def test_getitem_out_of_range_raise_error(filled_ll, out_of_range_index):
    with pytest.raises(IndexError):
        non_existing_value = filled_ll[out_of_range_index]


def test_setitem_in_range(filled_ll, in_range_index):
    filled_ll[in_range_index] = 'NEW'
    assert filled_ll[in_range_index] == 'NEW'


def test_setitem_out_of_range_raise_error(filled_ll, out_of_range_index):
    with pytest.raises(IndexError):
        filled_ll[out_of_range_index] = 'NEW'


# Tests on SinglyLinkedList and DoublyLinkedList classes.
def test_add_value_to_empty_ll_updates_first_link(empty_ll):
    empty_ll.add('First value')
    assert empty_ll.first.value == 'First value'


def test_add_value_to_filled_ll(filled_ll):
    filled_ll.add('New value')
    assert len(filled_ll) == len(INITIAL_VALUES) + 1


def test_insert_value_in_empty_ll_updates_first_link(empty_ll):
    empty_ll.insert('First value', 0)
    assert empty_ll.first.value == 'First value'


@pytest.mark.parametrize('index', list(range(0, len(INITIAL_VALUES))))
def test_insert_by_not_negative_index_in_filled_ll(filled_ll, index):
    filled_ll.insert('New value', index)
    assert filled_ll[index] == 'New value'


@pytest.mark.parametrize('index', list(range(-len(INITIAL_VALUES), 0)))
def test_insert_by_negative_index_in_filled_ll(filled_ll, index):
    filled_ll.insert('New value', index)
    assert filled_ll[index-1] == 'New value'


def test_pop_without_index_returns_correct_value(filled_ll):
    assert filled_ll.pop() == INITIAL_VALUES[0]


def test_pop_with_index_returns_correct_value(filled_ll, in_range_index):
    assert filled_ll.pop(in_range_index) == INITIAL_VALUES[in_range_index]


def test_pop_with_out_of_range_index_raise_error(filled_ll, out_of_range_index):
    with pytest.raises(IndexError):
        filled_ll.pop(out_of_range_index)


def test_first_link_switches_after_pop_first_value(filled_ll):
    filled_ll.pop()
    assert filled_ll.first.value == INITIAL_VALUES[1]


def test_last_link_switches_after_pop_last_value(filled_doubly_ll):
    filled_doubly_ll.pop(-1)
    assert filled_doubly_ll.last.value == INITIAL_VALUES[-2]


def test_first_link_points_to_none_after_pop_the_only_value(empty_ll):
    empty_ll.add('The one and only')
    empty_ll.pop()
    assert empty_ll.first is None


def test_last_link_points_to_none_after_pop_the_only_value():
    doubly_ll = DoublyLinkedList(['The one and only'])
    doubly_ll.pop()
    assert doubly_ll.last is None


def test_len_decreases_by_1_after_pop(filled_ll, in_range_index):
    filled_ll.pop(in_range_index)
    assert len(filled_ll) == len(INITIAL_VALUES) - 1
