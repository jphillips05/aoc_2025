from days.day4 import check_adjacent, solve, string_to_grid


def test_check_adjacent_center():
    """Test checking adjacent positions from center of grid."""
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    # Position (1,1) is 'E', adjacent positions are A,B,C,D,F,G,H,I
    # If we're looking for 'A', there's 1 occurrence, so < 2 should be True
    assert check_adjacent(grid, 1, 1, "A", 2) is True
    assert check_adjacent(grid, 1, 1, "A", 1) is False  # 1 is not < 1


def test_check_adjacent_corner():
    """Test checking adjacent positions from corner."""
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    # Position (0,0) is 'A', adjacent positions are B,D,E
    assert check_adjacent(grid, 0, 0, "B", 2) is True  # 1 occurrence < 2
    assert check_adjacent(grid, 0, 0, "B", 1) is False  # 1 occurrence is not < 1


def test_check_adjacent_edge():
    """Test checking adjacent positions from edge."""
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    # Position (0,1) is 'B', adjacent positions are A,C,D,E,F
    assert check_adjacent(grid, 0, 1, "A", 2) is True
    assert check_adjacent(grid, 0, 1, "D", 2) is True


def test_check_adjacent_no_matches():
    """Test when no adjacent positions match."""
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    # Position (1,1) is 'E', looking for 'X' which doesn't exist
    assert check_adjacent(grid, 1, 1, "X", 1) is True  # 0 < 1
    assert check_adjacent(grid, 1, 1, "X", 0) is False  # 0 is not < 0


def test_check_adjacent_multiple_matches():
    """Test when multiple adjacent positions match."""
    grid = [["A", "A", "A"], ["A", "B", "A"], ["A", "A", "A"]]
    # Position (1,1) is 'B', surrounded by 8 'A's
    assert check_adjacent(grid, 1, 1, "A", 9) is True  # 8 < 9
    assert check_adjacent(grid, 1, 1, "A", 8) is False  # 8 is not < 8
    assert check_adjacent(grid, 1, 1, "A", 7) is False  # 8 is not < 7


def test_check_adjacent_invalid_position():
    """Test with invalid position."""
    grid = [["A", "B", "C"], ["D", "E", "F"]]
    # Out of bounds
    assert check_adjacent(grid, -1, 0, "A", 1) is False
    assert check_adjacent(grid, 0, -1, "A", 1) is False
    assert check_adjacent(grid, 10, 0, "A", 1) is False
    assert check_adjacent(grid, 0, 10, "A", 1) is False


def test_check_adjacent_empty_grid():
    """Test with empty grid."""
    assert check_adjacent([], 0, 0, "A", 1) is False


def test_check_adjacent_single_cell():
    """Test with single cell grid."""
    grid = [["A"]]
    # No adjacent positions, so count is 0
    assert check_adjacent(grid, 0, 0, "A", 1) is True  # 0 < 1
    assert check_adjacent(grid, 0, 0, "A", 0) is False  # 0 is not < 0


def test_string_to_grid_newline():
    """Test converting string to grid with newline separator."""
    s = "ABC\nDEF\nGHI"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_string_to_grid_custom_separator():
    """Test converting string to grid with custom separator."""
    s = "A,B,C"
    result = string_to_grid(s, sep=",")
    assert result == [["A"], ["B"], ["C"]]


def test_string_to_grid_empty_string():
    """Test converting empty string to grid."""
    assert string_to_grid("") == []


def test_string_to_grid_single_line():
    """Test converting single line string to grid."""
    s = "ABC"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"]]


def test_string_to_grid_multiple_separators():
    """Test converting string with multiple consecutive separators."""
    s = "ABC\n\nDEF\nGHI"
    result = string_to_grid(s)
    # Empty lines should be filtered out
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_string_to_grid_space_separator():
    """Test converting string with space separator."""
    s = "A B C"
    result = string_to_grid(s, sep=" ")
    assert result == [["A"], ["B"], ["C"]]


def test_string_to_grid_with_carriage_return():
    """Test converting string with Windows line endings."""
    s = "ABC\r\nDEF\r\nGHI"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_string_to_grid_with_old_mac_line_endings():
    """Test converting string with old Mac line endings."""
    s = "ABC\rDEF\rGHI"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_string_to_grid_with_trailing_newline():
    """Test converting string with trailing newline."""
    s = "ABC\nDEF\nGHI\n"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_string_to_grid_mixed_line_endings():
    """Test converting string with mixed line endings."""
    s = "ABC\nDEF\r\nGHI\r"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]


def test_check_adjacent_jagged_array():
    """Test checking adjacent positions in a jagged array."""
    grid = [
        ["A", "B", "C"],
        ["D", "E"],  # Shorter row
        ["F", "G", "H", "I"],  # Longer row
    ]
    # Position (1,1) is 'E', adjacent positions are B,C,D,F,G
    assert check_adjacent(grid, 1, 1, "B", 2) is True  # 1 occurrence < 2
    assert check_adjacent(grid, 1, 1, "F", 2) is True  # 1 occurrence < 2


def test_check_adjacent_jagged_array_edge():
    """Test checking adjacent positions at edge of jagged array."""
    grid = [
        ["A", "B", "C"],
        ["D", "E"],  # Shorter row
        ["F", "G", "H", "I"],  # Longer row
    ]
    # Position (0,2) is 'C', adjacent positions are B,D,E,F
    assert check_adjacent(grid, 0, 2, "B", 2) is True
    assert check_adjacent(grid, 0, 2, "D", 2) is True


def test_string_to_grid_jagged_array():
    """Test converting string to jagged grid."""
    s = "ABC\nDE\nFGHI"
    result = string_to_grid(s)
    assert result == [["A", "B", "C"], ["D", "E"], ["F", "G", "H", "I"]]
    assert len(result[0]) == 3
    assert len(result[1]) == 2
    assert len(result[2]) == 4


def test_solve():
    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    assert solve(input) == 13
