"""EX02 - One Shot Wordle!"""

__author__ = "730472535"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
result: str = ""
b: int = 0
test: bool = False

while len(guess) != len(secret_word):
    guess = input(f"That in not {len(secret_word)} letters! Try again: ")
    
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        result = result + GREEN_BOX
    else:
        while not test and b < len(secret_word):  # b allowes the computer to test each letter of your guess against every letter in the secret word
            if guess[i] == secret_word[b]:
                result = result + YELLOW_BOX
                test = True  # stops the while loop if letter exists in word
                b = 0  # resets the variable b in order to test the next letter correctly
            else:
                if b == len(secret_word) - 1:  # program will only reach this step if the letter is not in the secret word
                    result = result + WHITE_BOX
                    b = 0
                    test = True  # exits the loop if the letter is not in the secret word
                else:
                    b += 1
                
    i += 1  # ensures the loop is progressing forward
    test = False  # resets the bool value of test so loop can be run for the next letter
print(result)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")