class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this queue:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def enqueue(queue, value):
    # Create a new node containing the given value..
    # If the stack is empty, then:
    #     Set the head to the new node.
    # Else, do:
    #     Set the tail's next to the new node.
    # Set the tail to the new node.
    # Increment the size.
    pass


def dequeue(queue, value):
    # If the stack has one element, then:
    #     Unset the head and tail.
    # Else, do:
    #     Set the head to the head's next.
    # Return the old head's value.
    # Decrement the size.
    pass


def peek(queue):
    # Return the head's value.
    pass
