from days.day2 import parse_range


def split_by_double_newline(s: str) -> list[str]:
    """Split a string by double newline into parts.

    Args:
        s: Input string to split

    Returns:
        A list of strings (first part, second part, ...)

    Example:
        >>> split_by_double_newline("part1\\n\\npart2")
        ['part1', 'part2']
    """
    parts = s.split("\n\n")
    return parts


def solve(input: str) -> int:
    total = 0
    fresh_ids: set[tuple[int, int]] = set()
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


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping intervals.

    Args:
        intervals: List of (start, end) tuples

    Returns:
        List of merged non-overlapping intervals

    Example:
        >>> merge_intervals([(1, 5), (3, 7), (10, 12)])
        [(1, 7), (10, 12)]
    """
    if not intervals:
        return []

    # Sort intervals by start value
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]

    for current_start, current_end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]

        # If current interval overlaps with the last merged interval, merge them
        if current_start <= last_end + 1:  # +1 to handle adjacent intervals
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def count_numbers_in_intervals(intervals: list[tuple[int, int]]) -> int:
    """Count total numbers in merged intervals without storing individual numbers.

    Args:
        intervals: List of (start, end) tuples (should be merged/non-overlapping)

    Returns:
        Total count of numbers across all intervals

    Example:
        >>> count_numbers_in_intervals([(1, 5), (10, 12)])
        8  # 5 numbers from 1-5, 3 numbers from 10-12
    """
    return sum(end - start + 1 for start, end in intervals)


def solve2(input: str) -> int:
    """Solve part 2 by merging intervals and counting total numbers.

    Memory-efficient approach: merges overlapping intervals and calculates
    total count without storing individual numbers.
    """
    parts = split_by_double_newline(input)
    intervals: list[tuple[int, int]] = []

    # Collect all intervals
    for line in parts[0].split("\n"):
        if line.strip():
            start, end = parse_range(line.strip())
            intervals.append((start, end))

    # Merge overlapping intervals
    merged = merge_intervals(intervals)

    # Count total numbers in merged intervals
    total_count = count_numbers_in_intervals(merged)

    return total_count


def main():
    from data import get_input_string

    input = get_input_string("data/2025/5.txt")
    print(solve(input))
    print(solve2(input))


if __name__ == "__main__":
    main()
