import re


def string_to_grid_by_row_and_spaces(s: str) -> list[list[str]]:
    """Convert a string to a grid by splitting on newlines, then spaces in each row.

    First splits by newlines to get rows, then splits each row by whitespace.

    Args:
        s: Input string with rows separated by newlines

    Returns:
        A list of lists of strings, where each inner list is a row split by spaces

    Example:
        >>> string_to_grid_by_row_and_spaces("1 2 3\\n4 5 6")
        [['1', '2', '3'], ['4', '5', '6']]
    """
    if not s:
        return []

    # Normalize line endings
    normalized = s.replace("\r\n", "\n").replace("\r", "\n")

    # Split by newlines to get rows
    lines = normalized.split("\n")

    # Split each line by whitespace (one or more spaces)
    grid = []
    for line in lines:
        if line.strip():  # Skip empty lines
            # Split by one or more spaces
            row = re.split(r"\s+", line.strip())
            grid.append(row)

    return grid


def get_column_values(data_rows: list[list[str]], col_idx: int) -> list[int]:
    """Extract integer values from a specific column in data rows.

    Args:
        data_rows: List of rows, where each row is a list of strings
        col_idx: Column index to extract values from

    Returns:
        List of integer values from the specified column

    Example:
        >>> get_column_values([["5", "10"], ["3", "20"]], 0)
        [5, 3]
        >>> get_column_values([["5", "10"], ["3", "20"]], 1)
        [10, 20]
    """
    column_values = []
    for row in data_rows:
        if col_idx < len(row):
            try:
                value = int(row[col_idx])
                column_values.append(value)
            except (ValueError, IndexError):
                continue
    return column_values


def apply_operation(operation: str, values: list[int]) -> int | None:
    """Apply an operation to a list of values.

    Args:
        operation: Operation to apply ("+" for sum, "*" for product)
        values: List of integer values to operate on

    Returns:
        Result of the operation, or None if operation is unknown

    Example:
        >>> apply_operation("+", [1, 2, 3])
        6
        >>> apply_operation("*", [2, 3, 4])
        24
        >>> apply_operation("?", [1, 2, 3]) is None
        True
    """
    if not values:
        return None

    if operation == "+":
        return sum(values)
    elif operation == "*":
        result = 1
        for val in values:
            result *= val
        return result
    else:
        return None


def solve(input_lines: str) -> int:
    """Solve the puzzle.

    The last row contains operations (+ or *) that should be applied to each
    column. For each column, apply the operation from the last row to all
    values in that column from the other rows.

    Args:
        input_lines: Input string with rows of numbers and a last row of operations

    Returns:
        The sum of results from applying operations to each column
    """
    grid = string_to_grid_by_row_and_spaces(input_lines)

    if not grid or len(grid) < 2:
        return 0

    # Last row contains the operations
    operations_row = grid[-1]
    # Other rows contain the data
    data_rows = grid[:-1]

    total = 0

    # For each column, apply the operation to all values in that column
    for col_idx in range(len(operations_row)):
        operation = operations_row[col_idx]
        column_values = get_column_values(data_rows, col_idx)

        if not column_values:
            continue

        result = apply_operation(operation, column_values)
        if result is not None:
            total += result

    return total


def main():
    from data import get_input_string

    input_lines = get_input_string("data/2025/6.txt")
    result = solve(input_lines)
    print(result)


if __name__ == "__main__":
    main()
