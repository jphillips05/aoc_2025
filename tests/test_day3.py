from days.day3 import highest_number, solve, string_to_ints


def test_string_to_ints():
    assert string_to_ints("123") == [1, 2, 3]
    assert string_to_ints("5192") == [5, 1, 9, 2]
    assert string_to_ints("0") == [0]
    assert string_to_ints("9876543210") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert string_to_ints("") == []


def test_string_to_ints_single_digit():
    assert string_to_ints("5") == [5]
    assert string_to_ints("9") == [9]
    assert string_to_ints("0") == [0]


def test_string_to_ints_repeated_digits():
    assert string_to_ints("111") == [1, 1, 1]
    assert string_to_ints("999") == [9, 9, 9]
    assert string_to_ints("000") == [0, 0, 0]


def test_highest_number():
    assert highest_number([1, 2, 3]) == 23
    assert highest_number([5, 1, 9, 2]) == 92
    assert highest_number([0, 1, 2]) == 12


def test_highest_number_single_digit():
    assert highest_number([5]) == 0
    assert highest_number([9]) == 0
    assert highest_number([0]) == 0


def test_highest_number_two_digits():
    assert highest_number([1, 2]) == 12
    assert highest_number([9, 1]) == 91
    assert highest_number([5, 7]) == 57
    assert highest_number([0, 1]) == 1


def test_highest_number_three_digits():
    assert highest_number([1, 2, 3]) == 23
    assert highest_number([9, 1, 5]) == 95
    assert highest_number([2, 1, 9]) == 29
    assert highest_number([5, 5, 5]) == 55


def test_highest_number_four_digits():
    assert highest_number([5, 1, 9, 2]) == 92
    assert highest_number([9, 1, 5, 2]) == 95
    assert highest_number([1, 9, 8, 7]) == 98
    assert highest_number([2, 3, 1, 4]) == 34


def test_highest_number_with_zero():
    assert highest_number([0, 1, 2]) == 12
    assert highest_number([1, 0, 2]) == 12
    assert highest_number([1, 2, 0]) == 20
    assert highest_number([0, 0, 1]) == 1


def test_highest_number_descending_order():
    assert highest_number([9, 8, 7]) == 98
    assert highest_number([5, 4, 3, 2]) == 54


def test_highest_number_ascending_order():
    assert highest_number([1, 2, 3, 4]) == 34
    assert highest_number([2, 3, 4, 5]) == 45


def test_highest_number_empty_list():
    assert highest_number([]) == 0


def test_solve_sample_input():
    """Test solve with the provided sample input."""
    input_lines = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    assert solve(input_lines) == 357
    assert solve(input_lines, n=12) == 3121910778619
