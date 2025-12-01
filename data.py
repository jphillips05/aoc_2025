import os
import argparse
from data_file import DataFile

HERE = os.path.dirname(os.path.abspath(__file__))


def get_input(file: str) -> list[str]:
    """Read input file and return lines as a list of strings."""
    with open(os.path.join(HERE, file), "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--year", help="The year of the puzzle")
    argparser.add_argument("--day", help="The day of the puzzle")

    args = argparser.parse_args()
    print("getting data")
    DataFile(args.year, args.day)
    print("done")
