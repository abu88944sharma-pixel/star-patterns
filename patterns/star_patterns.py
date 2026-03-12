def generate_right_angle_pattern(rows: int) -> str:
    """
    Generates a right-angled triangle star pattern string.

    Args:
        rows (int): The number of rows in the pattern. Must be a non-negative integer.

    Returns:
        str: The generated star pattern string.

    Raises:
        ValueError: If rows is negative.
        TypeError: If rows is not an integer.
    """
    if not isinstance(rows, int):
        raise TypeError(f"Rows must be an integer, got {type(rows).__name__}.")
    
    if rows < 0:
        raise ValueError("The number of rows cannot be negative.")

    lines = ["*" * i for i in range(1, rows + 1)]
    return "\n".join(lines)


if __name__ == "__main__":
    try:
        print(generate_right_angle_pattern(5))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
