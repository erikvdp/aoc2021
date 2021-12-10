from dataclasses import dataclass
from collections import defaultdict
from typing import Optional
import numpy as np

BOARD_SIZE = 5


class Board:
    def __init__(self) -> None:
        self.grid = np.empty((BOARD_SIZE, BOARD_SIZE), dtype=Position)

    def __str__(self) -> str:
        return self.grid.__str__()


@dataclass
class Position:
    number: int
    checked = bool(False)

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return f"{self.number}|1" if self.checked else f"{self.number}|0"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            return self.number == __o.number
        return False


def parse_input(raw_lines: list):
    numbers = [int(number) for number in raw_lines[0].split(",")]
    boards = []
    number_to_boards = defaultdict(list)
    i = 2
    while i < len(raw_lines):
        j = 0
        board = Board()
        while j < BOARD_SIZE:
            positions = [int(x.strip()) for x in raw_lines[i].split()]
            for k, pos in enumerate(positions):
                board.grid[j, k] = Position(number=pos)
                number_to_boards[pos].append(board)
            i += 1
            j += 1
            print(i, j)
        boards.append(board)
        i += 1
    return numbers, number_to_boards, boards


def _calculate_score(board: Board, number) -> int:
    return sum([x.number for x in board.grid.flatten() if x.checked is False]) * number


def play_bingo(numbers, number_to_boards, boards) -> Optional[int]:
    for number in numbers:
        for board in number_to_boards[number]:
            row, col = (
                np.where(board.grid == Position(number))[0][0],
                np.where(board.grid == Position(number))[1][0],
            )
            board.grid[row, col].checked = True
            # check if row/column is complete
            if np.all([x.checked for x in board.grid[row, :]]) or np.all(
                [x.checked for x in board.grid[:, col]]
            ):
                print(f"Bingo!")
                return _calculate_score(board, number)


def play_bingo_2(numbers, number_to_boards, boards) -> Optional[int]:
    num_boards = len(boards)
    for number in numbers:
        for board in number_to_boards[number]:
            if board in boards:
                row, col = (
                    np.where(board.grid == Position(number))[0][0],
                    np.where(board.grid == Position(number))[1][0],
                )
                board.grid[row, col].checked = True
                # check if row/column is complete
                if np.all([x.checked for x in board.grid[row, :]]) or np.all(
                    [x.checked for x in board.grid[:, col]]
                ):
                    boards.remove(board)
                    num_boards -= 1
                    if num_boards == 0:
                        return _calculate_score(board, number)
