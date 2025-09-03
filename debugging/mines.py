#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clear the terminal screen depending on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        """Initialize the Minesweeper game with board size and mine count."""
        self.width = width
        self.height = height
        # Randomly place mines using 1D indices (0..width*height-1)
        self.mines = set(random.sample(range(width * height), mines))
        # Track revealed cells: initially all False (hidden)
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """Print the game board. 
        If reveal=True, show all mines and numbers (used on game over)."""
        clear_screen()
        # Print column headers
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')  # Row index
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    idx = y * self.width + x
                    if idx in self.mines:
                        ch = '*'
                    else:
                        c = self.count_mines_nearby(x, y)
                        ch = str(c) if c > 0 else ' '
                else:
                    ch = '.'
                print(ch, end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """Count the number of mines around the given cell (x, y)."""
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:  # Skip the current cell itself
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Reveal a cell. Return False if it's a mine (game over), True otherwise."""
        # Out of bounds or already revealed → do nothing
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        if self.revealed[y][x]:
            return True

        # If the cell is a mine → game over
        if (y * self.width + x) in self.mines:
            return False

        # Mark cell as revealed
        self.revealed[y][x] = True

        # If no neighboring mines, automatically reveal neighbors (flood fill)
        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    self.reveal(x + dx, y + dy)
        return True

    def won(self):
        """Check if the player has won: 
        all non-mine cells are revealed."""
        total = self.width * self.height
        opened = sum(1 for row in self.revealed for v in row if v)
        return opened == total - len(self.mines)

    def play(self):
        """Main game loop."""
        while True:
            self.print_board()
            # Check win condition before asking for new input
            if self.won():
                print("Congratulations! You've won the game.")
                break
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()