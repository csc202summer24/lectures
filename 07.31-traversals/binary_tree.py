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
    # Return the result of traversing the tree's root.
    pass


def _traverse(node):
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
    # NOTE: This could certainly be done iteratively, as with postorder, by
    #       rearranging the recursive calls. Alternatively, any recursive
    #       function can be made iterative by maintaining a "stack of jobs".
    #
    # Create a new, empty stack.
    # Push the root onto the stack.
    #
    # While the stack is not empty, do:
    #     Pop a node off of the stack.
    #     Mark the node as traversed (do whatever we came here to do, e.g, put
    #      the node into a queue).
    #
    #     NOTE: We want to traverse the left before the right, so the left must
    #           be popped before the right, so the right must be pushed first.
    #
    #     If the node has a right child, then:
    #         Push the right child onto the stack.
    #     If the node has a left child, then:
    #         Push the left child onto the stack.
    #
    # Return (whatever we were asked to return, e.g, a queue).
    pass


def levelorder(tree):
    # NOTE: Since stacks are LIFO, siblings are pushed before children, thus,
    #       children are popped and traversed before siblings. If we instead
    #       wish to traverse siblings first, we must instead use a FIFO queue.
    #
    # Create a new, empty queue.
    # Enqueue the root onto the queue.
    #
    # While the queue is not empty, do:
    #     Dequeue a node off of the queue.
    #     Mark the node as traversed (do whatever we came here to do, e.g, put
    #      the node into a queue -- NOT the "queue of jobs").
    #
    #     If the node has a left child, then:
    #         Enqueue the left child onto the queue.
    #     If the node has a right child, then:
    #         Enqueue the right child onto the queue.
    #
    # Return (whatever we were asked to return, e.g, a queue -- NOT of jobs).
    pass
