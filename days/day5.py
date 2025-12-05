from days.day2 import parse_range


def split_by_double_newline(s: str) -> tuple[str, str]:
    """Split a string by double newline into two parts.

    Args:
        s: Input string to split

    Returns:
        A tuple of two strings (first part, second part)

    Example:
        >>> split_by_double_newline("part1\\n\\npart2")
        ('part1', 'part2')
    """
    parts = s.split("\n\n")
    return parts


def solve(input: str) -> int:
    total = 0
    fresh_ids = set[set[int, int]]()
    parts = split_by_double_newline(input)
    for line in parts[0].split("\n"):
        start, end = parse_range(line.strip())
        fresh_ids.add((start, end))

    for items in parts[1].split("\n"):
        if items.strip():
            id = int(items.strip())
            if any(id >= start and id <= end for start, end in fresh_ids):
                total += 1

    return total


def main():
    from data import get_input_string

    input = get_input_string("data/2025/5.txt")
    print(solve(input))


if __name__ == "__main__":
    main()
