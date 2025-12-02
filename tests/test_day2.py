import pytest

from days.day2 import is_valid_id, parse_range, process_range, range_list, solve


def test_parse_range_single_digits():
    assert parse_range("1-5") == (1, 5)
    assert parse_range("0-9") == (0, 9)
    assert parse_range("9-0") == (9, 0)


def test_parse_range_multiple_digits():
    assert parse_range("10-20") == (10, 20)
    assert parse_range("100-200") == (100, 200)
    assert parse_range("1-100") == (1, 100)


def test_parse_range_negative_numbers():
    # Note: Negative numbers don't work with simple split('-') approach
    # These would require a more sophisticated parser
    # For now, testing that they raise ValueError
    with pytest.raises(ValueError):
        parse_range("-5--1")
    with pytest.raises(ValueError):
        parse_range("-10-10")
    with pytest.raises(ValueError):
        parse_range("0--5")


def test_parse_range_large_numbers():
    assert parse_range("1000-2000") == (1000, 2000)
    assert parse_range("999999-1000000") == (999999, 1000000)


def test_parse_range_invalid_format_no_dash():
    with pytest.raises(ValueError, match="Expected format 'number-number'"):
        parse_range("15")


def test_parse_range_invalid_format_multiple_dashes():
    with pytest.raises(ValueError, match="Expected format 'number-number'"):
        parse_range("1-2-3")


def test_parse_range_invalid_format_empty_string():
    with pytest.raises(ValueError, match="Expected format 'number-number'"):
        parse_range("")


def test_parse_range_invalid_format_only_dash():
    with pytest.raises(ValueError):
        parse_range("-")


def test_parse_range_invalid_format_non_numeric():
    with pytest.raises(ValueError):
        parse_range("a-b")


def test_is_valid_id():
    # IDs where halves are the same are INVALID (return False)
    assert is_valid_id(11) is False  # "1" == "1"
    assert is_valid_id(22) is False  # "2" == "2"
    assert is_valid_id(99) is False  # "9" == "9"
    assert is_valid_id(1010) is False  # "10" == "10"
    assert is_valid_id(222222) is False  # "222" == "222"
    assert is_valid_id(446446) is False  # "446" == "446"
    assert is_valid_id(1188511885) is False  # "11885" == "11885"
    assert is_valid_id(38593859) is False  # "3859" == "3859"

    # IDs where halves differ are VALID (return True)
    assert is_valid_id(12) is True  # "1" != "2"
    assert is_valid_id(1234) is True  # "12" != "34"
    assert is_valid_id(1213) is True  # "12" != "13"

    # Odd-length IDs are VALID (return True)
    assert is_valid_id(123) is True
    assert is_valid_id(12345) is True


def test_range_list():
    assert range_list(1, 5) == [1, 2, 3, 4, 5]
    assert range_list(5, 1) == [5, 4, 3, 2, 1]
    assert range_list(3, 3) == [3]
    assert range_list(11, 22) == list(range(11, 23))


def test_process_range():
    # 11-22 has two invalid IDs: 11 and 22
    assert process_range("11-22") == [11, 22]

    # 95-115 has one invalid ID: 99
    assert process_range("95-115") == [99]

    # 998-1012 has one invalid ID: 1010
    assert process_range("998-1012") == [1010]

    # 1188511880-1188511890 has one invalid ID: 1188511885
    assert process_range("1188511880-1188511890") == [1188511885]

    # 222220-222224 has one invalid ID: 222222
    assert process_range("222220-222224") == [222222]

    # 1698522-1698528 contains no invalid IDs
    assert process_range("1698522-1698528") == []

    # 446443-446449 has one invalid ID: 446446
    assert process_range("446443-446449") == [446446]

    # 38593856-38593862 has one invalid ID: 38593859
    assert process_range("38593856-38593862") == [38593859]


def test_solve():
    input_lines = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
    ]
    # Expected sum: 11 + 22 + 99 + 1010 + 1188511885 + 222222 + 446446 + 38593859
    assert solve(input_lines) == 1227775554
