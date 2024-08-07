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
    # TODO: Add the new value as a leaf, either the next leaf of the lowest
    #       level, or the first leaf of a new level, so as to maintain the
    #       completeness of the tree. Then rearrange nodes as necessary in
    #       order to maintain the heap property.
    pass


def dequeue(pqueue):
    # TODO: Remove the root, which always has highest priority. Put something
    #       else in the root's place, so that the tree is still a tree. In
    #       particular, note that the only node that can truly be removed while
    #       maintaining the completeness of the tree is the last leaf of the
    #       lowest level. Then rearrange nodes as necessary in order to
    #       maintain the heap property.
    pass


def peek(pqueue):
    # NOTE: The elements in a priority queue will be arranged in a heap:
    #         * Each element is contained in a node in a complete binary tree.
    #         * Each node's value is no smaller than its childrens' values.
    #       ...thus, the root must contain the largest value. The second
    #       largest value must be in one of the root's children, but there is
    #       no guarantee as to which one; the smallest value must be in a leaf,
    #       but there is no guarantee as to which one.
    #
    #       This tree will be represented as an array:
    #         * The parent of index i is index i // 2.
    #         * The children of index i are indices 2i and 2i + 1.
    #       ...the root always has index 1, and index 0 is always empty.
    #
    # Return the element at index 1.
    pass
