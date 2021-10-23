r"""
Binary search tree implementation.

Usage example:
-------
>> b = BinarySearchTree([5, 1, 3, 4])
#                  4
#                /   \
#              3      5
#             /
#            1
>> b.root
3 <-- 4 --> 5
>> b.inorder()
[1, 3, 4, 5]
>> b.add(0)
>> b.add(-2)
#                 4
#               /   \
#             3      5
#            /
#           1
#         /
#        0
#      /
#    -2
>> b.root.left.left.left
-2 <-- 0 --> None
>> b.balance()
#                 3
#               /   \
#             0      5
#           / \     /
#         -2   1   4
>> b.root
0 <-- 3 --> 5
>> b.remove(0)
#                 3
#               /   \
#             1      5
#           /      /
#         -2      4
>> b.exists(0)
False
>> b.exists(4)
True
"""


class BSTNode:
    """Binary Search Tree element."""
    def __init__(self, value, left=None, right=None):
        self.value = value
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
    """
    Binary tree data structure where parent node contains value
    which is less than it's right child's value
    and greater than it's left child's value.
    Every node may have 2 children or less.
    """
    def __init__(self, iterable=()):
        self._length = 0
        self.root = None

        self._build_binary_search_tree(iterable)

    def __iter__(self):
        for value in self.inorder():
            yield value

    def __len__(self):
        return self._length

    def __contains__(self, value):
        return self.exists(value)

    def __repr__(self):
        return str(self.inorder())

    def _build_binary_search_tree(self, iterable):
        """Builds balanced binary search tree from a given collection."""

        def create_nodes(values):
            if values:
                mid = len(values) // 2

                node = BSTNode(values[mid])
                self._length += 1

                if not self.root:
                    self.root = node

                node.left = create_nodes(values[:mid])
                node.right = create_nodes(values[mid + 1:])

                return node

        if iter(iterable):

            if len(iterable) != len(set(iterable)):
                raise KeyError('Sequence of elements contains duplicates.')

            sorted_values = sorted(list(iterable))
            create_nodes(sorted_values)

    def _get_parent_node(self, child_value, subtree_root):
        """
        Return parent node by requested child's value.
        Traversal starts from a subtree_root.
        Support method that is used in add/remove methods.
        """
        if not subtree_root or subtree_root.value == child_value:
            # For subtree_root = self.root cases.
            return None

        elif child_value < subtree_root.value and subtree_root.left and child_value != subtree_root.left.value:
            return self._get_parent_node(child_value, subtree_root.left)
        elif child_value > subtree_root.value and subtree_root.right and child_value != subtree_root.right.value:
            return self._get_parent_node(child_value, subtree_root.right)
        else:
            return subtree_root

    def _get_node(self, value, subtree_root):
        """
        Return node by requested value.
        Traversal starts from a subtree_root.
        Support method that is used in exists/remove methods.
        """
        # This method may be used after _get_parent_node method,
        # then parent_node is passed here as 'subtree_root' argument,
        # so there is no need to traverse from the root of the tree.
        # subtree_root argument can be None in 2 cases:
        # 1) On first (non-recursive) call if desired node is root (root's parent is None)
        # 2) In recursive call if desired node doesn't exist.
        if subtree_root is None and self.root and value == self.root.value:
            return self.root

        if subtree_root and subtree_root.value < value:
            return self._get_node(value, subtree_root.right)
        elif subtree_root and subtree_root.value > value:
            return self._get_node(value, subtree_root.left)
        else:
            return subtree_root

    @staticmethod
    def _get_successor_node(node):
        """
        Returns node with a next largest value to a given node.
        Search for it in a subtree, where given node is a root.
        Used in remove method.
        """
        if node is None:
            raise ValueError("Can't find successor of None")

        successor = node.right
        if successor:
            while successor.left:
                successor = successor.left
        return successor

    def balance(self):
        """
        Rebuilds binary search tree in a configuration,
        where all paths from the root of the tree to it's leaves
        differ in length by no more than 1.
        """
        sorted_values = self.inorder()
        self.root = None
        self._build_binary_search_tree(sorted_values)

    def exists(self, value):
        """Returns True if node with required value is in a tree."""
        return bool(self._get_node(value, self.root))

    def add(self, value):
        """Appends node with a given value to the tree."""
        parent_node = self._get_parent_node(value, self.root)

        if not self.root:
            self.root = BSTNode(value)
        elif parent_node and value < parent_node.value and not parent_node.left:
            parent_node.left = BSTNode(value)
        elif parent_node and value > parent_node.value and not parent_node.right:
            parent_node.right = BSTNode(value)
        else:
            raise KeyError('Node with this value already exists')

        self._length += 1

    def remove(self, value):
        """
        Removes node with required value from a tree.
        Tree configuration is changing according to cases:
        1) If node to remove is a leaf, it's parent link redirects to None.
        2) If node to remove has one child, it's parent link redirects to a child.
        3) If node to remove has two children, it's replaced by a node with successor value, founded in it's subtree.
        (Node with successor value will be moved to the place where node to remove existed before).
        """
        parent_node = self._get_parent_node(value, self.root)
        node_to_remove = self._get_node(value, parent_node)

        if not node_to_remove:
            raise ValueError('{0} is not in binary search tree'.format(value))

        # First case.
        if node_to_remove.is_leaf():
            if node_to_remove == self.root:
                self.root = None
            elif node_to_remove == parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None

        # Second case.
        elif node_to_remove.has_one_child_only():
            child_node = node_to_remove.left if node_to_remove.left else node_to_remove.right
            if node_to_remove == self.root:
                self.root = child_node
            elif node_to_remove == parent_node.left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        # Third case.
        else:
            successor_node = self._get_successor_node(node_to_remove)
            self.remove(successor_node.value)
            # Successor node will be removed from it's place,
            # but not from a tree, so need to compensate length's loss.
            self._length += 1

            if node_to_remove == self.root:
                self.root = successor_node
            elif node_to_remove == parent_node.left:
                parent_node.left = successor_node
            else:
                parent_node.right = successor_node

            successor_node.left = node_to_remove.left
            successor_node.right = node_to_remove.right

        self._length -= 1

    def inorder(self):
        """Returns list of values obtained via inorder traversal."""
        inordered_values = []

        def _get_inordered_values(node):
            if node:
                if node.left:
                    _get_inordered_values(node.left)
                inordered_values.append(node.value)
                if node.right:
                    _get_inordered_values(node.right)

        _get_inordered_values(self.root)

        return inordered_values
