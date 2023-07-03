import numpy
import numpy as np
from io import StringIO
MARKED_NUMBER = -1

def bingo(board):
    bingo_result = False
    for axis in range(2):
        if MARKED_NUMBER*5 in np.sum(board, axis=axis):
            bingo_result = True
    return bingo_result

def mark_number(board, number):
    #print(board)
    #print(number)
    board1 = np.where(board == number, MARKED_NUMBER, board)
    return board1

def calculate_total(number,board):
    board = np.where(board == MARKED_NUMBER, 0, board)
    return np.sum(board)*number

def play(boards, numlist, winning): #for some reason returns the number after it should if plain number is returned
    """
    Return the winning board and last called number.

    Parameters
    ----------
    boards : list of numpy arrays.
    numlist : list of integers.

    Returns
    -------
    integer , numpy array
        last called number
        winning board


    """
    index_boards = {index : board for index, board in enumerate(boards)}
    index_loserboards = index_boards.copy()
    last_winning_board = None
    last_winning_number = None
    for numindex, number in enumerate(numlist):
        for index, board in index_boards.items():
            if index in index_loserboards:
                board = mark_number(board, number)
                index_boards[index] = board
                if bingo(board):
                    last_winning_board = board
                    last_winning_number = number
                    _ = index_loserboards.pop(index)
                    if winning:
                        return number, board
    return last_winning_number, last_winning_board

def read_file(filepath):
    with open(filepath) as file_handle:
        contents = file_handle.read()
        # list comprehension - reads everything in square brackets before
        # complaining
    items = contents.split("\n\n")
    numlist = [int(number.strip()) for number in items[0].split(",")]
    boards = [(board.strip()) for board in items[1:]]
    board_arrays = [np.genfromtxt(StringIO(board), dtype=np.int32) for board in boards]
    return numlist, board_arrays


if __name__ == "__main__":
    numlist, boardlist = read_file("input.txt")
    print(numlist)
    print(type(numlist))
    number, board = play(boardlist, numlist, True)
    print(f"part 1 {calculate_total(number, board)}")
    number, board = play(boardlist, numlist, False)
    print(f"part 2 {calculate_total(number, board)}")