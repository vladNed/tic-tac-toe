import os
import sys
import yaml

from time import perf_counter
from typing import Optional

from .board import Markers, Board
from .mechanics import Mechanics
from .oponent import Opponent


class Game:

    EVALUATOR = {
        Markers.PLAYER_1: 'X wins !!',
        Markers.PLAYER_2: 'O wins !!',
        Markers.EMPTY: 'Its a tie !!'
    }
    EXIT_COMMAND = "exit"
    CONFIG_PATH = './tic-tac-toe/config.yaml'

    def __init__(self):
        self.config = self.__load_config().get('engine', {})
        self.board = Board()
        self.ab_pruning = self.config['ab_pruning']
        self.mechanics = Mechanics(self.board)
        self.opponent = Opponent(self.mechanics, self.ab_pruning)
        self.turn = Markers.PLAYER_1
        if self.ab_pruning:
            self.beta = 2
            self.alpha = -2
        else:
            self.beta = None
            self.alpha = None

    def __load_config(self):
        try:
            with open(self.CONFIG_PATH) as fhandler:
                return yaml.safe_load(fhandler)
        except (yaml.YAMLError, FileNotFoundError):
            print("Could not load game. Configuration not found.")
            sys.exit()

    def __input_player(self, coordinate: str) -> Optional[int]:
        """
        Gets input from player and validates entry
        """
        coordinate = input(self.config['debug']['user_input'].format(c=coordinate))
        if coordinate.lower() == self.EXIT_COMMAND:
            print(self.config['text']['exit_msg'])
            sys.exit()

        try:
            result = int(coordinate)
        except ValueError:
            print(self.config['text']['invalid_msg'])
            return
        else:

            return result

    def __player_turn(self) -> None:
        """
        Performs player turn
        """
        while True:
            x = self.__input_player("x")
            if x is None:
                continue

            y = self.__input_player("y")
            if y is None:
                continue

            if self.mechanics.check_move(x, y):
                self.board.mark(Markers.PLAYER_1, x, y)
                self.turn = Markers.PLAYER_2
                break
            else:
                print(self.config['text']['place_msg'])

    def __opponent_turn(self) -> None:
        """
        Performs opponent turn
        """
        if self.opponent.ab_pruning:
            start = perf_counter()
            (_, x, y) = self.opponent.max(self.alpha, self.beta)
            end = perf_counter()
        else:
            start = perf_counter()
            (_, x, y) = self.opponent.max()
            end = perf_counter()
        print(self.config['debug']['solution'].format(seconds=end - start))
        print(self.config['debug']['opponent_move'].format(x=x, y=y))
        self.board.mark(Markers.PLAYER_2, x, y)
        self.turn = Markers.PLAYER_1
        self.board.display()

    def start(self):
        """
        Game start and entrypoint
        """
        TURN_MAPPER = {
            Markers.PLAYER_1: self.__player_turn,
            Markers.PLAYER_2: self.__opponent_turn
        }
        os.system('cls')
        self.board.display()
        while True:
            result = self.mechanics.check_end()
            if result is not None:
                print(self.EVALUATOR[result])
                break
            TURN_MAPPER[self.turn]()
