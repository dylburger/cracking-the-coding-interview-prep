from Node import Node
from checkBST import checkBST

def test_single_node_tree():
    """ root node is the only node
    """
    root = Node(3)
    assert checkBST(root) is True

def test_tree_with_single_left_and_right_nodes():
    """ tree with height = 1
    """
    root = Node(3, Node(2), Node(4))
    assert checkBST(root) is True

def test_tree_with_height_of_2():
    """ tree with height = 2
    """
    root = Node(5, Node(3, Node(1), Node(4)), Node(8, Node(7), Node(10)))
    assert checkBST(root) is True

def test_tree_with_duplicate_nodes():
    root = Node(5, Node(4, Node(3), Node(5)), Node(6, Node(1), Node(10)))
    assert checkBST(root) is False

def test_tree_with_one_duplicate_node():
    root = Node(2, Node(1), Node(2))
    assert checkBST(root) is False

def test_tree_with_out_of_range_value():
    root = Node(-1, Node(2), Node(4))
    assert checkBST(root) is False

def test_tree_with_out_of_range_value_max():
    root = Node(10001, Node(2), Node(4))
    assert checkBST(root) is False

def test_non_binary_search_tree():
    root = Node(3, Node(4), Node(2))
    assert checkBST(root) is False

def test_non_bst_2():
    root = Node(2, Node(1), Node(2))
    assert checkBST(root) is False
