from days.day5 import (
    count_numbers_in_intervals,
    merge_intervals,
    solve,
    solve2,
    split_by_double_newline,
)


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


def test_merge_intervals():
    """Test merging overlapping intervals."""
    intervals = [(1, 5), (3, 7), (10, 12)]
    merged = merge_intervals(intervals)
    assert merged == [(1, 7), (10, 12)]


def test_merge_intervals_adjacent():
    """Test merging adjacent intervals."""
    intervals = [(1, 5), (6, 10), (12, 15)]
    merged = merge_intervals(intervals)
    assert merged == [(1, 10), (12, 15)]


def test_merge_intervals_no_overlap():
    """Test intervals with no overlap."""
    intervals = [(1, 5), (10, 12), (20, 25)]
    merged = merge_intervals(intervals)
    assert merged == [(1, 5), (10, 12), (20, 25)]


def test_merge_intervals_contained():
    """Test when one interval is contained in another."""
    intervals = [(1, 10), (3, 5), (15, 20)]
    merged = merge_intervals(intervals)
    assert merged == [(1, 10), (15, 20)]


def test_count_numbers_in_intervals():
    """Test counting numbers in intervals."""
    intervals = [(1, 5), (10, 12)]
    count = count_numbers_in_intervals(intervals)
    assert count == 8  # 5 numbers (1-5) + 3 numbers (10-12)


def test_solve2():
    """Test solve2 with overlapping ranges."""
    input = """3-5
10-14
16-20
12-18"""
    # Ranges: 3-5, 10-14, 16-20, 12-18
    # Merged: 3-5, 10-20 (10-14 and 12-18 merge to 10-18, then 10-18 and 16-20 merge to 10-20)
    # Count: (5-3+1) + (20-10+1) = 3 + 11 = 14
    result = solve2(input)
    assert result == 14
