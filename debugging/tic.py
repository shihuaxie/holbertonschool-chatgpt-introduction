#!/usr/bin/python3

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    """Check if the board is completely filled (for a draw)."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Main Tic-Tac-Toe game loop."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Winner check
        if check_winner(board):
            print("Player " + ("O" if player == "X" else "X") + " wins!")
            break

        # Draw check
        if board_full(board):
            print("It's a draw!")
            break

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid position! Please enter 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only (0, 1, or 2).")


if __name__ == "__main__":
    tic_tac_toe()