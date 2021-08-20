import unittest
from algorithms.hash_table import HashTable


def fill_table(table, items):
    for item in items:
        table.add(item[0], item[1])


class HashTableGeneralTestCase(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(5)
        self.items = (
            ('one', 1),
            ('two', 2),
            ('three', 3)
        )

    def test_empty_table_repr(self):
        self.assertEqual(str(self.table), '{}')

    def test_filled_table_repr(self):
        self.table.add('one', 1)
        self.assertEqual(str(self.table), "{'one': 1}")

    def test_hashable_keys(self):
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertTrue(isinstance(self.table._hash(key), int))

    def test_unhashable_keys(self):
        for key in ([1, 2, 3], {'one': 1}, {1, 2, 2, 3}):
            self.assertRaises(TypeError, self.table._hash, key)

    def test_hash_is_lower_than_capacity(self):
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertLess(self.table._hash(key), len(self.table.array))

    def test_iter(self):
        fill_table(self.table, self.items)
        keys = set()
        for key in self.table:
            keys.add(key)
        self.assertEqual(keys, set([item[0] for item in self.items]))

    def test_contains(self):
        fill_table(self.table, self.items)
        self.assertTrue('one' in self.table)
        self.assertFalse('ten' in self.table)

    def test_len(self):
        fill_table(self.table, self.items)
        self.assertEqual(len(self.table), len(self.items))

    def test_getitem_by_existing_key(self):
        fill_table(self.table, self.items)
        for item in self.items:
            self.assertEqual(self.table[item[0]], item[1])

    def test_getitem_by_non_existing_key(self):
        fill_table(self.table, self.items)
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertRaises(KeyError, self.table.__getitem__, key)

    def test_get_by_existing_key(self):
        fill_table(self.table, self.items)
        for item in self.items:
            self.assertEqual(self.table.get(item[0]), item[1])

    def test_get_by_non_existing_key(self):
        fill_table(self.table, self.items)
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertIsNone(self.table.get(key))

    def test_setitem_by_new_key(self):
        fill_table(self.table, self.items)
        self.table['ten'] = 10
        self.assertEqual(self.table['ten'], 10)
        self.assertEqual(len(self.table), len(self.items) + 1)

    def test_setitem_by_existing_key(self):
        fill_table(self.table, self.items)
        self.table['one'] = 'Hello'
        self.assertEqual(self.table['one'], 'Hello')
        self.assertEqual(len(self.table), len(self.items))

    def test_add_by_new_key(self):
        fill_table(self.table, self.items)
        self.table.add('ten', 10)
        self.assertEqual(self.table['ten'], 10)
        self.assertEqual(len(self.table), len(self.items) + 1)

    def test_add_by_existing_key(self):
        fill_table(self.table, self.items)
        self.assertRaises(KeyError, self.table.add, 'one', 'Any')

    def test_get_load_factor(self):
        fill_table(self.table, self.items)
        self.assertEqual(self.table._get_load_factor(), len(self.table)/len(self.table.array))

    def test_increase_capacity(self):
        fill_table(self.table, self.items)
        self.assertEqual(len(self.table.array), 5)
        self.table['overloading'] = 'Yes'
        self.assertEqual(len(self.table.array), 10)

    def test_keys(self):
        fill_table(self.table, self.items)
        self.assertEqual(set(self.table.keys()), set([item[0] for item in self.items]))

    def test_values(self):
        fill_table(self.table, self.items)
        self.assertEqual(set(self.table.values()), set([item[1] for item in self.items]))

    def test_items(self):
        fill_table(self.table, self.items)
        self.assertEqual(set(self.table.items()), set(self.items))

    def test_pop_by_existing_key(self):
        fill_table(self.table, self.items)
        self.assertEqual(self.table.pop(self.items[0][0]), self.items[0][1])
        self.assertEqual(len(self.table), len(self.items) - 1)

    def test_pop_last_node_in_array_cell(self):
        fill_table(self.table, [('one', 1), ])
        self.assertEqual(self.table.pop(self.items[0][0]), self.items[0][1])
        self.assertIsNone(self.table.array[self.table._hash('one')])

    def test_pop_by_non_existing_key(self):
        fill_table(self.table, self.items)
        self.assertRaises(KeyError, self.table.pop, 'ten')


class CollisionProcessingTestCase(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(5)
        self.items = [(137, 'First'), (54, 'Second'), (96, 'Third')]
        fill_table(self.table, self.items)
        self.cell_index = self.table._hash(self.items[0][0])
        self.cell = self.table.array[self.cell_index]

    def test_equal_hash_for_items(self):
        self.assertEqual(self.cell_index, self.table._hash(self.items[1][0]))
        self.assertEqual(self.cell_index, self.table._hash(self.items[2][0]))

    def test_all_items_in_one_cell(self):
        self.assertEqual(len(self.cell), 3)

    def test_cell_repr(self):
        self.assertEqual(str(self.cell), "«[96, 'Third'] --> [54, 'Second'] --> [137, 'First']»")

    def test_table_repr(self):
        self.assertEqual(str(self.table), "{96: 'Third', 54: 'Second', 137: 'First'}")

    def test_iter(self):
        keys = set()
        for key in self.table:
            keys.add(key)
        self.assertEqual(keys, set([item[0] for item in self.items]))

    def test_getitem_by_existing_key(self):
        for item in self.items:
            self.assertEqual(self.table[item[0]], item[1])

    def test_get_by_existing_key(self):
        for item in self.items:
            self.assertEqual(self.table.get(item[0]), item[1])

    def test_setitem_by_existing_key(self):
        for i, item in enumerate(self.items):
            self.table[item[0]] = 'New data №{}'.format(i)
            self.assertEqual(self.table[item[0]], 'New data №{}'.format(i))

    def test_pop_by_existing_key(self):
        self.assertEqual(self.table.pop(self.items[2][0]), self.items[2][1])
        self.assertEqual(len(self.table), len(self.items) - 1)

    def test_keys(self):
        self.assertEqual(set(self.table.keys()), set([item[0] for item in self.items]))

    def test_values(self):
        self.assertEqual(set(self.table.values()), set([item[1] for item in self.items]))

    def test_items(self):
        self.assertEqual(set(self.table.items()), set(self.items))










