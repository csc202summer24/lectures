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
    # NOTE: Since the list is backed by an array to support efficient binary
    #       searches, we do need to be able to increase capacity, but we can
    #       assume that the list is always sorted -- we don't have to move the
    #       elements around; we just have to move them to a new array.
    #
    # If the size is equal to the capacity, then:
    #     Double the capacity.
    #     Create a new array of that new capacity.
    #     Copy each element of the old array into the new array.
    #     Set the backing array to the new array.
    #
    # NOTE: In order to maintain the sorted properties of the list, rather than
    #       allowing the caller to specify an index, we have to search for the
    #       appropriate index at which to insert the element. Once we find the
    #       right index, we still have to shift, so this can just be a linear.
    #
    # Set an index i to size.
    # While i > 0 and the element at index i - 1 is > the given value, do:
    #     Set the element at index i to the element at index i - 1.
    #     Decrement i.
    # Set the element at that index in the backing array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Removing from a sorted list is exactly the same as removing from
    #       an unsorted list. The only reason we had to change the logic for
    #       inserting is that we had to maintain sorted order, but removing an
    #       an element cannot possibly ruin that ordering anyways.
    #
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
