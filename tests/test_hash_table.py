import unittest
from algorithms.hash_table import HashTable


class HashTableGeneralTestCase(unittest.TestCase):
    """
    General TestCase for HashTable Class.
    """
    def setUp(self):
        self.base_table = HashTable(5)
        self.items = (
            ('one', 1),
            ('two', 2),
            ('three', 3)
        )
        self.filled_table = HashTable(5, self.items)

    def test_empty_table_repr(self):
        """
        Checks __repr__ method for empty table.
        """
        self.assertEqual(str(self.base_table), '{}')

    def test_filled_table_repr(self):
        """
        Checks __repr__ method for filled table.
        """
        self.base_table.add('one', 1)
        self.assertEqual(str(self.base_table), "{'one': 1}")

    def test_hashable_keys(self):
        """
        Checks if custom _hash function only accepts hashable arguments.
        """
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertTrue(isinstance(self.base_table._hash(key), int))

    def test_unhashable_keys(self):
        """
        Checks if TypeError is raised if unhashable arguments are passed to custom _hash function.
        """
        for key in ([1, 2, 3], {'one': 1}, {1, 2, 2, 3}):
            self.assertRaises(TypeError, self.base_table._hash, key)

    def test_hash_is_lower_than_capacity(self):
        """
        Checks if custom _hash function returns indexes in range of table.array.
        """
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertLess(self.base_table._hash(key), len(self.base_table.array))

    def test_iter(self):
        """
        Checks if __iter__ method implemented correctly.
        """
        keys = set()
        for key in self.filled_table:
            keys.add(key)
        self.assertEqual(keys, set([item[0] for item in self.items]))

    def test_contains(self):
        """
        Checks if __contains__ method implemented correctly.
        """
        self.assertTrue('one' in self.filled_table)
        self.assertFalse('ten' in self.filled_table)

    def test_len(self):
        """
        Checks if __len__ method implemented correctly.
        """
        self.assertEqual(len(self.filled_table), len(self.items))

    def test_getitem_by_existing_key(self):
        """
        Checks if __getitem__ method returns element by required existing index.
        """
        for item in self.items:
            self.assertEqual(self.filled_table[item[0]], item[1])

    def test_getitem_by_non_existing_key(self):
        """
        Checks if __getitem__ method raises KeyError if required key is not in table.
        """
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertRaises(KeyError, self.filled_table.__getitem__, key)

    def test_get_by_existing_key(self):
        """
        Checks if get method returns correct value by required key.
        """
        for item in self.items:
            self.assertEqual(self.filled_table.get(item[0]), item[1])

    def test_get_by_non_existing_key(self):
        """
        Checks if get method returns None by non-existing key.
        """
        for key in ('string', 100, 25.5, True, (1, 2, 3), range(5)):
            self.assertIsNone(self.filled_table.get(key))

    def test_setitem_by_new_key(self):
        """
        Checks if __setitem__ method adds key, value in table if required key is not there yet.
        """
        self.filled_table['ten'] = 10
        self.assertEqual(self.filled_table['ten'], 10)
        self.assertEqual(len(self.filled_table), len(self.items) + 1)

    def test_setitem_by_existing_key(self):
        """
        Checks if __setitem__ method updates value by existing key.
        """
        self.filled_table['one'] = 'Hello'
        self.assertEqual(self.filled_table['one'], 'Hello')
        self.assertEqual(len(self.filled_table), len(self.items))

    def test_add_by_new_key(self):
        """
        Checks if add method adds key, value in table if key is not there yet.
        """
        self.filled_table.add('ten', 10)
        self.assertEqual(self.filled_table['ten'], 10)
        self.assertEqual(len(self.filled_table), len(self.items) + 1)

    def test_add_by_existing_key(self):
        """
        Checks if KeyError is raised if attempts to add new key, value to table with existing key.
        """
        self.assertRaises(KeyError, self.filled_table.add, 'one', 'Any')

    def test_get_load_factor(self):
        """
        Checks if _get_load_factor method returns correct value.
        """
        self.assertEqual(self.filled_table._get_load_factor(), len(self.filled_table)/len(self.filled_table.array))

    def test_increase_capacity(self):
        """
        Checks if _increase_capacity method implemented correctly.
        """
        self.assertEqual(len(self.filled_table.array), 5)
        self.filled_table['overloading'] = 'Yes'
        self.assertEqual(len(self.filled_table.array), 10)

    def test_keys(self):
        """
        Checks if keys method returns existing keys.
        """
        self.assertEqual(set(self.filled_table.keys()), set([item[0] for item in self.items]))

    def test_values(self):
        """
        Checks if value method returns existing values.
        """
        self.assertEqual(set(self.filled_table.values()), set([item[1] for item in self.items]))

    def test_items(self):
        """
        Checks if items method returns key, value pairs.
        """
        self.assertEqual(set(self.filled_table.items()), set(self.items))

    def test_pop_by_existing_key(self):
        """
        Checks pop method returns removes key, value from the table and returns value if required key is in the table.
        """
        self.assertEqual(self.filled_table.pop(self.items[0][0]), self.items[0][1])

    def test_pop_last_node_in_array_cell(self):
        """
        Checks pop method overwrites array cell by None, if last item in this cell was popped.
        """
        self.filled_table.pop(self.items[0][0])
        self.assertIsNone(self.filled_table.array[self.filled_table._hash('one')])

    def test_pop_lowers_length_attribute(self):
        """
        Checks if pop method lowers table._length by 1.
        """
        self.filled_table.pop(self.items[0][0])
        self.assertEqual(len(self.filled_table), len(self.items) - 1)

    def test_pop_by_non_existing_key(self):
        """
        Checks if KeyError is raised if attempts to pop element by non-existing key.
        """
        self.assertRaises(KeyError, self.filled_table.pop, 'ten')


