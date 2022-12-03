"""Advent of Code 2022"""
DAY = 1


def solve_part1(inputs: list[str]) -> int:
    pass


def solve_part2(inputs: list[str]) -> int:
    pass


def solve(desc: str, filename: str):
    with open(filename, 'r') as file:
        inputs = file.readlines()
    print(f'{desc}, part 1:', solve_part1(inputs))
    print(f'{desc}, part 2:', solve_part2(inputs))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
