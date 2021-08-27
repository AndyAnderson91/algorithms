class BSTNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        left = self.left.data if self.left else None
        right = self.right.data if self.right else None
        return '{0} <-- {1} --> {2}'.format(left, self.data, right)

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

    def __contains__(self, data):
        return bool(self._get_node(data))

    def __repr__(self):
        return str(self.inorder())

    def _build_binary_search_tree(self, values):
        prepared = self._order_to_add(sorted(list(values)), 0, len(values)-1)
        for value in prepared:
            self.add(value)

    def _order_to_add(self, array, start, end):
        if start > end:
            return []

        mid = (start + end) // 2
        return [array[mid]] + self._order_to_add(array, start, mid - 1) + self._order_to_add(array, mid + 1, end)

    def _get_inordered_data(self, node, nodes):
        if node:
            if node.left:
                self._get_inordered_data(node.left, nodes)
            nodes.append(node.data)
            if node.right:
                self._get_inordered_data(node.right, nodes)

        return nodes

    def _get_node(self, data):
        current = self.root
        while current:
            if data == current.data:
                return current

            current = current.left if data < current.data else current.right

    @staticmethod
    def _get_successor(node):
        current = node.right
        if current:
            while current.left:
                current = current.left
        return current

    def balance(self):
        sorted_values = self.inorder()
        self.root = None
        self._build_binary_search_tree(sorted_values)

    def add(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            self._length += 1
        else:
            parent = self.root
            while parent:
                if data < parent.data and parent.left:
                    parent = parent.left
                elif data < parent.data and not parent.left:
                    parent.left = BSTNode(data, parent)
                    self._length += 1
                    return
                elif data > parent.data and parent.right:
                    parent = parent.right
                elif data > parent.data and not parent.right:
                    parent.right = BSTNode(data, parent)
                    self._length += 1
                    return
                else:
                    raise KeyError('No duplicates available')

    def remove(self, data):
        node_to_remove = self._get_node(data)

        if not node_to_remove:
            raise ValueError('{0} is not in binary search tree'.format(data))

        parent = node_to_remove.parent

        if node_to_remove.is_leaf():
            if node_to_remove == self.root:
                self.root = None
            elif node_to_remove == parent.left:
                parent.left = None
            else:
                parent.right = None

        elif node_to_remove.has_one_child_only():
            child = node_to_remove.left if node_to_remove.left else node_to_remove.right
            if node_to_remove == self.root:
                self.root = child
            elif node_to_remove == parent.left:
                parent.left = child
            else:
                parent.right = child
            child.parent = parent

        else:
            successor = self._get_successor(node_to_remove)
            self.remove(successor.data)

            if node_to_remove == self.root:
                self.root = successor
            elif node_to_remove == parent.left:
                parent.left = successor
            else:
                parent.right = successor

            successor.parent = parent

            successor.left = node_to_remove.left
            if successor.left:
                successor.left.parent = successor

            successor.right = node_to_remove.right
            if successor.right:
                successor.right.parent = successor

    def exists(self, data):
        return bool(self._get_node(data))

    def inorder(self):
        return self._get_inordered_data(self.root, [])


arr = [2, 7, 8, 15, 16, 18, 21, 22, 22.5, 23, 24, 25, 26, 28, 30]

b = BinarySearchTree(arr)
b.remove(30)
print(b.root.right.right)

print(b.inorder())
