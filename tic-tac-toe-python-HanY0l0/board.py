import os
def get_empty_board():
    row0 = [".", ".", "."]
    row1 = [".", ".", "."]
    row2 = [".", ".", "."]
    board_empty = [row0, row1, row2]
    return board_empty
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''


def display_board(board):
    print("   1   2   3")
    print("A  " + " | ".join(board[0]))
    print("   --+---+---")
    print("B  " + " | ".join(board[1]))
    print("   --+---+---")
    print("C  " + " | ".join(board[2]))


"""
  Should print the tic tac toe board in a format similar to
       1   2   3
    A   . | . | .
       ---+---+---
    B   . | . | .
       --+---+---
    C   . | . | .
       --+---+---
  """


def is_board_full(board):
    #counter = 0
    for sublist in board:
        if "." in sublist:
            return False
        #for position in sublist:
            #if position != ".":
                #counter = counter
            #else:
                #counter = counter + 1
    return True

    #if counter == 0:
        #return True
    #else:
        #return False


def get_winning_player(board):
    for i in range(len(board[0])):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != ".":
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != ".":
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != ".":
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[2][0] != ".":
        return board[0][2]



    """"
    # Sprawdzanie po rzędach
    if board[0].count("X") == 3 or board[1].count("X") == 3 or board[2].count("X") == 3:
        return "X"
    elif board[0].count("O") == 3 or board[1].count("O") == 3 or board[2].count("O") == 3:
        return "O"
    # Sprawdzanie po kolumnach
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "X"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "O"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "O"
    # Sprawdzanie po przekątnych
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"

    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    else:
        return None
    """

board = [
    ['X', "X", "O"],
    ['O', "X", "X"],
    ['O', "O", "X"]
]
print(get_winning_player(board))


"""
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
"""


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)
    board_5 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    get_winning_player(board_5)

    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    
    display_board(board)
    
    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1)) 

    board_2 = [
      [".", "O", "O"],
      [".", "O", "X"],
      [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2)) 

    board_3 = [
      ["O", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3)) 

    board_4 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
      ["X", "O", "O"],
      ["X", "O", "."],
      ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))