#!/usr/bin/python3

"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c],
[r, c], [r, c]]
where `r` and `c` represent the row and column, respectively,
where a queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for rw in range(len(board)):
        for cl in range(len(board)):
            if board[rw][cl] == "Q":
                solution.append([rw, cl])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for cl in range(col + 1, len(board)):
        board[row][cl] = "x"
    # X out all backwards spots
    for cl in range(col - 1, -1, -1):
        board[row][cl] = "x"
    # X out all spots below
    for rw in range(row + 1, len(board)):
        board[rw][col] = "x"
    # X out all spots above
    for rw in range(row - 1, -1, -1):
        board[rw][col] = "x"
    # X out all spots diagonally down to the right
    cl = col + 1
    for rw in range(row + 1, len(board)):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1
    # X out all spots diagonally up to the left
    cl = col - 1
    for rw in range(row - 1, -1, -1):
        if cl < 0:
            break
        board[rw][cl]
        cl -= 1
    # X out all spots diagonally up to the right
    cl = col + 1
    for r in range(row - 1, -1, -1):
        if cl >= len(board):
            break
        board[rw][cl] = "x"
        cl += 1
    # X out all spots diagonally down to the left
    cl = col - 1
    for rw in range(row + 1, len(board)):
        if cl < 0:
            break
        board[rw][cl] = "x"
        cl -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    This function finds all possible solutions to the
    N-queens problem using backtracking.

    Args:
        board (list): The current working chessboard represented
                     as a list of lists.
        row (int): The current row being considered for queen placement.
        queens_placed (int): The number of queens already placed on the board.
        solutions (list): A list of lists containing solutions.

    Returns:
        list: A list of lists representing the solutions,
        where each inner list contains the
        positions of queens as [row, column].
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for cl in range(len(board)):
        if board[row][cl] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][cl] = "Q"
            xout(tmp_board, row, cl)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for soln in solutions:
        print(soln)
