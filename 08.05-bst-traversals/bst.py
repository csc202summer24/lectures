class BinarySearchTree:
    """ A binary search tree """

    def __init__(self):
        # The root of this tree:
        self.root = None
        # The number of nodes in this tree:
        self.size = 0


class Node:
    """ A single node in a binary search tree """

    def __init__(self, key, left, right):
        # The key contained in this node:
        self.key = key
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def find(bst, key):
    # Return the result of finding from the root.
    pass


def _find(node, key):
    # If the node does not exist, then:
    #     Note that the key does not exist.
    # Else if the node contains the given key, then:
    #     Note that the key exists in the node.
    # Else if the node's key is larger than the given key, then:
    #     Return the result of recursing on the left child.
    # Else, do:
    #     Return the result of recursing on the right child.
    pass


def insert(bst, key):
    # Set the root to the result of inserting at the root.
    pass


def _insert(bst, node, key):
    # If the node does not exist, then:
    #     Increment the size.
    #     Return a new node with no children containing the given key.
    # Else if the node's key is larger than the given key, then:
    #     Set the left child to the result of recursing on that child.
    #     Return the given node.
    # Else if the node's key is smaller than the given key, then:
    #     Set the right child to the result of recursing on that child.
    #     Return the given node.
    # Else, do:
    #     Note that the node already contains the given key.
    #     Return the given node.
    pass


def remove(bst, key):
    pass


def inorder(bst):
    pass
