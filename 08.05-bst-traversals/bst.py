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
    # Set the root to the result of removing from the root.
    pass


def _remove(bst, node, key):
    # If the node does not exist, then:
    #     Note that the key does not exist.
    # Else if the node contains the given key, then:
    #     If the node does not have a right child, then:
    #         Decrement the size.
    #         Return the left child.
    #     Else if the node does not have a left child, then:
    #         Decrement the size.
    #         Return the right child.
    #     Else, do:
    #
    #         NOTE: If the node has two children, we need to keep the node (the
    #               only thing connecting those children), but we need to
    #               replace its key (the thing actually being removed).
    #               Consider the smallest key in the right subtree:
    #                 * By definition, it's bigger than any to the left.
    #                 * By construction, it's smaller than any to the left.
    #               ...that smallest key to the right can take our place.
    #
    #         Find the smallest key in the right subtree.
    #         Set the right child to the result of removing that smallest key
    #          from the right child.
    #         Set the node's key to that smallest key.
    #         Return the given node.
    #
    # Else if the node's key is larger than the given key, then:
    #     Set the left child to the result of recursing on that child.
    #     Return the given node.
    # Else, do:
    #     Set the right child to the result of recursing on that child.
    #     Return the given node.
    pass


def _min(node):
    # If the node does not exist, then:
    #     Note that there is no smallest key.
    # Else if the node has no left child, then:
    #     Return the node's key.
    # Else, do:
    #     Return the result of recursing on the left child.


def inorder(bst):
    # Return the result of traversing the tree's root.
    pass


def _traverse(node):
    # If the node is None, then:
    #     Return (whatever we were asked to return, e.g, a queue).
    # Else, do:
    #     Recurse on the node's left child.
    #     Mark the node as traversed (do whatever we came here to do, e.g, put
    #      the node into a queue).
    #     Recurse on the node's right child.
    #     Return (whatever we were asked to return, e.g, a queue).
    pass
