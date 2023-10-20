def get_human_coordinates(board, current_player):
  associate = {"A":0 , "B":1 , "C":2,
              1:0, 2:1, 3:2
              }

  while True:
    try:
      coords = input(f"Player {current_player} provide coordinates (row, column): ").upper()
      if coords == "QUIT":
        exit(code="Goodbye!")
      if len(coords) !=2:
        raise ValueError("Invalid input format. Coordinates must follow this pattern: row,column.")
      if coords[0] not in {"A", "B", "C"}:
        raise ValueError("Invalid input. Rows can only be A, B or C")
      if int(coords[1]) not in {1, 2, 3}:
        raise ValueError("Invalid input. Columns can only be 1, 2 or 3")
      x = associate[coords[0]]
      y = associate[int(coords[1])]
      if board[x][y] != ".":
        raise ValueError("Already taken, try a different one")
      return x, y
    except ValueError as e:
      print(f"{e}")
      continue




def get_random_ai_coordinates(board, current_player):
  associate = {"A":0 , "B":1 , "C":2,
              1:0, 2:1, 3:2
              }

  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 