class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    # NOTE: If front < 0 and back < 0, there are no elements in the queue.
    #       If front <= back, the elements are the subarray [front:back + 1].
    #       Else, they are the subarray [front:capacity + 1] + [0:back + 1].
    #
    # If the queue is at capacity, then:
    #     Double the capactity.
    #     Create a new array of that new capacity.
    #     "Unwrap" the elements of the old array; copy them into the new array.
    #     Set the backing array to the new array.
    #
    # If the queue is empty, then:
    #     Set the front and back to 0.
    # Else, do:
    #     Increment the back and mod it by the capacity.
    # Set the element in the array at the back index to the given value.
    pass


def dequeue(queue):
    # If the queue has one element, then:
    #     Set the front and back to -1.
    # Else, do:
    #     Increment the front and mod it by the capacity.
    # Return the element in the array at the old front index.
    pass


def peek(queue):
    # Return the element in the array at the front index.
    pass
