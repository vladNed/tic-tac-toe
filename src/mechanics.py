from typing import Optional
from numpy import diagonal, rot90

from .board import Board, Markers

class Mechanics:

    def __init__(self, board: Board):
        self.board = board
        self.result = None

    def check_move(self, x: int, y: int) -> bool:
        """
        Checks if a player can set a marker tag there
        """
        return self.board[x][y] == Markers.EMPTY

    def _check_vertical_win(self) -> Optional[Markers]:
        for i in range(3):
            column = set(self.board.state[:, i])
            if (Markers.EMPTY not in column) and len(column) == 1:
                return self.board[0][i]

    def _check_horizontal_win(self) -> Optional[Markers]:
        for i in range(3):
            if len(set(self.board[i])) == 1 and Markers.EMPTY not in set(self.board[i]):
                return self.board[i][0]

    def _check_diagonal_win(self) -> Optional[Markers]:
        first_diagonal = set(diagonal(self.board.state))
        if len(first_diagonal) == 1 and Markers.EMPTY not in first_diagonal:
            return self.board[0][0]
        second_diagonal = set(diagonal(rot90(self.board.state)))
        if len(second_diagonal) == 1 and Markers.EMPTY not in second_diagonal:
            return self.board[0][2]

    def _check_board_full(self) -> Optional[Markers]:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == Markers.EMPTY:
                    return None
        return Markers.EMPTY

    def check_end(self) -> Optional[Markers]:
        """
        Check the game state to see if the game
        has ended
        """
        vertical = self._check_vertical_win()
        if vertical:
            return vertical
        horizontal = self._check_horizontal_win()
        if horizontal:
            return horizontal
        diagonal = self._check_diagonal_win()
        if diagonal:
            return diagonal
        board_full = self._check_board_full()
        if board_full:
            return board_full
