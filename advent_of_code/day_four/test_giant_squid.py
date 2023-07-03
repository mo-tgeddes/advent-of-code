import numpy as np
import pytest
from .giant_squid import mark_number, bingo, calculate_total, play

numbers = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

board1 = np.array(
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    np.int32,
)
expected_case1 = np.array(
    [
        [22, 13, 17, 11, -1],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ],
    np.int32,
)
board2 = np.array(
    [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6],
    ],
    np.int32,
)
board3 = np.array(
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
    np.int32,
)

expected_case2 = np.copy(board1)
winning_board_row = np.array(
    [
        [-1,-1,-1,-1,-1],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7],
    ],
    np.int32,
)

winning_board_column = np.array(
    [
        [14, 21, -1, 24, 4],
        [10, 16, -1, 9, 19],
        [18, 8, -1, 26, 20],
        [22, 11, -1, 6, 5],
        [2, 0, -1, 3, 7],
    ],
    np.int32,
)

@pytest.mark.parametrize("board, expected", [(board1, False),(winning_board_row, True),(winning_board_column, True)])
def test_bingo(board, expected):
    output = bingo(board)
    assert output == expected

@pytest.mark.parametrize("board, number, expected", [(board1, 0, expected_case1),(board1, 25, expected_case2)])
def test_mark_number(board, number, expected):
    output = mark_number(board, number)
    np.testing.assert_array_equal(output, expected)

@pytest.mark.parametrize("number, board, expected", [(2, winning_board_row, 490),(4, winning_board_column, 980)])
def test_calculate_total(number, board, expected):
    output = calculate_total(number, board)
    assert output == expected

@pytest.mark.parametrize("boardlist, numberlist, expected", [([board1,board2,board3], numbers, [24, winning_board_row])])
def test_play(boardlist, numberlist, expected):
    output = play(boardlist, numberlist, True)
    assert output == expected

@pytest.mark.parametrize("boardlist, numberlist, expected", [([board1,board2,board3], numbers, 4512)])
def test_all(boardlist, numberlist, expected):
    output = calculate_total(play(boardlist, numberlist, True)[0],play(boardlist, numberlist, True)[1])
    assert output == expected


