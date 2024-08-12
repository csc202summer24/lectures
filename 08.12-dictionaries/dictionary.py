class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    # Return that element in the backing array.
    pass


def insert(dct, key, value):
    # NOTE: The general idea is to convert keys back into array indices, as
    #       arrays can be indexed in constant time. This only works as long
    #       as we can guarantee that no two keys get converted into the same
    #       index; we currently have no way of knowing otherwise if a value
    #       is associated with the same key in the event of a collision...
    #
    # Hash the given key and mod it by the capacity.
    # If that element in the backing array exists, then:
    #     Set that element in the backing array to the given value.
    # Else, do:
    #     Set that element in the backing array to the given value.
    #     Increment the size.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    # Unset that element in the backing array.
    # Decrement the size.
    # Return the "unset" element.
    pass


def keys(dct):
    pass
