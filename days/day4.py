def string_to_grid(s: str, sep: str = "\n") -> list[list[str]]:
    """Convert a string into a grid by splitting on a separator character.

    Splits the input string by the separator character and returns a list
    of lists of strings representing the grid rows. Each row is a list of
    characters. Handles different line ending formats (\\n, \\r\\n, \\r).

    Args:
        s: Input string to convert to grid (may include line endings)
        sep: Separator character to split on (default: newline)

    Returns:
        A list of lists of strings representing grid rows (jagged array)

    Example:
        >>> string_to_grid("ABC\\nDEF\\nGHI")
        [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        >>> string_to_grid("A,B,C", sep=",")
        [['A'], ['B'], ['C']]
    """
    if not s:
        return []

    # Normalize line endings - replace \r\n with \n, then \r with \n
    normalized = s.replace("\r\n", "\n").replace("\r", "\n")

    # Split on the separator (or newline if default)
    if sep == "\n":
        lines = normalized.split("\n")
    else:
        lines = normalized.split(sep)

    # Filter out empty lines and convert each line to a list of characters
    return [list(line) for line in lines if line]


def check_adjacent(grid: list[list[str]], row: int, col: int, char: str, n: int) -> bool:
    """Check adjacent positions for a specific character.

    Checks all 8 adjacent positions (up, down, left, right, and 4 diagonals)
    around the given coordinate. Returns True if there are less than n
    occurrences of the specified character. Handles jagged arrays (rows of
    different lengths).

    Args:
        grid: A grid represented as a list of lists of strings (may be jagged)
        row: Row index (0-based)
        col: Column index (0-based)
        char: Character to search for in adjacent positions
        n: Threshold - returns True if count < n

    Returns:
        True if there are less than n occurrences of char in adjacent positions

    Example:
        >>> grid = ["ABC", "DEF", "GHI"]
        >>> check_adjacent(grid, 1, 1, 'A', 2)
        True
        >>> check_adjacent(grid, 0, 0, 'B', 1)
        False
    """
    if not grid or row < 0 or col < 0:
        return False

    rows = len(grid)
    if row >= rows:
        return False

    # Check if the current position is valid (handles jagged arrays)
    if col >= len(grid[row]):
        return False

    count = 0
    # Check all 8 adjacent positions
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),  # Top row
        (0, -1),
        (0, 1),  # Middle row (left, right)
        (1, -1),
        (1, 0),
        (1, 1),  # Bottom row
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check bounds (handles jagged arrays by checking each row's length)
        if 0 <= new_row < rows and 0 <= new_col < len(grid[new_row]):
            if grid[new_row][new_col] == char:
                count += 1

    return count < n


def solve(input_str: str) -> int:
    """Solve the puzzle by checking adjacent positions in the grid.

    Converts the input string to a grid and counts '@' positions that have
    less than 4 adjacent '@' characters.

    Args:
        input_str: Input string representing the grid

    Returns:
        The count of '@' positions with less than 4 adjacent '@' characters
    """
    grid = string_to_grid(input_str)
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if position is '@' and has less than 4 adjacent '@' characters
            if grid[row][col] == "@" and check_adjacent(grid, row, col, "@", 4):
                count += 1

    return count


def main():
    from data import get_input

    input_str = "\n".join(get_input("data/2025/4.txt"))
    result = solve(input_str)
    print(result)


if __name__ == "__main__":
    main()
