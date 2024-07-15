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
    # NOTE: This would be O(1) regardless of whether we added to the head or to
    #       the tail, since both head and tail are directly accessible...
    #
    # Create a new node containing the given value.
    # If the queue is empty, then:
    #     Set the head to the new node.
    # Else, do:
    #     Set the tail's next to the new node.
    # Set the tail to the new node.
    # Increment the size.
    pass


def dequeue(queue, value):
    # NOTE: ...but removing from the head is O(1) whereas removing from the
    #       tail is O(n), so the tail has to be the back of the queue.
    #
    # Set the head to the head's next.
    # If the queue is of size 1, then:
    #     Set the tail to None.
    # Decrement the size.
    # Return the unlinked node's value.
    pass


def peek(queue):
    # Return the head's value.
    pass
