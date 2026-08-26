import math
n=int(input('enter no'))
def calculate_factorial(n: int) -> int:
    """Calculates n! for 0 <= n <= 12 using math.factorial."""
    if not (0 <= n <= 12):
        raise ValueError("n must be between 0 and 12, inclusive.")
    return math.factorial(n)
calculate_factorial(n)
