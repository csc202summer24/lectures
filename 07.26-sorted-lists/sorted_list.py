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
    # Sort the array.
    # Create a new sorted list containing the sorted array.
    # Return the sorted list.
    pass


def _merge(array_a, size_a, array_b, size_b):
    # Create a new array of size size_a + size_b.
    # Set indices i, j, and k to 0.
    #
    # While i < size_a and j < size_b, do:
    #    If the i'th element of array_a is <= the j'th of array_b, then:
    #        Set the k'th element of the new array to the i'th of array_a.
    #        Increment i.
    #    Else, do:
    #        Set the k'th element of the new array to the j'th of array_b.
    #        Increment j.
    #    Increment k.
    #
    # NOTE: Once we exit the main loop, one of the two arrays is empty. Any
    #       elements leftover in the other array must be both sorted and larger
    #       than all others; they just need to be added to the end.
    #
    # While i < size_a, do:
    #    Set the k'th element of the new array to the i'th of array_a.
    #    Increment i and k.
    #
    # While j < size_b, do:
    #    Set the k'th element of the new array to the j'th of array_b.
    #    Increment j and k.
    #
    # Return the new array
    pass


def _sort(array, size):
    # NOTE: It is possible to write an iterative merge sort, but a recursive
    #       approach is far more natural: a merge sort naturally involves
    #       identifying and solving smaller versions of the same problem.
    #
    # Create two new arrays, array_a and array_b, of size size / 2.
    # Copy the first half of the array's elements into array_a.
    # Copy the second half of the array's elements into array_b.
    # Recursively sort array_a.
    # Recursively sort array_b.
    # Return the result of merging array_a with array_b.
    pass
