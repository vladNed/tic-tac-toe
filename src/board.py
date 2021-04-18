from numpy import ndarray, full
from enum import Enum


class PositionError(Exception):
    pass


class TagError(Exception):
    pass


class Markers(str, Enum):
    """
    Board markers
    """
    PLAYER_1 = "X"
    PLAYER_2 = "0"
    EMPTY = "_"


class Board:
    """
    Tic Tac Toe board
    """

    def __init__(self):
        self.state = full((3, 3), Markers.EMPTY.value)

    def __getitem__(self, x: int) -> ndarray:
        return self.state[x]

    def display(self) -> None:
        """
        Displays the current state of the board
        """
        for row in range(3):
            print('| ', end="")
            for col in range(3):
                print(f"{self.state[row][col]} |", end=" ")
            print("\n")

    def mark(self, tag: Markers, x: int, y: int) -> None:
        """
        Places a player token upon the board
        """
        if (not (0 <= x <= 2)) or (not (0 <= y <= 2)):
            raise PositionError

        self.state[x][y] = tag.value
