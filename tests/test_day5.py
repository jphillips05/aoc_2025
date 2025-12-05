from days.day5 import solve, split_by_double_newline


def test_split_by_double_newline():
    """Test splitting a string by double newline."""
    s = "part1\n\npart2"
    first, second = split_by_double_newline(s)
    assert first == "part1"
    assert second == "part2"


def test_split_by_double_newline_empty_first():
    """Test splitting when first part is empty."""
    s = "\n\npart2"
    first, second = split_by_double_newline(s)
    assert first == ""
    assert second == "part2"


def test_split_by_double_newline_empty_second():
    """Test splitting when second part is empty."""
    s = "part1\n\n"
    first, second = split_by_double_newline(s)
    assert first == "part1"
    assert second == ""


def test_split_by_double_newline_both_empty():
    """Test splitting when both parts are empty."""
    s = "\n\n"
    first, second = split_by_double_newline(s)
    assert first == ""
    assert second == ""


def test_solve():
    input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    assert solve(input) == 3
