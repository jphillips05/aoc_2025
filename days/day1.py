from data import get_input


def parse_line(line: str) -> list[int]:
    direction = 1 if line[0] == "R" else -1
    steps = int(line[1:])
    return direction, steps


def move(line: str, position: int) -> tuple[int, int]:
    direction, steps = parse_line(line)
    zeroes = 0
    for _ in range(steps):
        position += direction
        position = position % 100
        if position == 0:
            zeroes += 1

    return position, zeroes


def solve(input: list[str], count_all: bool = False) -> int:
    position = 50
    zeroes = 0
    all_zeroes = 0
    for line in input:
        position, count = move(line, position)
        all_zeroes += count
        if position == 0:
            zeroes += 1

    return all_zeroes if count_all else zeroes


def main():
    input = get_input("data/2025/1.txt")
    zeroes = solve(input)
    print(zeroes)


if __name__ == "__main__":
    main()
