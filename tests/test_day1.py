from days.day1 import move, parse_line, solve

input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_move():
    assert move("R60", 95) == (55, 1)
    assert move("R1000", 50) == (50, 10)


def test_solve():
    assert solve(input.split("\n"), True) == 6
    assert solve(input.split("\n")) == 3


def test_parse_line():
    assert parse_line("R1") == (1, 1)
    assert parse_line("L1") == (-1, 1)
    assert parse_line("R10") == (1, 10)
    assert parse_line("L10") == (-1, 10)
