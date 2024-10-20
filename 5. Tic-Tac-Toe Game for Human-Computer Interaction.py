import random

# Display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check for a win or tie
def check_winner(board, mark):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == mark for i, j, k in win_conditions)

# Check if the board is full
def board_full(board):
    return ' ' not in board

# Player's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            board[int(move) - 1] = 'X'
            break
        print("Invalid move. Try again.")

# Computer's move
def computer_move(board):
    possible_moves = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(possible_moves)
    board[move] = 'O'

# Main game loop
def tic_tac_toe():
    board = [' ' for _ in range(9)]
    display_board(board)

    while True:
        player_move(board)
        display_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if board_full(board):
            print("It's a tie!")
            break

        print("Computer's turn...")
        computer_move(board)
        display_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if board_full(board):
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()
