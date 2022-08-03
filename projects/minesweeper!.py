"""An attempt at Minesweeper."""

import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()  # plant the bomb
        self.assign_values_to_board()
        # initialize a set to keep track of which locations uncovered
        # using (row,col) tuples
        self.dug = set()  # 0, 0 appears as {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs using list of lists

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            # assigning each bomb a random location

            if board[row][col] == '*':
                # this means we had already planted a bomb
                continue

            board[row][col] = '*'  # plant a bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
    
    def get_num_neighboring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number of bombs
        
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - (row + 1) + 1)):
            for c in range(max(0, (col - 1), min(self.dim_size - 1, col + 1) + 1)):
                # checking below and above of row, right and left of column
                if r == row and c == col:
                    # original location
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at location, True is successful, False if bomb
        # dig at location with no neighboring bombs? recursively dig neighbors

        self.dug.add((row, col))  # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - (row + 1) + 1)):
            for c in range(max(0, (col - 1), min(self.dim_size - 1, col + 1) + 1)):
                if (r, c) in self.dug:
                    continue  # no dig where already dug
                self.dig(r, c)

        return True  # should never hit a bomb

    def __str__(self):
        # print the board as a string

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
 

def play(dim_size=10, num_bombs=10):
    # create the board
    board = Board(dim_size, num_bombs)

    # show the user the board and ask where they want to dig
    # if location is a bomb, game over
    # if location if not a bomb, dig recursively until each square is at least next to a bomb
    # repeat until no more places to dig
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # make input readable no matter what
        user_input = re.split(',(\\s*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            # dug a bomb, end game
            break

    # either dug a bomb or have no more spaces to dig
    if safe:
        print("You win!")
    else:
        print("You lose.")
        # reveal board
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == 'main':
    play()