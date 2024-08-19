class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    #
    # Start with the current node being the head at that hash code.
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def insert(dct, key, value):
    # If the size equals the capacity, then:
    #     NOTE: Ideally, the new capacity would be prime, but computing the
    #           next prime would be too expensive; doubling and adding one is
    #           a reasonable approximation.
    #
    #     Create a new array of double the capacity plus one.
    #
    #     NOTE: Copying the elements over to the new array is not as simple
    #           as in array lists -- since the capacity has changed, the hash
    #           codes of all existing elements has also changed.
    #
    #     For i from 0 to size - 1, do:
    #         Start with the current node being the head at i.
    #         While the current node is not None, do:
    #
    #             NOTE: When rehashing, every key being rehashed was already
    #                   in the dictionary, thus, every key being rehashed is
    #                   necessarily unique. We need not check for duplicates.
    #
    #             Rehash the current node's key; mod it by the new capacity.
    #             Reinsert the current node at the head at the new hash code.
    #             Set the current node to the current node's next.
    #
    #     Set the dictonary's array to the new array.
    #
    # NOTE: The new key's hash code depends on the capacity, so it cannot be
    #       computed until after any rehashing is complete.
    #
    # Hash the given key and mod it by the capacity.
    #
    # If the head at the hash code is None, then:
    #     Create a new node containing the given key and value.
    #     Set the head at the hash code to the new node.
    #     Increment the size.
    # Else, do:
    #     Start with the current node being the head at the hash code.
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None:
    #             Create a new node containing the given key and value.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
    #     Set the current node's value to the given value.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    #
    # If the head at the hash code contains the given key, then:
    #     Set the head at the hash code to its next.
    # Else, do:
    #     Start with the current node being the head at the hash code.
    #     While the current node's next's key is not the given key, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    # Decrement the size.
    # Return the "unlinked" node's value.
    pass


def keys(dct):
    pass
