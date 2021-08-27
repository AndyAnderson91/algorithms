class BSTNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return '{0} <-- {1} --> {2}'.format(left, self.value, right)

    def is_leaf(self):
        return not bool(self.left or self.right)

    def has_one_child_only(self):
        return bool(self.left) != bool(self.right)


class BinarySearchTree:
    def __init__(self, iterable=()):
        self._length = 0
        self.root = None

        if iterable:
            sorted_values = sorted(list(iterable))
            self._build_binary_search_tree(sorted_values)

    def __iter__(self):
        for value in self.inorder():
            yield value

    def __len__(self):
        return self._length

    def __contains__(self, value):
        return bool(self._get_node(value))

    def __repr__(self):
        return str(self.inorder())

    def _build_binary_search_tree(self, sorted_values):
        prepared_values = self._prepare_values(sorted_values, 0, len(sorted_values)-1)
        for value in prepared_values:
            self.add(value)

    def _prepare_values(self, array, start, end):
        if start > end:
            return []

        mid = (start + end) // 2
        return [array[mid]] + self._prepare_values(array, start, mid - 1) + self._prepare_values(array, mid + 1, end)

    def _get_inordered_values(self, node, values):
        if node:
            if node.left:
                self._get_inordered_values(node.left, values)
            values.append(node.value)
            if node.right:
                self._get_inordered_values(node.right, values)

        return values

    def _get_node(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node

            current_node = current_node.left if value < current_node.value else current_node.right

    @staticmethod
    def _get_successor(node):
        current_node = node.right
        if current_node:
            while current_node.left:
                current_node = current_node.left
        return current_node

    def balance(self):
        sorted_values = self.inorder()
        self.root = None
        self._build_binary_search_tree(sorted_values)

    def add(self, value):
        if not self.root:
            self.root = BSTNode(value)
            self._length += 1
        else:
            parent_node = self.root
            while parent_node:
                if value < parent_node.value and parent_node.left:
                    parent_node = parent_node.left
                elif value < parent_node.value and not parent_node.left:
                    parent_node.left = BSTNode(value, parent_node)
                    self._length += 1
                    return
                elif value > parent_node.value and parent_node.right:
                    parent_node = parent_node.right
                elif value > parent_node.value and not parent_node.right:
                    parent_node.right = BSTNode(value, parent_node)
                    self._length += 1
                    return
                else:
                    raise KeyError('Node with this value already exists')

    def remove(self, value):
        node_to_remove = self._get_node(value)

        if not node_to_remove:
            raise ValueError('{0} is not in binary search tree'.format(value))

        parent_node = node_to_remove.parent

        if node_to_remove.is_leaf():
            if node_to_remove == self.root:
                self.root = None
            elif node_to_remove == parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None

        elif node_to_remove.has_one_child_only():
            child_node = node_to_remove.left if node_to_remove.left else node_to_remove.right
            if node_to_remove == self.root:
                self.root = child_node
            elif node_to_remove == parent_node.left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            child_node.parent = parent_node

        else:
            successor_node = self._get_successor(node_to_remove)
            self.remove(successor_node.value)

            if node_to_remove == self.root:
                self.root = successor_node
            elif node_to_remove == parent_node.left:
                parent_node.left = successor_node
            else:
                parent_node.right = successor_node

            successor_node.parent = parent_node

            successor_node.left = node_to_remove.left
            if successor_node.left:
                successor_node.left.parent = successor_node

            successor_node.right = node_to_remove.right
            if successor_node.right:
                successor_node.right.parent = successor_node

        self._length -= 1

    def exists(self, value):
        return bool(self._get_node(value))

    def inorder(self):
        return self._get_inordered_values(self.root, [])
