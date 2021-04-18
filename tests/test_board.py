from src.board import Board, Markers, TagError, PositionError
import pytest


@pytest.fixture
def board() -> Board:
    return Board()


def test_mark_success(board: Board):
    board.mark(Markers.PLAYER_1, 0, 0)
    assert board[0][0] == Markers.PLAYER_1


def test_mark_give_string(board: Board):
    with pytest.raises(TagError):
        board.mark('X', 0, 0)


def test_mark_invalid_position(board: Board):
    with pytest.raises(PositionError):
        board.mark('X', 4, 5)


def test_get_item(board: Board):
    value = board[0][0]
    assert value == Markers.EMPTY
