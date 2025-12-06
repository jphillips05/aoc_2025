import re


def string_to_grid(s: str, sep: str | re.Pattern[str] = "\n") -> list[list[str]]:
    """Convert a string into a grid by splitting on a separator character or regex.

    Splits the input string by the separator (string or regex pattern) and returns
    a list of lists of strings representing the grid rows. Each row is a list of
    characters. Handles different line ending formats (\\n, \\r\\n, \\r).

    Args:
        s: Input string to convert to grid (may include line endings)
        sep: Separator string or regex pattern to split on (default: newline)

    Returns:
        A list of lists of strings representing grid rows (jagged array)

    Example:
        >>> string_to_grid("ABC\\nDEF\\nGHI")
        [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        >>> string_to_grid("A,B,C", sep=",")
        [['A'], ['B'], ['C']]
        >>> string_to_grid("A  B  C", sep=re.compile(r"\\s+"))
        [['A'], ['B'], ['C']]
    """
    if not s:
        return []

    # Normalize line endings - replace \r\n with \n, then \r with \n
    normalized = s.replace("\r\n", "\n").replace("\r", "\n")

    # Split on the separator (string or regex pattern)
    if isinstance(sep, re.Pattern):
        # Use regex to split
        lines = sep.split(normalized)
    elif sep == "\n":
        lines = normalized.split("\n")
    else:
        lines = normalized.split(sep)

    # Filter out empty lines and convert each line to a list of characters
    return [list(line) for line in lines if line]


def count_adjacent(grid: list[list[str]], row: int, col: int, char: str) -> int:
    """Count adjacent positions matching a specific character.

    Checks all 8 adjacent positions (up, down, left, right, and 4 diagonals)
    around the given coordinate and returns the count of matching characters.
    Handles jagged arrays (rows of different lengths).

    Args:
        grid: A grid represented as a list of lists of strings (may be jagged)
        row: Row index (0-based)
        col: Column index (0-based)
        char: Character to search for in adjacent positions

    Returns:
        The count of adjacent positions matching the character

    Example:
        >>> grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        >>> count_adjacent(grid, 1, 1, 'A')
        1
    """
    if not grid or row < 0 or col < 0:
        return 0

    rows = len(grid)
    if row >= rows or col >= len(grid[row]):
        return 0

    count = 0
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < rows and 0 <= new_col < len(grid[new_row]):
            if grid[new_row][new_col] == char:
                count += 1

    return count


def check_adjacent(grid: list[list[str]], row: int, col: int, char: str, n: int) -> bool:
    """Check adjacent positions for a specific character.

    Checks all 8 adjacent positions (up, down, left, right, and 4 diagonals)
    around the given coordinate. Returns True if there are less than n
    occurrences of the specified character. Marks the position as 'x' if condition is met.
    Handles jagged arrays (rows of different lengths).

    Args:
        grid: A grid represented as a list of lists of strings (may be jagged)
        row: Row index (0-based)
        col: Column index (0-based)
        char: Character to search for in adjacent positions
        n: Threshold - returns True if count < n

    Returns:
        True if there are less than n occurrences of char in adjacent positions

    Example:
        >>> grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        >>> check_adjacent(grid, 1, 1, 'A', 2)
        True
        >>> check_adjacent(grid, 0, 0, 'B', 1)
        False
    """
    if not grid or row < 0 or col < 0:
        return False

    rows = len(grid)
    if row >= rows or col >= len(grid[row]):
        return False

    count = count_adjacent(grid, row, col, char)
    result = count < n
    if result:
        grid[row][col] = "x"
    return result


def solve(input_str: str, iterate_until_stable: bool = False) -> int:
    """Solve the puzzle by checking adjacent positions in the grid.

    Converts the input string to a grid and counts '@' positions that have
    less than 4 adjacent '@' characters. Marks matching positions as 'x'.

    Args:
        input_str: Input string representing the grid
        iterate_until_stable: If True, continue iterating until no new positions
            are marked in an iteration

    Returns:
        The count of '@' positions with less than 4 adjacent '@' characters
    """
    grid = string_to_grid(input_str)
    total_count = 0

    while True:
        # Collect positions to mark first (don't modify grid during check)
        positions_to_mark = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    # Use count_adjacent helper to check if position should be marked
                    if count_adjacent(grid, row, col, "@") < 4:
                        positions_to_mark.append((row, col))

        # Mark all positions at once
        for row, col in positions_to_mark:
            grid[row][col] = "x"

        iteration_count = len(positions_to_mark)
        total_count += iteration_count

        # If not iterating until stable, or no new positions were marked, we're done
        if not iterate_until_stable or iteration_count == 0:
            break

    return total_count


def main():
    from data import get_input

    input_str = "\n".join(get_input("data/2025/4.txt"))
    result = solve(input_str)
    result_loop = solve(input_str, iterate_until_stable=True)
    print(result)
    print(result_loop)


if __name__ == "__main__":
    main()
