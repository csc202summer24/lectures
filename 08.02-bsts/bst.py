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
    # Return the result of finding at the root.
    pass


def _find(node, key):
    # If the node does not exist, then:
    #     Note that the key does not exist.
    # Else if the node contains the given key, then:
    #     Note that the node contains the key.
    # Else if the node's key is larger than the given key, then:
    #     Return the result of recursing on the left child.
    # Else, do:
    #     Return the result of recursing on the right child.
    pass


def insert(bst, key):
    # NOTE: See below: the recursive function returns the resulting root,
    #       which may be different from the original root, so it needs to
    #       replace that original root within the BST. In general, every
    #       time we insert, we replace the node at which we inserted.
    #
    # Set the root to the result of inserting at the root.
    #
    # NOTE: It's possible that the BST already contained the given key. Not
    #       all insertions necessarily create new Nodes, and thus not all
    #       insertions necessarily increment the size.
    pass


def _insert(bst, node, key):
    # NOTE: This recursive function will take as argument an existing Node,
    #       which may or may not be None -- the root of a subtree which
    #       may or may not be empty. It will return a new Node -- the root
    #       of a new subtree, which may or may not have the same root.
    #
    # If the node does not exist, then:
    #     Create a new node with no children containing the given key.
    #     Increment the size.
    #     Return the new node.
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
