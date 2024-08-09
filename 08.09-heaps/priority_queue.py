class PriorityQueue:
    """ A prioritized collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0


def enqueue(pqueue, value):
    # If the size is equal to the capacity, then:
    #     Double the capacity.
    #     Create a new array of that new capacity + 1.
    #     Copy each element of the old array into the new array.
    #     Set the backing array to the new array.
    #
    # Start with index i being that of the next leaf (i = size + 1).
    # Set the i'th element to the given value.
    #
    # NOTE: Because the tree is complete, it cannot degenerate into a linked
    #       list, and enqueueing requires at most O(log n) swaps. Roughly
    #       half of the nodes in the tree are in the lowest level -- most
    #       nodes probably belong near the bottom of the tree. Since values
    #       are enqueued at the bottom of the tree, the average value only
    #       requires O(1) swaps to get to where it belongs...
    #
    # While i is not the index of the root (i != 1), do:
    #     If the i'th element is greater than its parent (index i // 2), then:
    #         Swap the i'th element with its parent's element.
    #         Set index i to its parent's index.
    #     Else, do:
    #         Note that all elements are already in the right place.
    #
    # Increment the size.
    pass


def dequeue(pqueue):
    # Start with index i being that of the root (i = 1).
    # Set the i'th element to that of the last leaf (index size).
    #
    # NOTE: ...but by the same line of reasoning, if most nodes belong at the
    #       bottom of the tree, then moving a value into the root probably
    #       moves it very far from where it belongs. The average value then
    #       requires O(log n) swaps to get back to where it belongs.
    #
    # While i is not the index of a leaf (index 2i is in-bounds), do:
    #     If the right child exists (index 2i + 1 is in-bounds) and the right
    #      child (index 2i + 1) is larger than the left child (index 2i), then:
    #         If the i'th element is smaller than the right child, then:
    #             Swap the i'th element with its right child's element.
    #             Set i to the right child's index.
    #         Else, do:
    #             Note that all elements are already in the right place.
    #     Else, do:
    #         If the i'th element is smaller than the left child, then:
    #             Swap the i'th element with its left child's element.
    #             Set i to the left child's index.
    #         Else, do:
    #             Note that all elements are already in the right place.
    #
    # Decrement the size.
    pass


def peek(pqueue):
    # Return the root (index 1).
    pass
