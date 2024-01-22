def power(x, n):
    """
    This function is return the power of x to n using a loop.
    Time Complexity: O(n)

    Parameters:
    x - a number
    n - an integer > 0
    """
    result = x

    for _i in range(1, n):
        result *= x

    return result
