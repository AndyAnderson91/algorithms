"""
HashTable class tests.
Three tables are used for testing:
1) Empty hash table. Used in several tests
where it doesn't really matter is it filled or not,
or there it should be empty.
2, 3) Hash table with collisions and hash table without collisions.
These two are main testing objects, and almost every single test in this module
runs both of them to ensure all methods works correctly in both cases.
"""

import pytest
from algorithms.hash_table import HashTable


# Constants.

INITIAL_ITEMS = [('one', 1), ('two', 2), ('three', 3)]
INITIAL_KEYS = [item[0] for item in INITIAL_ITEMS]
NON_EXISTING_KEYS = [12, 'abc', True, None]


# Local fixtures.

@pytest.fixture
def empty_table():
    return HashTable()


@pytest.fixture
def filled_table_with_collisions():
    return HashTable(INITIAL_ITEMS, 4)


@pytest.fixture
def filled_table_without_collisions():
    return HashTable(INITIAL_ITEMS, 5)


@pytest.fixture(params=['filled_table_with_collisions',
                        'filled_table_without_collisions'])
def filled_table(request):
    return request.getfixturevalue(request.param)


# Tests.

def test_filled_table_with_collisions(filled_table_with_collisions):
    """Checks if this table has collisions."""
    # Filled cells number is less than items number.
    filled_cells = [cell for cell in filled_table_with_collisions.array if cell is not None]
    assert len(filled_cells) < len(INITIAL_ITEMS)


def test_filled_table_without_collisions(filled_table_without_collisions):
    """Checks if this table doesn't have collisions."""
    # One item per array cell.
    filled_cells = [cell for cell in filled_table_without_collisions.array if cell is not None]
    assert len(filled_cells) == len(INITIAL_ITEMS)


@pytest.mark.parametrize('key', [1, 345, 567821345, 0, -12, 'text', '', (1, 2, 3, 4), (), True, False, None])
def test_hashing_of_hashable_keys(empty_table, key):
    assert isinstance(empty_table._hash(key), int)


@pytest.mark.parametrize('key',
                         [[], [1, 2, 3], {}, {'abc': 123}, set(), {1, 2, 3, 4, 5}])
def test_hashing_of_unhashable_keys_raise_error(empty_table, key):
    with pytest.raises(TypeError):
        empty_table._hash(key)


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_hash_is_lower_than_capacity(empty_table, key):
    assert empty_table._hash(key) < len(empty_table.array)


@pytest.mark.parametrize('non_iterable', [12, True, False, 0, 2.5, None])
def test_build_hash_table_with_non_iterable_argument_raise_error(non_iterable):
    with pytest.raises(TypeError):
        HashTable(non_iterable)


@pytest.mark.parametrize('wrong_iterable', [
    (1, ),
    (1, 2, 3),
    {1, 2, 3, 4},
    [(1, 2), (3, 4), (5, )]
])
def test_build_hash_table_with__wrong_format_argument_raise_error(wrong_iterable):
    # Correct format is a dict or sequence of 2-items tuples.
    with pytest.raises(TypeError):
        HashTable(wrong_iterable)


@pytest.mark.parametrize('list_argument', [
    [(1, 2), (3, 4), (5, 6)],
    [('a', 'b')],
    [(True, 1), (False, 0)]
])
def test_build_hash_table_with_list_of_tuples_argument(list_argument):
    assert len(HashTable(list_argument)) == len(list_argument)


@pytest.mark.parametrize('dict_argument', [
    {1: 2, 3: 4, 5: 6},
    {'a': 'b'},
    {True: 1, False: 0}
])
def test_build_hash_table_with_dict_argument(dict_argument):
    assert len(HashTable(dict_argument)) == len(dict_argument)


@pytest.mark.parametrize('iterable, capacity_given, capacity_expected', [
    ((), None, 1),
    ((1, ), None, 3),
    ((1, 2), None, 5),
    ((), 0, 1),
    ((), 1, 1),
    ((), 6, 6),
    # Minimum initial capacity is len(iterable) + 1,
    # even if it's lower value directly passed as argument.
    ((1, 2, 3), 1, 4),
    ((1, 2, 3, 4, 5), 2, 6)
    ])
