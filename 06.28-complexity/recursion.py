import sys


def fibonacci(n):
    """
    Compute the n'th Fibonacci number.

    :param n: A non-negative integer
    :return: The (n - 1)'st and n'th Fibonacci numbers
    """

    # With naive recursion, this function's complexity is approximately
    #  O(1.65^n), not because it was written recursively...

    if n == 0:
        return (None, 0)
    elif n == 1:
        return (0, 1)
    else:

        # ...but because it does the same work multiple times. For example:
        #  1. Compute f(n - 1). By definition, f(n - 1) = f(n - 2) + f(n - 3).
        #  2. Compute f(n - 2) again.
        # Doing work recursively is not inherently inefficient; doing work
        #  multiple times is inefficient.
        # return fibonacci(n - 1) + fibonacci(n - 2)

        previous, current = fibonacci(n - 1)
        return (current, current + previous)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
