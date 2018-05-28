class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def checkBST(root):
    """ Given a Binary Tree root node, 
        return True if this is a binary search tree
    """
    INT_MIN = 0
    INT_MAX = 10000

    values_seen_so_far = []

    def checkNode(node, minVal, maxVal):
        if node is None or node.data is None:
            return True
        if node.data < minVal or node.data > maxVal or node.data in values_seen_so_far:
            return False

        values_seen_so_far.append(node.data)

        return checkNode(node.left, INT_MIN, (node.data - 1)) and checkNode(node.right, (node.data + 1), INT_MAX)

    return checkNode(root, INT_MIN, INT_MAX)
