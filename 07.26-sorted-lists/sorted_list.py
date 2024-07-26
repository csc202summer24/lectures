class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0


def insert(lst, value):
    # If the size is equal to the capacity, then:
    #     Double the capacity.
    #     Create a new array of that new capacity.
    #     Copy each element of the old array into the new array.
    #     Set the backing array to the new array.
    #
    # Set an index i to the size.
    # While i > 0 and the element at index i - 1 is > the given value, do:
    #     Set the element at index i to the element at index i - 1.
    #     Decrement i.
    # Set the element at that index in the backing array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # For i from idx to size - 1, do:
    #     Set the element at index i to the element at index i + 1.
    # Decrement the size.
    # Return the element that used to be at the given index.
    pass


def find(lst, value):
    # Set a low index to 0 and a high index to size - 1.
    #
    # While low <= high, do:
    #    Set a mid index to (low + high) / 2.
    #    If the element at the mid index is equal to the given value, then:
    #        Return the mid index.
    #    Else if it is less than the given value, then:
    #        Set the low index to mid + 1.
    #    Else if it is greater than the given value, then:
    #        Set the high index to mid - 1.
    #
    # Return -1.
    pass


def create(array, size):
    # NOTE: This is not the most efficient way to sort a list, but with the
    #       insert function already implemented, an insertion sort is trivial.
    #
    # Create a new sorted list.
    # For i from 0 to size - 1, do:
    #     Insert the element at index i in the array into the sorted list.
    # Return the sorted list.
    pass
