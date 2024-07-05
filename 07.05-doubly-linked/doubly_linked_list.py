class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing doubly linked list:
        self.head = None
        # The tail of the backing doubly linked list:
        self.tail = None;
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a doubly linked list """

    def __init__(self, value, previous, next):
        # The value contained in this node:
        self.value = value
        # The previous node in the linked list:
        self.previous = previous
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # NOTE: This seems clever, but it only improves the worst-case scenario
    #       from n nodes to n/2 nodes, and n/2 is still O(n)...it still does
    #       not support fast "random access".
    #
    # If the given index is in the first half of the list, then:
    #     Start with the current node being the head.
    #     For i from 0 to idx, do:
    #         Set the current node to the current node's next.
    # Else, do:
    #     Start with the current node being the tail.
    #     For i from size - 1 to idx, do:
    #         Set the current node to the current node's prev.
    # Return the current node's value.
    pass


def set(lst, idx, value):
    # Start with the current node being the head.
    # For i from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Set the current node's value to the given value.
    pass


def add(lst, idx, value):
    # Create a new node containing the given value.
    #
    # NOTE: In a singly linked list, we special case adding to the head; thus,
    #       in a doubly linked list, we special case both head and tail.
    #
    # If the size is 0, then:
    #     Set the new node's prev and next to None.
    #     Set the head and the tail to the new node.
    # Else if the given index is 0, then:
    #     Set the new node's prev to None.
    #     Set the new node's next to the head.
    #     Set the head's prev to the new node.
    #     Set the head to the new node.
    # Else if the given index is equal to the size, then:
    #     Set the new node's prev to the tail.
    #     Set the new node's next to None.
    #     Set the tail's next to the new node.
    #     Set the tail to the new node.
    #
    # Else, do:
    #     Start with the current node being the head.
    #     For i from 0 to idx - 1, do:
    #         Set the current node to the current node's next.
    #
    #     NOTE: Just as with singly linked lists, we first find the previous
    #           node. With doubly linked lists, we must update not only that
    #           previous node, but also its next node.
    #
    #     Set the new node's next to the current node's next.
    #     Set the current node's next to the new node.
    #     Set the new node's next's prev to the new node.
    #     Set the new node's prev to the current node.
    # Increment the size.
    pass


def remove(lst, idx):
    # TODO: Update remove the same way as add: three special cases instead of
    #       one, and generally update prev in addition to next.
    #
    # If the given index is 0, then:
    #     Set the head to the head's next.
    # Else, do:
    #     Start with the current node being the head.
    #     For i from 0 to idx - 1, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    # Decrement the size.
    # Return the "unlinked" node's value.
    pass
