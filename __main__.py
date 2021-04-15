"""
Tic Tac Toe Game

Created with Adversial Search algorithm
as an AI opponent

Author: Vlad Nedelcu
Date: 15.04.2021
Version: 1.0
"""
from .src.game_engine import Game

if __name__ == "__main__":
    game = Game()
    game.start()
