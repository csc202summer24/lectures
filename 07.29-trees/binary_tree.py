class BinaryTree:
    """ A binary tree """

    def __init__(self, value = None):
        if value is None:
            # The root of this empty tree:
            self.root = None
            # The number of nodes in this tree:
            self.size = 0
        else:
            # The root of this singleton tree:
            self.root = Node(value, None, None)
            # The number of nodes in this tree:
            self.size = 1


class Node:
    """ A single node in a binary tree """

    def __init__(self, value, left, right):
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def combine(value, left, right):
    # Create a new tree of one node containing the value.
    # Set the new tree's root's left child to the left subtree's root.
    # Set the new tree's root's right child to the right subtree's root.
    # Set the new tree's size to the left's size + the right's size + 1.
    pass


def postorder(tree):
    # NOTE: Since trees are recursively defined, we would like to traverse them
    #       with a recursive function, but we must bear in mind that BinaryTree
    #       is not recursive -- it doesn't contain more BinaryTrees -- rather,
    #       Node is recursive...
    #
    # Return the result of traversing the tree's root.
    pass


def _traverse(node):
    # NOTE: A tree is a linked list where each node may have multiple children.
    #       Just as linked list ops. must begin at the head, tree ops. must
    #       begin at the root. In a post-order traversal, however, we cannot
    #       immediately traverse the root, because nodes must generally be
    #       traversed after their children.
    #
    # If the node is None, then:
    #     Return (whatever we were asked to return, e.g, a queue).
    # Else, do:
    #     Recurse on the node's left child.
    #     Recurse on the node's right child.
    #     Mark the node as traversed (do whatever we came here to do, e.g, put
    #      the node into a queue).
    #     Return (whatever we were asked to return, e.g, a queue).
    pass


def preorder(tree):
    pass


def levelorder(tree):
    pass
