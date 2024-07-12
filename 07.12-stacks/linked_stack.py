class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this stack:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def push(stack, value):
    # NOTE: Stacks are a special case of lists: they are lists that are only
    #       accessible at one terminus. In a singly linked list, the beginning
    #       can be accessed in O(1) time, whereas the end is accessed in O(n)
    #       time, thus, the beginning ought to be the top-of-stack.
    #
    # Create a new node containing the given value.
    # Set the new node's next to the head.
    # Set the head to the new node.
    # Increment the size.
    pass


def pop(stack):
    # Set the head to the head's next.
    # Decrement the size.
    # Return the "unlinked" node's value.
    pass


def peek(stack):
    # Return the head node's value.
    pass
