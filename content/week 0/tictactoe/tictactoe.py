"""
Tic Tac Toe Player
"""

import math
import copy
from typing import no_type_check_decorator

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    moves = 0
    for row in board:
        for cell in row:
            if cell != EMPTY:
                moves = moves + 1
    
    if moves % 2 == 0:
        return X
    else: 
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pactions = set()
    nrow, ncell = 0, 0

    for row in board:
        for cell in row:
            if cell == EMPTY:
                pactions.add((nrow, ncell))
            ncell = ncell + 1
        
        nrow = nrow + 1 
        ncell = 0 

    return pactions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """ 
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in row for row in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            return maxValue(board)[1]
        else:
            return minValue(board)[1]

def maxValue(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        tmpv = minValue(result(board, action))[0]
        if tmpv > v:
            v = tmpv  
            move = action
            if v == 1:
                return v, move
    
    return v, move

def minValue(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        tmpv = maxValue(result(board, action))[0]
        if tmpv < v:
            v = tmpv
            move = action
            if v == -1:
                return v, move

    return v, move
