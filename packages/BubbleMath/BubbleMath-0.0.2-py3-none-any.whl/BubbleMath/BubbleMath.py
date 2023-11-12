import gmpy2

def square_root(n: float, precision: int = None) -> float:
    """Calculate the square root of any number.

    Parameters:
    - n: The number to find the square root of.

    Returns:
    - float: The square root.

    Example:
    >>> square_root(4)
    2.0
    >>> square_root(2)
    1.4142135623730951
    """
    if precision != None:
        root = round(n**0.5, precision)
    else:
        root = n**0.5
    return root

def factorial(n: int) -> int:
    """Calculate the factorial of any non-negative integer.

    Parameters:
    - n (int): Non-negative integer.

    Returns:
    - int: Factorial of the input integer.

    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    result = gmpy2.mpz(1)
    for i in range(1, n + 1):
        result *= i
    return result

def quadratic(A: float, B: float, C: float, precision: int = 2) -> tuple[float, float]:
    """Calculate the roots of a quadratic equation.

    Parameters:
    - A: Coefficient of the quadratic term.
    - B: Coefficient of the linear term.
    - C: Constant term.
    - precision: Decimal point precision (default is 2).

    Returns:
    - tuple: Positive and negative roots of the equation.

    Example:
    >>> quadratic(1, -3, 2)
    (2.0, 1.0)
    >>> quadratic(3, -5, 2, precision=3)
    (1.0, 0.667)  # Rounded to 3 decimal places
    >>> quadratic(1, 0, -2, precision=5)
    (1.41421, -1.41421)  # Rounded to 5 decimal places
    """
    root_part = square_root((B**2) - (4 * (A * C)))
    pos_x = round((-B + root_part) / (2 * A), precision)
    neg_x = round((-B - root_part) / (2 * A), precision)
    return pos_x, neg_x
    
def pythag(a: float, b: float, precision: int = 1) -> float:
    """Calculate the length of the hypotenuse using the Pythagorean theorem.

    Formula: a^2 + b^2 = c^2

    Parameters:
    - a: Length of one side.
    - b: Length of the other side.
    - precision: Decimal point precision (default is 1).

    Returns:
    - float: Length of the hypotenuse.

    Example:
    >>> pythag(3, 4)
    5.0
    >>> pythag(5, 9, 1) # Round to 1 decimal place
    10.3
    >>> pythag(2.3, 3.9, 3) # Round to 3 decimal places
    4.528
    """
    return round(square_root(a**2 + b**2), precision)

def inverse_pythag(c: float, a: float, precision: int = 1) -> float:
    """Calculate the length of one missing side using the inverse Pythagorean theorem.

    Formula: b^2 = c^2 - a^2

    Parameters:
    - c: Length of the hypotenuse.
    - a: Length of the other side.
    - precision: Decimal point precision (default is 1).

    Returns:
    - float: Length of the missing side.

    Example:
    >>> inverse_pythag(5, 4)
    3.0
    >>> inverse_pythag(4.528, 2.3)
    3.9
    >>> inverse_pythag(10.3, 5, 1)
    9.0
    """
    return round(square_root(c**2 - a**2), precision)

if __name__ == "__main__":
    from timeit import default_timer as timer
    start = timer()
    print(factorial(10))
    # print(quadratic(3, -5, 2, precision=3))
    # print(square_root(2, precision=5))
    end = timer()
    print(f"Time Taken: {(end - start) * 1000}ms")