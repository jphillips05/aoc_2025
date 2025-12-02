import pytest

from days.day2 import (
    has_repeated_pattern,
    invalid_ids,
    is_valid_id,
    parse_range,
    process_range,
    range_list,
    solve,
)


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


def test_has_repeated_pattern():
    # IDs with repeated patterns are invalid
    assert has_repeated_pattern("123123123") is True  # "123" repeated 3 times
    assert has_repeated_pattern("1111") is True  # "1" repeated 4 times
    assert has_repeated_pattern("1212") is True  # "12" repeated 2 times
    assert has_repeated_pattern("12341234") is True  # "1234" repeated 2 times
    assert has_repeated_pattern("111") is True  # "1" repeated 3 times

    # IDs without repeated patterns
    assert has_repeated_pattern("1234") is False
    assert has_repeated_pattern("12345") is False
    assert has_repeated_pattern("123456") is False
    assert has_repeated_pattern("1234567") is False


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

    # IDs with repeated patterns - is_valid_id only checks halves
    # (repeated pattern check is done separately in process_range)
    assert is_valid_id(123123123) is True  # "123" repeated, but halves differ ("123123" != "123")
    assert is_valid_id(1212) is False  # "12" repeated AND halves same ("12" == "12")
    assert is_valid_id(1111) is False  # "1" repeated AND halves same ("11" == "11")
    assert is_valid_id(12341234) is False  # "1234" repeated AND halves same ("1234" == "1234")

    # IDs where halves differ are VALID (return True)
    assert is_valid_id(12) is True  # "1" != "2"
    assert is_valid_id(1234) is True  # "12" != "34"
    assert is_valid_id(1213) is True  # "12" != "13"

    # Odd-length IDs are VALID (return True)
    assert is_valid_id(123) is True
    assert is_valid_id(12345) is True
    assert is_valid_id(111) is True  # odd length, valid (repeated pattern checked separately)


def test_range_list():
    assert range_list(1, 5) == [1, 2, 3, 4, 5]
    assert range_list(5, 1) == [5, 4, 3, 2, 1]
    assert range_list(3, 3) == [3]
    assert range_list(11, 22) == list(range(11, 23))


def test_process_range():
    # process_range now just returns the range of numbers
    assert process_range("11-22") == list(range(11, 23))
    assert process_range("95-115") == list(range(95, 116))
    assert process_range("998-1012") == list(range(998, 1013))
    assert process_range("1-5") == [1, 2, 3, 4, 5]
    assert process_range("1212-1214") == [1212, 1213, 1214]


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
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]
    assert solve(input_lines, check_repeating=False) == 1227775554

    assert solve(input_lines, check_repeating=True) == 4174379265


def test_solve_check_repeating_individual_ranges():
    """Test solve with check_repeating=True for each individual range."""
    # 11-22 still has two invalid IDs, 11 and 22
    assert invalid_ids(process_range("11-22"), check_repeating=True) == [11, 22]
    assert solve(["11-22"], check_repeating=True) == 33

    # 95-115 now has two invalid IDs, 99 and 111
    assert invalid_ids(process_range("95-115"), check_repeating=True) == [99, 111]
    assert solve(["95-115"], check_repeating=True) == 210

    # 998-1012 now has two invalid IDs, 999 and 1010
    assert invalid_ids(process_range("998-1012"), check_repeating=True) == [999, 1010]
    assert solve(["998-1012"], check_repeating=True) == 2009

    # 1188511880-1188511890 still has one invalid ID, 1188511885
    assert invalid_ids(process_range("1188511880-1188511890"), check_repeating=True) == [1188511885]
    assert solve(["1188511880-1188511890"], check_repeating=True) == 1188511885

    # 222220-222224 still has one invalid ID, 222222
    assert invalid_ids(process_range("222220-222224"), check_repeating=True) == [222222]
    assert solve(["222220-222224"], check_repeating=True) == 222222

    # 1698522-1698528 still contains no invalid IDs
    assert invalid_ids(process_range("1698522-1698528"), check_repeating=True) == []
    assert solve(["1698522-1698528"], check_repeating=True) == 0

    # 446443-446449 still has one invalid ID, 446446
    assert invalid_ids(process_range("446443-446449"), check_repeating=True) == [446446]
    assert solve(["446443-446449"], check_repeating=True) == 446446

    # 38593856-38593862 still has one invalid ID, 38593859
    assert invalid_ids(process_range("38593856-38593862"), check_repeating=True) == [38593859]
    assert solve(["38593856-38593862"], check_repeating=True) == 38593859

    # 565653-565659 now has one invalid ID, 565656
    assert invalid_ids(process_range("565653-565659"), check_repeating=True) == [565656]
    assert solve(["565653-565659"], check_repeating=True) == 565656

    # 824824821-824824827 now has one invalid ID, 824824824
    assert invalid_ids(process_range("824824821-824824827"), check_repeating=True) == [824824824]
    assert solve(["824824821-824824827"], check_repeating=True) == 824824824

    # 2121212118-2121212124 now has one invalid ID, 2121212121
    assert invalid_ids(process_range("2121212118-2121212124"), check_repeating=True) == [2121212121]
    assert solve(["2121212118-2121212124"], check_repeating=True) == 2121212121
