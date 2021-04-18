import pytest

from src.mechanics import Mechanics
from src.board import Board, Markers


@pytest.fixture
def mechanics() -> Mechanics:
    board = Board()
    return Mechanics(board)


def test_check_move(mechanics):
    assert mechanics.check_move(0, 0)


def test_check_move_false(mechanics):
    mechanics.board.mark(Markers.PLAYER_1, 0, 1)
    assert not mechanics.check_move(0, 1)


def test_check_vertical_win(mechanics: Mechanics):
    for i in range(3):
        mechanics.board.mark(Markers.PLAYER_1, i, 0)

    assert mechanics.check_end() == Markers.PLAYER_1


def test_check_horizontal_win(mechanics: Mechanics):
    for i in range(3):
        mechanics.board.mark(Markers.PLAYER_1, 0, i)

    assert mechanics.check_end() == Markers.PLAYER_1


def test_check_diagonal_win_1(mechanics: Mechanics):
    for i in range(3):
        mechanics.board.mark(Markers.PLAYER_1, i, i)

    assert mechanics.check_end() == Markers.PLAYER_1


def test_check_diagonal_win_2(mechanics: Mechanics):
    mechanics.board.mark(Markers.PLAYER_1, 0, 2)
    mechanics.board.mark(Markers.PLAYER_1, 1, 1)
    mechanics.board.mark(Markers.PLAYER_1, 2, 0)

    assert mechanics.check_end() == Markers.PLAYER_1


def test_not_end(mechanics: Mechanics):
    mechanics.board.mark(Markers.PLAYER_1, 0, 2)
    mechanics.board.mark(Markers.PLAYER_1, 2, 0)

    assert mechanics.check_end() is None