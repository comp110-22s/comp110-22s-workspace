"""One Shot Wordle!"""

__author__ = "730474722"

"""Providing the correct user input"""
secret: str = "ears"
intro: str = input(f"What is your {len(secret)}-letter guess? ")
proceed: bool = False
while (proceed is False):
    if len(secret) != len(intro):
        intro = input(f"That was not {len(secret)}-letters! Try again: ")
    else:
        proceed = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

current_index: int = 0
ci = current_index
scan = 0
g = GREEN_BOX
w = WHITE_BOX
y = YELLOW_BOX
emojis: str = ""
tracker: bool = False
tracker is False

"""Matching indexes when guess is incorrect"""
if intro != secret:
    while ci < len(secret):
        if intro[ci] == secret[ci]:
            emojis += g
        else:
            while (not tracker) and (scan < len(secret)):
                if intro[ci] == secret[scan]:
                    tracker = True
                else:
                    scan += 1
            if tracker is True:
                emojis += y
            else: 
                emojis += w
        scan = 0
        tracker = False
        ci += 1 
    print(emojis)
    print("Not quite. Play again soon!")


"""Win"""
if intro == secret:
    while ci < len(secret):
        emojis += g
        ci += 1
    print(emojis)
    print("Woo! You got it!")
