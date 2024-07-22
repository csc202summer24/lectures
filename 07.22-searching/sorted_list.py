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
    pass


def remove(lst, idx):
    pass


def find(lst, value):
    # NOTE: Since the list is known to be sorted, we ought to be able to make
    #       more clever choices: if the middle element is smaller than the
    #       given value, for example, we ought to be able to discard the entire
    #       first half of the list without ever searching it.
    #
    # Set a low index to 0 and a high index to size - 1 -- these represent the
    #  bounds of the sublist that we have yet to search.
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
    # NOTE: To get here, low > high, meaning that the sublist to be searched is
    #       empty and we never found the given element.
    #
    # Return -1.
    pass


def create(array, size):
    pass
