"""
Tests for BSTNode and BinarySearchTree classes.
Three binary search trees are used for testing:
1) Empty binary search tree. Used in several tests
where it doesn't really matter if it's filled or not,
of there it should be empty.
2, 3) Balanced and unbalanced filled binary search trees.
These two trees are main testing objects,
and almost every single test in this module runs both of them
to ensure all methods works correctly in both cases.
"""

import pytest
from algorithms.binary_search_tree import BSTNode, BinarySearchTree


# Constants.

INITIAL_VALUES = [5, 4, -2, 6, 7, 1]
SORTED_INITIAL_VALUES = sorted(INITIAL_VALUES)


# Local fixtures.

@pytest.fixture
def empty_tree():
    return BinarySearchTree()


@pytest.fixture
def unbalanced_tree():
    unb_tree = BinarySearchTree()
    for value in SORTED_INITIAL_VALUES:
        unb_tree.add(value)
    return unb_tree


@pytest.fixture
def balanced_tree():
    return BinarySearchTree(INITIAL_VALUES)


@pytest.fixture(params=['unbalanced_tree', 'balanced_tree'])
def filled_tree(request):
    return request.getfixturevalue(request.param)


# BSTNode class tests.

@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_node_creation(value):
    assert BSTNode(value).value == value


def test_node_is_leaf_true():
    assert BSTNode(5).is_leaf()


@pytest.mark.parametrize('left, right', [(None, 12), (0, 12), (0, None)])
def test_node_is_leaf_false(left, right):
    parent_node = BSTNode(5)
    if left is not None:
        parent_node.left = BSTNode(left)
    if right is not None:
        parent_node.right = BSTNode(right)

    assert not parent_node.is_leaf()


@pytest.mark.parametrize('left, right', [(None, 12), (0, None)])
def test_node_has_one_child_only_true(left, right):
    parent_node = BSTNode(5)
    if left is not None:
        parent_node.left = BSTNode(left)
    if right is not None:
        parent_node.right = BSTNode(right)

    assert parent_node.has_one_child_only()


@pytest.mark.parametrize('left, right', [(None, None), (0, 12)])
def test_node_has_one_child_only_false(left, right):
    parent_node = BSTNode(5)
    if left is not None:
        parent_node.left = BSTNode(left)
    if right is not None:
        parent_node.right = BSTNode(right)

    assert not parent_node.has_one_child_only()


# BinarySearchTree class tests.

def test_build_empty_tree():
    assert BinarySearchTree().root is None


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_build_one_node_tree(value):
    assert BinarySearchTree([value]).root.value == value


@pytest.mark.parametrize('values', [
    (1, 1),
    (5, 1, 2, 3, 2),
    (6, 7, 6)
])
def test_build_tree_with_duplicates_raise_error(values):
    with pytest.raises(KeyError):
        BinarySearchTree(values)


