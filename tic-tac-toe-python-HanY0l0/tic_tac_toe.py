from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option
import os
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = "X"
    while is_game_running:
        os.system('cls')
        display_board(board)
        if game_mode == 1:
            x, y = get_human_coordinates(board, current_player)
            board[x][y] = current_player
            current_player = "O" if current_player == "X" else "X"
            winning_player = get_winning_player(board)
            its_a_tie = is_board_full(board)
        if game_mode == 2:
            winning_player = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if winning_player:
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            if its_a_tie:
                print("It's a tie!")
                break

if __name__ == "__main__":
    main()