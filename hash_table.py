from algorithms.linked_lists import SinglyLinkedList


class HashTable:
    """
    Implementation of an associative array abstract data type.
    Collision resolution is separate chaining with singly linked list.
    Supported methods: __init__, __iter__, __contains__, __len__,
    __getitem__, __setitem__, __repr__, _get_load_factor, _increase_capacity, keys, values, items, get, add, pop.
    """
    def __init__(self, capacity=1000):
        self.array = [None]*capacity
        self._length = 0
        self.max_load_factor = 0.75

    def __iter__(self):
        """
        Same behavior as python dict.__iter__().
        Yields key on each iteration.
        """
        for cell in self.array:
            if cell is not None:
                for node in cell:
                    yield node.data[0]

    def __contains__(self, item):
        """
        Returns True if key is in hash table. False otherwise.
        """
        for key in self:
            if key == item:
                return True

        return False

    def __len__(self):
        """
        Returns number of all key, value pairs in hash table.
        """
        return self._length

    def __getitem__(self, key):
        """
        Returns value by required key.
        if key is not in the hash table, raises KeyError.
        """
        # Checks if key is in hash table.
        if key not in self:
            raise KeyError('Key is not in the hash table.')

        # If key is in the hash table, returns it's value.
        else:
            return self.get(key)

    def __setitem__(self, key, value):
        """
        Overwrites value with required key by provided data.
        If required key is not in the hash table, adds key, value pair to it.
        """
        index = self._hash(key)

        # If cell isn't empty - looks for required key in cell nodes.
        if self.array[index]:
            for node in self.array[index]:
                # If required key is found, update it's value.
                if node.data[0] == key:
                    node.data[1] = value
                    return

            # If key is not in singly linked list yet, adds (key, value) pair to it.
            self.array[index].add([key, value])

        else:
            # If array cell with hash index is empty, creates singly linked list and adds key, value in it.
            self.array[index] = SinglyLinkedList(([key, value],))

        self._length += 1

        # Checks if it's time to increase capacity.
        if self._get_load_factor() > self.max_load_factor:
            self._increase_capacity()

    def __repr__(self):
        """
        String representation of HashTable object.
        Same style as python dict.__repr__().
        """
        items = ''
        for key in self:
            value = self.get(key)

            items += "{0}: {1}, ".format(
                "'{}'".format(key) if isinstance(key, str) else key,
                "'{}'".format(value) if isinstance(value, str) else value
            )

        # items[-2] cuts off last comma and space.
        return '{' + items[:-2] + '}'

    def _get_load_factor(self):
        """
        Returns value of load_factor.
        Ratio of number of stored items to array length.
        If it's more than 0.75, it's time to increase array size.
        """
        return len(self) / len(self.array)

    def _increase_capacity(self):
        """
        Creates temp hash table with two times bigger array size.
        Rewrites all key, value pairs to new table.
        Replaces original table array with an increased temp array.
        """
        temp_hash_table = HashTable(len(self.array) * 2)
        for key in self:
            temp_hash_table.add(key, self[key])

        self.array = temp_hash_table.array

    def keys(self):
        """
        Returns list of keys stored in hash table.
        """
        return [key for key in self]

    def values(self):
        """
        Returns list of values stored in hash table.
        """
        return [self[key] for key in self]

    def items(self):
        """
        Returns list of tuples (key, value) stored in hash table.
        """
        return [(key, self[key]) for key in self]

    def _hash(self, key):
        # Obviously, not the greatest hash function ever,
        # and probably built-in hash() function or any hashlib functions could be used,
        # but goal was to implement a custom one.
        """
        Accepts hashable key and transforms it into an integer hash value.
        If key is not hashable, TypeError is raised.
        """
        if not key.__hash__:
            raise TypeError('Unhashable key type')

        # Constant values used by function.
        # Has separate values for str type, so
        # 1 and '1' keys are hashed differently.
        const = 53 if isinstance(key, str) else 47
        max_pow = 5
        hash_value = 0
        for i, symbol in enumerate(str(key)):
            hash_value += abs(const - ord(symbol)) * (const**(max_pow - (i % max_pow)))

        # Makes hash value lower than table capacity.
        return hash_value % len(self.array)

    def get(self, key):
        """
        Returns value by a given key.
        If key is not in hash table, returns None.
        """
        # Gets hash from key.
        index = self._hash(key)

        # Checks if array cell with hash index already contains data.
        if self.array[index]:
            # if True - looks for required key in cell nodes.
            for node in self.array[index]:
                # If required key is found, returns it's value.
                if node.data[0] == key:
                    return node.data[1]

        # If required key isn't found, returns None
        return None

    def add(self, key, value):
        """
        Adds (key, value) to hash table.
        If key is already in table, KeyError is raised.
        """
        # Gets hash value from key.
        index = self._hash(key)

        # Checks if array cell with hash index already contains data.
        # If True - Collision.
        if self.array[index]:
            # Checks if key already in singly linked list.
            for node in self.array[index]:
                # Raises KeyError if True.
                if node.data[0] == key:
                    raise KeyError('Item with this key already exists')

            # If key is not in singly linked list yet, adds (key, value) pair to it.
            self.array[index].add([key, value])

        # If array cell with required hash index is empty, creates singly linked list and adds (key, value) to it.
        else:
            self.array[index] = SinglyLinkedList(([key, value],))

        self._length += 1

        # Checks if it's time to increase capacity.
        if self._get_load_factor() > self.max_load_factor:
            self._increase_capacity()

    def pop(self, key):
        """
        Returns value by a given key, and removes (key, value) from hash table.
        Raises KeyError if key is not in the table.
        """
        # Gets hash value from key.
        index = self._hash(key)

        # Checks if array cell with hash index isn't empty contains data.
        if self.array[index]:
            # If True, looks for required key in cell nodes.
            for i, node in enumerate(self.array[index]):
                # If required key is found, removes (key, value) from the hash table, and returns value
                if node.data[0] == key:
                    value = self.array[index].pop(i).data[1]

                    # If singly linked list is empty after popping required node,
                    # redefines cell value to None.
                    if not self.array[index].first:
                        self.array[index] = None

                    self._length -= 1
                    return value

        # If required key is not found, raises KeyError.
        raise KeyError('Key is not in the hash table.')


h = HashTable(5)
h[137] = 'First'
h[54] = 'Second'
h[96] = 'Third'

print(h.array)
print(h)
