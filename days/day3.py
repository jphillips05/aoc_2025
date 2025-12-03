def string_to_ints(s: str) -> list[int]:
    """Convert a string into a list of integers.

    Each character in the string is converted to an integer.

    Args:
        s: A string containing digits

    Returns:
        A list of integers, one for each character

    Example:
        >>> string_to_ints("123")
        [1, 2, 3]
        >>> string_to_ints("5192")
        [5, 1, 9, 2]
    """
    return [int(char) for char in s]


def highest_number(digits: list[int], n: int = 2) -> int:
    """Return the highest possible n-digit number from a list of single-digit integers.

    Finds all possible n-digit numbers by selecting n digits in their original order,
    and returns the highest one.

    Args:
        digits: A list of single-digit integers (0-9)
        n: The number of digits in the number to find (default: 2)

    Returns:
        The highest n-digit number that can be formed

    Example:
        >>> highest_number([1, 2, 3])
        23
        >>> highest_number([5, 1, 9, 2])
        92
        >>> highest_number([1, 2, 3, 4], n=3)
        234
        >>> highest_number([0, 1, 2])
        12
    """
    if len(digits) < n:
        return 0

    max_num = 0  # Cache the highest number we've seen

    # Use iterative approach with a stack to avoid recursion overhead
    # Stack stores (start_index, current_number, digits_used)
    stack = [(0, 0, 0)]

    while stack:
        start_idx, current_num, digits_used = stack.pop()

        if digits_used == n:
            # We've built a complete number, update max
            max_num = max(max_num, current_num)
        else:
            # Check if this branch could potentially beat max_num
            # Calculate the maximum possible number we could form from here
            remaining = n - digits_used
            # Best case: fill remaining digits with 9s
            max_possible = current_num
            for _ in range(remaining):
                max_possible = max_possible * 10 + 9

            # If even the best case can't beat max_num, skip this branch
            if max_possible <= max_num:
                continue

            # Continue building the number
            for i in range(start_idx, len(digits) - remaining + 1):
                new_num = current_num * 10 + digits[i]
                stack.append((i + 1, new_num, digits_used + 1))

    return max_num


def solve(input_lines: list[str], n: int = 2) -> int:
    """Process input lines and return the sum of highest 2-digit numbers.

    For each line, converts it to a list of digits, finds the highest 2-digit number,
    and sums all the results.

    Args:
        input_lines: List of strings containing digits

    Returns:
        The sum of all highest 2-digit numbers

    Example:
        >>> solve(["123", "5192"])
        115  # 23 + 92
    """
    total = 0
    for line in input_lines:
        if line.strip():
            digits = string_to_ints(line.strip())
            total += highest_number(digits, n)
    return total


def main():
    from data import get_input

    input_lines = get_input("data/2025/3.txt")
    total = solve(input_lines)
    total_12 = solve(input_lines, n=12)
    print(total)
    print(total_12)


if __name__ == "__main__":
    main()
