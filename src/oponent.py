import yaml
import sys
from typing import Tuple

from .board import Markers
from .mechanics import Mechanics

class Opponent:
    """
    AI Tic Tac Toe opponent algorithm
    """

    EVALUATOR = {
        Markers.PLAYER_1: (-1, 0, 0),
        Markers.PLAYER_2: (1, 0, 0),
        Markers.EMPTY: (0, 0, 0)
    }
    CONFIG_PATH = './tic-tac-toe/config.yaml'

    def __init__(self, mechanics: Mechanics, ab_pruning: bool = False):
        self._mechanics = mechanics
        self.ab_pruning = ab_pruning
        self.config = self.__load_config()['opponent']

    def __load_config(self):
        try:
            with open(self.CONFIG_PATH) as fhandler:
                return yaml.safe_load(fhandler)
        except (yaml.YAMLError, FileNotFoundError):
            print("Could not load game. Configuration not found.")
            sys.exit()

    def max(self, alpha: int = None, beta: int = None) -> Tuple[int, int, int]:
        maxv = self.config['max']['v']
        x = self.config['max']['x']
        y = self.config['max']['y']
        check = self._mechanics.check_end()
        if check is not None:
            return self.EVALUATOR[check]
        for i in range(3):
            for j in range(3):
                if self._mechanics.board[i][j] == Markers.EMPTY:
                    self._mechanics.board.mark(Markers.PLAYER_2, i, j)
                    (m, _, _) = self.min(alpha, beta)
                    if m > maxv:
                        maxv = m
                        x = i
                        y = j
                    self._mechanics.board.mark(Markers.EMPTY, i, j)
                    if self.ab_pruning:
                        if maxv >= beta:
                            return maxv, x, y
                        if maxv > alpha:
                            alpha = maxv
        return (maxv, x, y)

    def min(self, alpha: int = None, beta: int = None) -> Tuple[int, int, int]:
        minv = self.config['min']['v']
        x = self.config['min']['x']
        y = self.config['min']['y']
        check = self._mechanics.check_end()
        if check is not None:
            return self.EVALUATOR[check]
        for i in range(3):
            for j in range(3):
                if self._mechanics.board[i][j] == Markers.EMPTY:
                    self._mechanics.board.mark(Markers.PLAYER_1, i, j)
                    (m, _, _) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        x = i
                        y = j
                    self._mechanics.board.mark(Markers.EMPTY, i, j)
                    if self.ab_pruning:
                        if minv <= alpha:
                            return minv, x, y
                        if minv < beta:
                            beta = minv
        return minv, x, y