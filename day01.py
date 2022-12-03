"""Advent of Code 2022"""
from itertools import groupby

DAY = 1


def parse_inputs(inputs: list[str]) -> list[list[int]]:
    """
    Break the input lines into the integer groups defined by the empty lines.

    For example, turn:
        1
        2

        3

        4
    Into:
        [[1, 2], [3], [4]]
    """
    groups = []
    for _, vals in groupby(inputs, key=lambda x: x == "\n"):
        group = [int(val) for val in vals if val != "\n"]
        if group:
            groups.append(group)
    return groups


def solve_part1(inputs: list[str]) -> int:
    """Find the largest group in the inputs."""
    groups = parse_inputs(inputs)
    return max(sum(group) for group in groups)


def solve_part2(inputs: list[str]) -> int:
    """Find the largest 3 groups in the inputs."""
    groups = parse_inputs(inputs)
    sums = [sum(group) for group in groups]
    largest = []
    for i in range(3):
        largest.append(max(sums))
        sums.remove(max(sums))
    return sum(largest)


def solve(desc: str, filename: str):
    with open(filename, 'r') as file:
        inputs = file.readlines()
    print(f'{desc}, part 1:', solve_part1(inputs))
    print(f'{desc}, part 2:', solve_part2(inputs))


if __name__ == '__main__':
    solve(f'Day {DAY} test case', f'day{str(DAY).zfill(2)}testcase.txt')
    solve(f'Day {DAY}', f'day{str(DAY).zfill(2)}input.txt')
