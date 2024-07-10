class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The length of the backing array -- since arrays cannot be expanded,
        #  we have to make an array that is initally bigger than it needs to
        #  be, which means we have to distinguish between size and capacity:
        self.capacity = 4

        # The backing array -- Python does not expose true arrays to the
        #  programmer, but we can pretend that a Python list is an array by
        #  avoiding any operations other than getting and setting elements:
        self.array = [None] * self.capacity

        # The number of elements in this list:
        self.size = 0


def get(lst, idx):
    # NOTE: With array lists, unlike linked lists, we don't have to iterate
    #       over the list to get to the desired index; we can jump directly
    #       there.
    #
    # Return the element at that index in the backing array.
    pass


def set(lst, idx, value):
    # Set the element at that index in the backing array to the given value.
    pass


def add(lst, idx, value):
    # NOTE: Since arrays have a fixed number of elements, it is possible that
    #       we don't have space for a new element, in which case we are forced
    #       to create a larger array. By doubling the capacity, *most*
    #       additions will find that the array already has enough space. On
    #       average, the "amortized" complexity will not require adding space.
    #
    # If the size is equal to the capacity, then:
    #     Double the capacity.
    #     Create a new array of that new capacity.
    #     Copy each element of the old array into the new array.
    #     Set the backing array to the new array.
    #
    # NOTE: In order to enable fast random access, elements' indices in the
    #       backing array need to match their indices in the list, which means
    #       that adding an element to the middle of the list requires shifting
    #       the elements after it "down" in the array.
    #
    # For i from size to idx + 1, do:
    #     Set the element at index i to the element at index i - 1.
    # Set the element at that index in the backing array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # For i from idx to size - 1, do:
    #     Set the element at index i to the element at index i + 1.
    # Decrement the size.
    # Return the element that used to be at the given index.
    pass
