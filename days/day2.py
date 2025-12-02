def parse_range(range_str: str) -> tuple[int, int]:
    """Split a string on '-' and return two integers.

    Args:
        range_str: A string like "1-5" or "10-20"

    Returns:
        A tuple of two integers (start, end)

    Example:
        >>> parse_range("1-5")
        (1, 5)
        >>> parse_range("10-20")
        (10, 20)
    """
    parts = range_str.split("-")
    if len(parts) != 2:
        raise ValueError(f"Expected format 'number-number', got '{range_str}'")
    return int(parts[0]), int(parts[1])


def range_list(start: int, end: int) -> list[int]:
    """Return a list of integers from start to end (inclusive).

    Args:
        start: The starting number
        end: The ending number (inclusive)

    Returns:
        A list of integers from start to end

    Example:
        >>> range_list(1, 5)
        [1, 2, 3, 4, 5]
        >>> range_list(5, 1)
        [5, 4, 3, 2, 1]
        >>> range_list(3, 3)
        [3]
    """
    if start <= end:
        return list(range(start, end + 1))
    else:
        return list(range(start, end - 1, -1))


def is_valid_id(id_num: int) -> bool:
    """Check if an ID is valid by comparing both halves of its string representation.

    An ID is invalid if both halves are the same. An ID is valid if the halves differ
    or if it has an odd length.

    Args:
        id_num: The ID number to validate

    Returns:
        True if the ID is valid (halves differ or odd length),
        False if invalid (halves are the same)

    Example:
        >>> is_valid_id(1212)
        False  # "12" == "12", invalid
        >>> is_valid_id(1234)
        True  # "12" != "34", valid
        >>> is_valid_id(123)
        True  # odd length, valid
    """
    id_str = str(id_num)
    length = len(id_str)

    # Can't split odd-length strings evenly, so they're valid
    if length % 2 != 0:
        return True

    mid = length // 2
    first_half = id_str[:mid]
    second_half = id_str[mid:]

    # If halves are the same, ID is invalid
    return first_half != second_half


def process_range(range_str: str) -> list[int]:
    """Process a range string and return a list of invalid IDs.

    Parses the range string, generates all numbers in that range, checks each
    for validity, and collects the invalid ones.

    Args:
        range_str: A string like "1-5" or "10-20"

    Returns:
        A list of invalid ID numbers from the range

    Example:
        >>> process_range("1212-1214")
        [1213, 1214]
        >>> process_range("1212-1212")
        []
    """
    start, end = parse_range(range_str)
    numbers = range_list(start, end)
    invalid_ids = []

    for num in numbers:
        if not is_valid_id(num):
            invalid_ids.append(num)

    return invalid_ids


def solve(input_lines: list[str]) -> int:
    """Process input lines and return the sum of all invalid IDs.

    Args:
        input_lines: List of range strings like ["1-5", "10-20"]

    Returns:
        The sum of all invalid IDs found across all ranges

    Example:
        >>> solve(["1212-1214", "1234-1236"])
        3702
    """
    all_invalid_ids = []

    for line in input_lines:
        if line.strip():  # Skip empty lines
            invalid_ids = process_range(line.strip())
            all_invalid_ids.extend(invalid_ids)

    return sum(all_invalid_ids)


def main():
    from data import get_input

    input_lines = get_input("data/2025/2.txt")
    total = solve(input_lines[0].split(","))
    print(total)


if __name__ == "__main__":
    main()
