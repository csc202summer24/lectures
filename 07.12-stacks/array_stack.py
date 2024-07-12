class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this stack:
        self.size = 0


def push(stack, value):
    # NOTE: Stacks are a special case of lists: they are lists that are only
    #       accessible at one terminus. In an array list, the end can be added
    #       or removed in O(1) time, whereas the beginning would require
    #       O(n) time, thus, the end ought to be the top-of-stack.
    #
    # If the size is equal to the capacity, then:
    #     Double the capacity.
    #     Create a new array of that new capacity.
    #     Copy each element of the old array into the new array.
    #     Set the backing array to the new array.
    # Set the element at index "size" in the backing array to the given value.
    # Increment the size.
    pass


def pop(stack):
    # Decrement the size.
    # Return the element at index "size" in the backing array.
    pass


def peek(stack):
    # Return the element at index "size - 1" in the backing array.
    pass
