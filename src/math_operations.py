def add_numbers(a, b):
    """Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract_numbers(a, b):
    """
    Subtract one number from another.

    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.

    Returns:
        float: The result of the subtraction.
    """
    return a - b


def multiply_numbers(a, b):
    """Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide_numbers(a, b):
    """Divide one number by another.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("The denominator cannot be zero.")
    return a / b