def test_build_binary_search_tree_put_mid_value_in_root():
    mid_value = SORTED_INITIAL_VALUES[len(INITIAL_VALUES)//2]
    assert BinarySearchTree(INITIAL_VALUES).root.value == mid_value


def test_build_binary_search_tree_put_values_in_correct_order():
    assert BinarySearchTree(INITIAL_VALUES).inorder() == SORTED_INITIAL_VALUES


def test_iter(filled_tree):
    values = []
    for value in filled_tree:
        values.append(value)
    assert values == SORTED_INITIAL_VALUES


def test_len(filled_tree):
    assert len(filled_tree) == len(INITIAL_VALUES)


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_contains_true(filled_tree, value):
    assert value in filled_tree


def test_contains_false(filled_tree):
    assert not (-99999 in filled_tree)


def test_repr(filled_tree):
    assert filled_tree.__repr__() == str(SORTED_INITIAL_VALUES)


@pytest.mark.parametrize('child, parent', [
    (-2, 1),
    (4, 1),
    (1, 5),
    (6, 7),
    (7, 5)
])
def test_get_parent_node_in_balanced_tree(balanced_tree, child, parent):
    assert balanced_tree._get_parent_node(child, balanced_tree.root).value == parent


@pytest.mark.parametrize('child, parent', [
    (7, 6),
    (6, 5),
    (5, 4),
    (4, 1),
    (1, -2)
])
def test_get_parent_node_in_unbalanced_tree(unbalanced_tree, child, parent):
    assert unbalanced_tree._get_parent_node(child, unbalanced_tree.root).value == parent


def test_get_parent_node_return_none_for_root(filled_tree):
    assert filled_tree._get_parent_node(filled_tree.root.value, filled_tree.root) is None


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_get_node_return_node_with_requested_value(filled_tree, value):
    assert filled_tree._get_node(value, filled_tree.root).value == value


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_get_node_after_get_parent_node(filled_tree, value):
    # If somewhere we need both - parent node and it's child node
    # (as in remove method, for example) it is more optimal
    # to search for a child node from it's parent node,
    # instead of searching for each node separately from the root,
    # so it's reasonable to test how _get_parent_node
    # and _get_node methods works one after another.
    parent_node = filled_tree._get_parent_node(value, filled_tree.root)
    child_node = filled_tree._get_node(value, parent_node)
    assert child_node.value == value


@pytest.mark.parametrize('value', SORTED_INITIAL_VALUES)
def test_get_existing_successor_node(filled_tree, value):
    current_node = filled_tree._get_node(value, filled_tree.root)
    if current_node.right:
        successor_index = SORTED_INITIAL_VALUES.index(value) + 1
        successor_value = SORTED_INITIAL_VALUES[successor_index]
        assert filled_tree._get_successor_node(current_node).value == successor_value


@pytest.mark.parametrize('value', SORTED_INITIAL_VALUES)
def test_get_non_existing_successor_node_return_none(filled_tree, value):
    current_node = filled_tree._get_node(value, filled_tree.root)
    if current_node.right is None:
        assert filled_tree._get_successor_node(current_node) is None


def test_get_successor_node_of_none_raise_error(filled_tree):
    with pytest.raises(ValueError):
        filled_tree._get_successor_node(None)


def test_balance_method_rebuild_tree_as_balanced(unbalanced_tree, balanced_tree):
    unbalanced_tree.balance()
    unb_root, bal_root = unbalanced_tree.root.value, balanced_tree.root.value
    unb_left, bal_left = unbalanced_tree.root.left.value, balanced_tree.root.left.value
    unb_right, bal_right = unbalanced_tree.root.right.value, balanced_tree.root.right.value
    assert (unb_root, unb_left, unb_right) == (bal_root, bal_left, bal_right)


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_exists_true(filled_tree, value):
    assert filled_tree.exists(value)


def test_exists_false(filled_tree):
    assert not filled_tree.exists(-999999)


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_first_added_value_accessible_via_root_link(empty_tree, value):
    empty_tree.add(value)
    assert empty_tree.root.value == value


def test_add_new_value_increase_length(filled_tree):
    filled_tree.add(-99999)
    assert filled_tree._length == len(INITIAL_VALUES) + 1


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_add_duplicate_raise_error(filled_tree, value):
    with pytest.raises(KeyError):
        filled_tree.add(value)


@pytest.mark.parametrize('left, right, parent', [
    (-5, 0, -2),
    (2, 4.5, 4),
    (5.5, 6.5, 6)
])
def test_added_children_accessible_via_left_and_right_parent_link(balanced_tree, left, right, parent):
    parent_node = balanced_tree._get_node(parent, balanced_tree.root)
    balanced_tree.add(left)
    balanced_tree.add(right)
    assert (parent_node.left.value, parent_node.right.value) == (left, right)


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_remove_existing_value_decrease_length(filled_tree, value):
    filled_tree.remove(value)
    assert filled_tree._length == len(INITIAL_VALUES) - 1


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_remove_correct_value(filled_tree, value):
    filled_tree.remove(value)
    assert sorted(filled_tree.inorder() + [value]) == SORTED_INITIAL_VALUES


@pytest.mark.parametrize('value', [-999, 0, 3, 8, 999])
def test_remove_non_existing_value_raise_error(filled_tree, value):
    with pytest.raises(ValueError):
        filled_tree.remove(value)


@pytest.mark.parametrize('value', [-2, 4, 6])
def test_removed_leaf_parent_link_redirected_to_none(balanced_tree, value):
    parent_node = balanced_tree._get_parent_node(value, balanced_tree.root)
    balanced_tree.remove(value)
    link_removed_leaf = parent_node.left if value < parent_node.value else parent_node.right
    assert link_removed_leaf is None


@pytest.mark.parametrize('child, node, parent', [
    (7, 6, 5),
    (6, 5, 4),
    (5, 4, 1),
    (4, 1, -2),
])
def test_node_with_one_child_replaced_by_its_child_after_removing(unbalanced_tree, child, node, parent):
    parent_node = unbalanced_tree._get_parent_node(node, unbalanced_tree.root)
    node_to_remove = unbalanced_tree._get_node(node, parent_node)
    child_node = unbalanced_tree._get_node(child, node_to_remove)
    unbalanced_tree.remove(node)
    assert parent_node.right.value == child_node.value


@pytest.mark.parametrize('value, successor', [
    (1, 4),
    (5, 6)
])
def test_node_with_two_children_replaced_by_successor_after_removing(balanced_tree, value, successor):
    parent_node = balanced_tree._get_parent_node(value, balanced_tree.root)
    balanced_tree.remove(value)
    if parent_node:
        redirected_link = parent_node.left if value < parent_node.value else parent_node.right
    else:
        redirected_link = balanced_tree.root
    assert redirected_link.value == successor


@pytest.mark.parametrize('value', INITIAL_VALUES)
def test_right_order_after_node_removed(filled_tree, value):
    filled_tree.remove(value)
    remaining_values = filled_tree.inorder()
    assert remaining_values == sorted(remaining_values)


def test_inorder(filled_tree):
    assert filled_tree.inorder() == SORTED_INITIAL_VALUES
