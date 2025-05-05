# Tic-Tac-Toe game

# Initialize the board
board = [" " for _ in range(9)]  # Board will have 9 spaces

# Function to print the board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

# Function to check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Main game loop
def play_game():
    current_player = "X"
    turns = 0

    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        
        if board[move] != " ":
            print("That spot is already taken. Try again.")
            continue
        
        board[move] = current_player
        turns += 1
        
        # Check if the current player has won
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (a draw)
        if turns == 9:
            print_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
