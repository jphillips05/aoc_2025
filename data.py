import argparse
import os

from data_file import DataFile

HERE = os.path.dirname(os.path.abspath(__file__))


def get_input_string(file: str) -> str:
    """Read input file and return lines as a string."""
    with open(os.path.join(HERE, file)) as f:
        return f.read()


def get_input(file: str) -> list[str]:
    """Read input file and return lines as a list of strings."""
    with open(os.path.join(HERE, file)) as f:
        return [line.strip() for line in f.readlines()]


def create_day_file(day: str) -> None:
    """Create day solution file if it doesn't exist."""
    day_file = os.path.join(HERE, f"days/day{day}.py")
    if not os.path.exists(day_file):
        template = f"""from data import get_input


def solve(input_lines: list[str]) -> int:
    \"\"\"Solve the puzzle.

    Args:
        input_lines: List of input lines

    Returns:
        The solution
    \"\"\"
    return 0


def main():
    input_lines = get_input("data/2025/{day}.txt")
    result = solve(input_lines)
    print(result)


if __name__ == "__main__":
    main()
"""
        with open(day_file, "w") as f:
            f.write(template)
        print(f"Created {day_file}")


def create_test_file(day: str) -> None:
    """Create test file if it doesn't exist."""
    test_file = os.path.join(HERE, f"tests/test_day{day}.py")
    if not os.path.exists(test_file):
        template = f"""from days.day{day} import solve


def test_solve():
    \"\"\"Test the solve function.\"\"\"
    input_lines = ["test", "input"]
    result = solve(input_lines)
    assert result == 0
"""
        with open(test_file, "w") as f:
            f.write(template)
        print(f"Created {test_file}")


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--year", help="The year of the puzzle")
    argparser.add_argument("--day", help="The day of the puzzle")

    args = argparser.parse_args()
    print("getting data")
    DataFile(args.year, args.day)
    create_day_file(args.day)
    create_test_file(args.day)
    print("done")
