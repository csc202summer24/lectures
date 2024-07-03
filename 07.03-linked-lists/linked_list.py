class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # NOTE: Whenever we need to "traverse" the list, we have to start with the
    #       head node and follow the links down to the node we actually want.
    #
    # Start with the current node being the head.
    # For i from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def set(lst, idx, value):
    # Start with the current node being the head.
    # For i from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Set the current node's value to the given value.
    pass


def add(lst, idx, value):
    # NOTE: Any operation involving the first element in the list is special,
    #       because it means that the head reference might need to change.
    #
    # Create a new node containing the given value.
    # If the given index is 0 (including if the list is empty), then:
    #     Set the new node's next to the head.
    #     Set the head to the new node.
    # Else, do:
    #
    #     NOTE: In general, adding a node requires first finding the *previous*
    #           node in the list, because it's the previous node's next that
    #           needs to refer to the new node.
    #
    #     Start with the current node being the head.
    #     For i from 0 to idx - 1, do:
    #         Set the current node to the current node's next.
    #
    #     NOTE: Since we are adding a new node after the current node, anything
    #           that used to come after the current node now needs to come
    #           after the new node.
    #
    #     Set the new node's next to the current node's next.
    #     Set the current node's next to the new node.
    #
    # Increment the size.
    pass


def remove(lst, idx, value):
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
