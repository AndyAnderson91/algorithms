"""
Hash table implementation.
Collision resolution is separate chaining with singly linked list.

Usage example:
-------
>> h = HashTable(5, [('one', 1), ('two', 2), ('three', 3)])
>> h
{'two': 2, 'one': 1, 'three': 3}
>> h.add('four', 4)                         # {'two': 2, 'four': 4, 'three': 3, 'one': 1}
>> h.pop('three')                           # {'two': 2, 'four': 4, 'one': 1}
3
>> h.get('five')
None
>> h['five']
KeyError: 'Key is not in the hash table.'
>> h['six'] = 6                             # {'two': 2, 'four': 4, 'six': 6, 'one': 1}
>> h['one'] = True                          # {'two': 2, 'four': 4, 'six': 6, 'one': True}
>> h.keys()
['two', 'four', 'six', 'one']
>> h.values()
[2, 4, 6, True]
>> h.items()
[('two', 2), ('four', 4), ('six', 6), ('one', True)]
>> len(h)
4

Example on collision resolution:
-------
>> h = HashTable(3)                   # h.array: [None, None, None]
# Select keys with equal hashes.
>> h._hash('hello')
2
>> h._hash('world')
2
>> h.add('hello', 1)                  # h.array: [None, None, «['hello', 1]»]
>> h.add('world', 2)                  # h.array: [None, None, «['world', 2] --> ['hello', 1]»]
# Both items are in last array cell,
# contained in singly linked list.
# Capacity doubles if load_factor > 0.75.
>> h.add('bar', 3)                    # h.array: [None, None, None, None, «['bar', 3]», «['hello', 1] --> ['world', 2]»]
"""
from algorithms.linked_lists import SinglyLinkedList


class HashTable:
    """
    Supported methods: __init__, __iter__, __contains__, __len__,
    __getitem__, __setitem__, __repr__, _get_load_factor,
    _increase_capacity, keys, values, items, get, add, pop.
    All methods behave the same as python dict methods.
    """
    def __init__(self, capacity, iterable=()):
        self.array = [None]*capacity
        self._length = 0
        self.max_load_factor = 0.75

        self._build_hash_table(iterable)

    def __iter__(self):
        """Yields key on each iteration."""
        for cell in self.array:
            if cell is not None:
                for item in cell:
                    yield item[0]

    def __contains__(self, key):
        return key in self.keys()

    def __len__(self):
        """Returns number of (key, value) pairs in hash table."""
        return self._length

    def __getitem__(self, key):
        """
        Returns value by required key.
        if key is not in the hash table, raises KeyError.
        """
        if key not in self:
            raise KeyError('Key is not in the hash table.')
        else:
            return self.get(key)

    def __setitem__(self, key, value):
        """
        If key is already in the table, overwrites it's value by provided data.
        Else adds (key, value) pair to hash table.
        """
        index = self._hash(key)

        if self.array[index]:
            for item in self.array[index]:
                if item[0] == key:
                    item[1] = value
                    return

            self.array[index].add([key, value])

        else:
            self.array[index] = SinglyLinkedList(([key, value],))

        self._length += 1

        if self._get_load_factor() > self.max_load_factor:
            self._increase_capacity()

    def __repr__(self):
        items_repr = []
        for key in self:
            value = self.get(key)

            item_repr = "{0}: {1}".format(
                "'{}'".format(key) if isinstance(key, str) else key,
                "'{}'".format(value) if isinstance(value, str) else value
            )
            items_repr.append(item_repr)

        return '{' + ', '.join(items_repr) + '}'

    def _build_hash_table(self, iterable):
        # iterable expected to be container with (key, value) items.
        for item in iterable:
            if len(item) != 2:
                raise TypeError('Expected sequence of containers with 2 elements inside.')

            self.add(item[0], item[1])

    def _hash(self, key):
        """
        Accepts hashable key and transforms it into an integer hash value.
        If key is not hashable, TypeError is raised.
        """
        if not key.__hash__:
            raise TypeError('Unhashable key type')

        # Has separate constant value for str type, so
        # 1 and '1' keys are hashed differently.
        const = 53 if isinstance(key, str) else 47
        max_pow = 5
        hash_value = 0
        for i, symbol in enumerate(str(key)):
            # Pow variates from 0 to 5, so hash is not gonna be huge if long argument is passed.
            hash_value += abs(const - ord(symbol)) * (const**(max_pow - (i % max_pow)))

        # Makes hash value lower than table capacity.
        return hash_value % len(self.array)

    def _get_load_factor(self):
        return len(self) / len(self.array)

    def _increase_capacity(self):
        """
        Doubles capacity of self.array by
        creating temp hash table, copying all (key, value) pairs to it and
        replacing original table array with an increased temp array.
        """
        temp_hash_table = HashTable(len(self.array) * 2)
        for key in self:
            temp_hash_table.add(key, self[key])

        self.array = temp_hash_table.array

    def keys(self):
        """Returns list of keys."""
        return [key for key in self]

    def values(self):
        """Returns list of values."""
        return [self[key] for key in self]

    def items(self):
        """Returns list of (key, value) items."""
        return [(key, self[key]) for key in self]

    def get(self, key, default=None):
        """
        Returns value by a given key.
        If key is not in hash table, returns default (or None).
        """
        index = self._hash(key)

        if self.array[index]:
            for item in self.array[index]:
                if item[0] == key:
                    return item[1]

        return default

    def add(self, key, value):
        """
        Adds key and value to the hash table.
        If key is already in table, KeyError is raised.
        """
        index = self._hash(key)

        # If True - Collision.
        if self.array[index]:
            for item in self.array[index]:
                if item[0] == key:
                    raise KeyError('Item with this key already exists')

            self.array[index].add([key, value])
        else:
            self.array[index] = SinglyLinkedList(([key, value],))

        self._length += 1

        if self._get_load_factor() > self.max_load_factor:
            self._increase_capacity()

    def pop(self, key):
        """
        Returns value by a given key, and removes (key, value) item from hash table.
        Raises KeyError if key is not in the table.
        """
        index = self._hash(key)

        if self.array[index]:
            for i, item in enumerate(self.array[index]):
                # index is needed to pop item from singly linked list.
                if item[0] == key:
                    value = self.array[index].pop(i)[1]

                    if not self.array[index].first:
                        self.array[index] = None

                    self._length -= 1

                    return value

        raise KeyError('Key is not in the hash table.')
