from days.day6 import (
    apply_operation,
    get_column_values,
    solve,
    string_to_grid_by_row_and_spaces,
    solve_part_2,
)


def test_string_to_grid_by_row_and_spaces():
    """Test converting string to grid by rows and spaces."""
    s = "1 2 3\n4 5 6\n+ * +"
    grid = string_to_grid_by_row_and_spaces(s)
    assert grid == [["1", "2", "3"], ["4", "5", "6"], ["+", "*", "+"]]


def test_string_to_grid_by_row_and_spaces_multiple_spaces():
    """Test with multiple spaces between numbers."""
    s = "1   2   3\n4    5"
    grid = string_to_grid_by_row_and_spaces(s)
    assert grid == [["1", "2", "3"], ["4", "5"]]


def test_string_to_grid_by_row_and_spaces_empty():
    """Test with empty string."""
    assert string_to_grid_by_row_and_spaces("") == []
    assert string_to_grid_by_row_and_spaces("\n\n") == []


def test_get_column_values():
    """Test extracting column values from data rows."""
    data_rows = [["5", "10", "15"], ["3", "20", "25"], ["7", "30"]]
    assert get_column_values(data_rows, 0) == [5, 3, 7]
    assert get_column_values(data_rows, 1) == [10, 20, 30]
    assert get_column_values(data_rows, 2) == [15, 25]  # Jagged array


def test_get_column_values_empty():
    """Test with empty data rows."""
    assert get_column_values([], 0) == []


def test_get_column_values_invalid_numbers():
    """Test that invalid numbers are skipped."""
    data_rows = [["5", "abc", "15"], ["3", "20"]]
    assert get_column_values(data_rows, 0) == [5, 3]
    assert get_column_values(data_rows, 1) == [20]  # "abc" is skipped


def test_apply_operation_add():
    """Test addition operation."""
    assert apply_operation("+", [1, 2, 3]) == 6
    assert apply_operation("+", [10, 20, 30]) == 60
    assert apply_operation("+", [5]) == 5


def test_apply_operation_multiply():
    """Test multiplication operation."""
    assert apply_operation("*", [2, 3, 4]) == 24
    assert apply_operation("*", [5, 2]) == 10
    assert apply_operation("*", [7]) == 7


def test_apply_operation_unknown():
    """Test unknown operation returns None."""
    assert apply_operation("?", [1, 2, 3]) is None
    assert apply_operation("-", [1, 2, 3]) is None


def test_apply_operation_empty():
    """Test with empty values returns None."""
    assert apply_operation("+", []) is None
    assert apply_operation("*", []) is None


def test_solve():
    """Test the solve function with sample input."""
    # ruff: noqa
    input_str = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    result = solve(input_str)
    assert result == 4277556

    result_part_2 = solve_part_2(input_str)
    assert result_part_2 == 3263827