def test_get_capacity(iterable, capacity_given, capacity_expected):
    assert HashTable._get_capacity(capacity_given, iterable) == capacity_expected


def test_iter(filled_table):
    assert set([key for key in filled_table]) == set(INITIAL_KEYS)


def test_len(filled_table):
    assert len(filled_table) == len(INITIAL_ITEMS)


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_contain_true(filled_table, key):
    assert key in filled_table


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_contain_false(filled_table, key):
    assert key not in filled_table


def test_repr_empty_hash_table(empty_table):
    assert empty_table.__repr__() == '{}'


def test_repr_hash_table():
    # Not testing with many items because of random order.
    assert HashTable([(123, 'abc')]).__repr__() == "{123: 'abc'}"


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_getitem_by_existing_key(filled_table, key):
    assert filled_table[key] == dict(INITIAL_ITEMS)[key]


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_getitem_by_non_existing_key_raise_error(filled_table, key):
    with pytest.raises(KeyError):
        filled_table[key]


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_setitem_by_existing_key(filled_table, key):
    filled_table[key] = 'New value'
    assert filled_table[key] == 'New value'


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_setitem_by_non_existing_key(filled_table, key):
    filled_table[key] = 'New value'
    assert filled_table[key] == 'New value'


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_setitem_by_non_existing_key_increase_length(filled_table, key):
    initial_length = len(filled_table)
    filled_table[key] = 'New value'
    assert len(filled_table) == initial_length + 1


@pytest.mark.parametrize('items ,capacity', [
    ([], 2),
    ([(True, False)], 4),
    ([('a', 'b'), ('c', 'd')], 10),
    ([(1, 2), (3, 4), (5, 6)], 500)
])
def test_get_load_factor(items, capacity):
    assert HashTable(items, capacity)._get_load_factor() == len(items) / capacity


def test_increase_capacity(filled_table):
    # Current len(self.array) = 4 for table_with_collisions
    # and 5 for table_without_collisions.
    # Each table contains 3 items,
    # So in both tables load_factor is not more than 0.75.
    # After adding 1 item, both tables load_factor will exceed 0.75,
    # (border value by default), so capacity will be doubled.
    initial_capacity = len(filled_table.array)
    filled_table['four'] = 4
    assert len(filled_table.array) == initial_capacity*2


def test_keys(filled_table):
    assert set(filled_table.keys()) == set(INITIAL_KEYS)


def test_values(filled_table):
    assert set(filled_table.values()) == set([item[1] for item in INITIAL_ITEMS])


def test_items(filled_table):
    assert set(filled_table.items()) == set(INITIAL_ITEMS)


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_get_by_existing_key(filled_table, key):
    assert filled_table.get(key) == dict(INITIAL_ITEMS)[key]


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_get_by_non_existing_key_return_none(filled_table, key):
    assert filled_table.get(key) is None


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_add_by_non_existing_key_increase_length(filled_table, key):
    initial_length = len(filled_table)
    filled_table.add(key, 'New value')
    assert len(filled_table) == initial_length + 1


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_value_is_acceptable_after_add(filled_table, key):
    filled_table.add(key, 'New value')
    assert filled_table[key] == 'New value'


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_add_by_existing_key_raise_error(filled_table, key):
    with pytest.raises(KeyError):
        filled_table.add(key, 'New value')


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_pop_by_existing_key_decrease_length(filled_table, key):
    initial_length = len(filled_table)
    filled_table.pop(key)
    assert len(filled_table) == initial_length - 1


@pytest.mark.parametrize('key', INITIAL_KEYS)
def test_pop_by_existing_key_return_correct_value(filled_table, key):
    assert filled_table.pop(key) == dict(INITIAL_ITEMS)[key]


@pytest.mark.parametrize('key', NON_EXISTING_KEYS)
def test_pop_by_non_existing_key_raise_error(filled_table, key):
    with pytest.raises(KeyError):
        filled_table.pop(key)