class CollisionProcessingTestCase(unittest.TestCase):
    """
    This TestCase purpose is to test collision resolution and implemented methods behavior in collision situation.
    """
    def setUp(self):
        """
        Keys are deliberately selected on a way, their hashes are one integer.
        Not hard considering hashtable is only 5 elements size.
        All these items will be store in one array cell and contained in singly linked list.
        """
        self.items = [(137, 'First'), (54, 'Second'), (96, 'Third')]
        self.table = HashTable(5, self.items)
        self.cell_index = self.table._hash(self.items[0][0])
        self.cell = self.table.array[self.cell_index]

    def test_equal_hash_for_items(self):
        """
        Checks if all hashes are equal.
        """
        self.assertEqual(self.cell_index, self.table._hash(self.items[1][0]))
        self.assertEqual(self.cell_index, self.table._hash(self.items[2][0]))

    def test_all_items_in_one_cell(self):
        """
        Checks if all 3 items are stored in one array cell.
        """
        self.assertEqual(len(self.cell), 3)

    def test_cell_repr(self):
        """
        This one is more like a demonstration of how does it look, than actually a test.
        This is how items are stored in one array cell.
        """
        self.assertEqual(str(self.cell), "«[96, 'Third'] --> [54, 'Second'] --> [137, 'First']»")

    def test_table_repr(self):
        """
        Checks if table.__repr__ method works correctly.
        """
        self.assertEqual(str(self.table), "{96: 'Third', 54: 'Second', 137: 'First'}")

    def test_iter(self):
        """
        Checks if __iter__ method works correctly.
        """
        keys = set()
        for key in self.table:
            keys.add(key)
        self.assertEqual(keys, set([item[0] for item in self.items]))

    def test_getitem_by_existing_key(self):
        """
        Checks if __getitem__ method works correctly.
        """
        for item in self.items:
            self.assertEqual(self.table[item[0]], item[1])

    def test_get_by_existing_key(self):
        """
        Checks if get method works correctly.
        """
        for item in self.items:
            self.assertEqual(self.table.get(item[0]), item[1])

    def test_setitem_by_existing_key(self):
        """
        Checks if __setitem__ method works correctly.
        """
        for i, item in enumerate(self.items):
            self.table[item[0]] = 'New data №{}'.format(i)
            self.assertEqual(self.table[item[0]], 'New data №{}'.format(i))

    def test_pop_by_existing_key(self):
        """
        Checks if pop method works correctly.
        """
        self.assertEqual(self.table.pop(self.items[2][0]), self.items[2][1])
        self.assertEqual(len(self.table), len(self.items) - 1)

    def test_keys(self):
        """
        Checks if keys method works correctly.
        """
        self.assertEqual(set(self.table.keys()), set([item[0] for item in self.items]))

    def test_values(self):
        """
        Checks if values method works correctly.
        """
        self.assertEqual(set(self.table.values()), set([item[1] for item in self.items]))

    def test_items(self):
        """
        Checks if items method works correctly.
        """
        self.assertEqual(set(self.table.items()), set(self.items))
