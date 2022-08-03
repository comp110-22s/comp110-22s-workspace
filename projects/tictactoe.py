"""Tic-tac-toe!!"""

CHARS: list[str] = ["   ", " X ", " O "]  # index 0: whitespace | index 1: X | index 2: O
BOARD = [
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]]
]  # CHARS[0] is empty, board starts completely empty


def main() -> None:
    """Entrypoint of program."""
    tic_tac_toe()


def tic_tac_toe() -> None:
    """Handling all the details of the game."""
    num_turns: int = 1  # count num_turns to know whose turn it is
    # hint: player X should move on odd turns and player O should move on even turns
    player_name: str = ""
    i: int = -1  # i and j will eventually be BOARD indices, but let's keep them at -1 for now
    j: int = -1
    display_TTT()  # display the board before we start the game
    while True:
        # Step 1: player_name and num_turns
        if num_turns % 2 != 0:
            player_name = "X"
        else:
            player_name = "O"
        # Step 2: input and indices
        player_input = input("Enter a row (0, 1, or 2) and column (0, 1, or 2), no space, for player " + player_name + ": ")
        i: int = int(player_input[0])
        j: int = int(player_input[1]) 

        # OPTIONAL: invalid input
        if (BOARD[i][j] != CHARS[0]):  # if this space is not empty
            print("This space is already occupied!")
            continue

        # Step 3: update the board
        if player_name == "X":
            BOARD[i][j] = CHARS[1]
        else:
            BOARD[i][j] = CHARS[2]
        display_TTT()

        # Step 4: use check_win()

        if check_win(i, j) is True:
            print("Player " + player_name + " won.")
            break
        num_turns += 1

        # Step 5: draw condition
        if num_turns > 9:
            print("Draw")
            break


def check_win(i: int, j: int) -> bool:
    """Check the row, column, and diagonal (if applicable) of the space with indices (i, j) of BOARD. Note that we do not need to check all of BOARD, just the row, column, and diagonal of the last space."""
    # Step 6: check row
    if BOARD[0][j] == BOARD[1][j] and BOARD[1][j] == BOARD[2][j]:
        return True

    # Step 7: check column
    elif BOARD[i][0] == BOARD[i][1] and BOARD[i][1] == BOARD[i][2]:
        return True
    # Step 8: check diagonals
    elif ((BOARD[0][0] == BOARD[1][1] and BOARD[1][1] == BOARD[2][2]) or (BOARD[0][2] == BOARD[1][1] and BOARD[1][1] == BOARD[2][0])):
        return True
    return False


def display_TTT() -> None:
    """Display the board."""
    # Step 9: display the board
    i: int = 0
    while (i < 4):
        print("-------------") 
        if (i < 3):
            print("|" + BOARD[i][0] + "|" + BOARD[i][1] + "|" + BOARD[i][2] + "|") 
        i += 1
        # use this number of dashes - this should be printed 4 times total
    # and the string "|" should be around each character, like so: "| X | O |  |""


if __name__ == "__main__":
    main()