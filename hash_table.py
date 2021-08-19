from linked_lists import SinglyLinkedList


class HashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.length = 0

    def __hash_function(self, key):
        total = 0
        const = 89
        max_pow = 5
        for i, symbol in enumerate(str(key)):
            total += ord(symbol) * (const**(max_pow - (i % max_pow)))

        hash_value = total % self.capacity

        return hash_value

    def get(self, key):
        index = self.__hash_function(key)
        if not self.arr[index]:
            return None
        else:
            for node in self.arr[index]:
                if node.data[0] == key:
                    return node.data[1]
            return None

    def add(self, key, value):
        index = self.__hash_function(key)
        # If slot is empty, creates SinglyLinkedList in it
        # and adds (key, value) inside created list.
        if not self.arr[index]:
            self.arr[index] = SinglyLinkedList()
            self.arr[index].add((key, value))
        # If slot isn't empty - collision.
        else:
            # Checks if same key is inside SinglyLinkedList.
            # Raises KeyError if True.
            for node in self.arr[index]:
                if node.data[0] == key:
                    raise KeyError('Item with this key already exists')
            # Otherwise adds (key, value) pair to SinglyLinkedList.
            self.arr[index].add((key, value))

        self.length += 1

    def pop(self, key):
        index = self.__hash_function(key)

        if not self.arr[index]:
            return None

        else:
            for i, node in enumerate(self.arr[index]):
                if node.data[0] == key:
                    value = self.arr[index].pop(i).data[1]
                    if not self.arr[index].first:
                        self.arr[index] = None

                    self.length -= 1
                    return value

            return None


h = HashTable(7)

h.add('hey', 100)
h.add('one', 1)
h.add('two', 2)
h.add('three', 3)
h.add('four', 4)
h.add('five', 5)
h.add('six', 6)
h.add('seven', 7)

print(h.pop('four'))

print(h.arr)
