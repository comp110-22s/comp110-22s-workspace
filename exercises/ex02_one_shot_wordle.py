"""One Shot Wordle"""

__author__ = 730474722

secret: str = "python"
intro: str = input("What is your 6-letter guess? ")
if len(secret) != len(intro):
    intro = input("That was not 6-letters! Try again: ")
    intro = input("That was not 6-letters! Try again: ")
    intro = input("That was not 6-letters! Try again: ")
    intro = input("That was not 6-letters! Try again: ")
    if len(intro) != len(secret):
        print("Not quite. Play again soon!")
        exit()
    
while intro != secret:
    print("Not quite. Play again soon!")
    exit()
if intro == secret:
    print("Woo! You got it!")




