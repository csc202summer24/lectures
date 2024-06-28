import sys


def fibonacci(n):
    """
    Compute the n'th Fibonacci number.

    :param n: A non-negative integer
    :return: The n'th Fibonacci number
    """
    current = previous = None

    # This loop runs n + 1 times, so this function performs
    #  T(n) = 2 + c * (n + 1) + 1 operations, and has complexity O(n).

    for i in range(n + 1):
        if i == 0:
            current = 0
        elif i == 1:
            previous = current
            current = 1
        else:
            temp = previous
            previous = current
            current = current + temp

    return current


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
