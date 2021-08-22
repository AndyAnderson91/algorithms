from algorithms.linked_lists import SinglyLinkedList


class HashTable:
    """
    Implementation of an associative array abstract data type.
    Collision resolution is separate chaining with singly linked list.
    Supported methods: __init__, __iter__, __contains__, __len__,
    __getitem__, __setitem__, __repr__, _get_load_factor,
    _increase_capacity, keys, values, items, get, add, pop.
    """
    def __init__(self, capacity, iterable=()):
        self.array = [None]*capacity
        self._length = 0
        self.max_load_factor = 0.75

        for item in iterable:
            if len(item) != 2:
                raise TypeError('Expected sequence of containers with 2 elements inside.')

            self.add(item[0], item[1])

    def __iter__(self):
        """
        Same behavior as python dict.__iter__().
        Yields key on each iteration.
        """
        for cell in self.array:
            if cell is not None:
                for item in cell:
                    yield item[0]

    def __contains__(self, required_key):
        """
        Returns True if key is in hash table. False otherwise.
        """
        for key in self:
            if key == required_key:
                return True

        return False

    def __len__(self):
        """
        Returns number of all (key, value) pairs in hash table.
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
        If key is already in the table, overwrites it's value by provided data.
        Else adds (key, value) pair to hash table.
        """
        index = self._hash(key)

        # If cell isn't empty - looks for required key in cell items.
        if self.array[index]:
            for item in self.array[index]:
                # If required key is found, update it's value.
                if item[0] == key:
                    item[1] = value
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
            # Pow variates from 0 to 5, so hash is not gonna be huge if long argument is passed.
            hash_value += abs(const - ord(symbol)) * (const**(max_pow - (i % max_pow)))

        # Makes hash value lower than table capacity.
        return hash_value % len(self.array)

    def _get_load_factor(self):
        """
        Returns value of load_factor -
        Ratio of number of stored items to array length.
        Value more than self.max_load_factor means it's time to increase capacity.
        """
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

    def get(self, key, default=None):
        """
        Behaves the same as dict.get()
        Returns value by a given key.
        If key is not in hash table, returns default (or None).
        """
        # Gets hash from key.
        index = self._hash(key)

        # Checks if array cell with hash index already contains data.
        if self.array[index]:
            # if True - looks for required key in cell items.
            for item in self.array[index]:
                # If required key is found, returns it's value.
                if item[0] == key:
                    return item[1]

        # If required key isn't found, returns default.
        return default

    def add(self, key, value):
        """
        Adds key and value to the hash table.
        If key is already in table, KeyError is raised.
        """
        # Gets hash from key.
        index = self._hash(key)

        # Checks if array cell with hash index already contains data.
        # If True - Collision.
        if self.array[index]:
            # Checks if key already in singly linked list.
            for item in self.array[index]:
                # Raises KeyError if True.
                if item[0] == key:
                    raise KeyError('Item with this key already exists')

            # If key is not in singly linked list yet, adds (key, value) pair to it.
            self.array[index].add([key, value])

        # If array cell with required hash index is empty, creates singly linked list with (key, value) in first node.
        else:
            self.array[index] = SinglyLinkedList(([key, value],))

        # Increments hash table length by 1.
        self._length += 1

        # Checks if it's time to increase capacity.
        if self._get_load_factor() > self.max_load_factor:
            self._increase_capacity()

    def pop(self, key):
        """
        Returns value by a given key, and removes (key, value) from hash table.
        Raises KeyError if key is not in the table.
        """
        # Gets hash from key.
        index = self._hash(key)

        # Checks if array cell with hash index contains data.
        if self.array[index]:
            # If True, looks for required key in cell items.
            for i, item in enumerate(self.array[index]):
                # If required key is found, removes (key, value) from the hash table, and returns value
                if item[0] == key:
                    value = self.array[index].pop(i)[1]

                    # If singly linked list is empty after popping required node,
                    # overwrites cell value to None.
                    if not self.array[index].first:
                        self.array[index] = None

                    # Decrements hash table length by 1
                    self._length -= 1

                    return value

        # If required key is not found, raises KeyError.
        raise KeyError('Key is not in the hash table.')
