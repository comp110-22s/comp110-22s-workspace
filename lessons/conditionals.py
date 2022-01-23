"""An example of conditional {if-else} statments."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day")
else:  
    print("Sorry, you guessed incorrectly :( ")
    answer: str = str((input("Do you want to play again. Yes or No?")))
    if answer == "Yes":
        print("I'm thinking of a number between 1-5, what is it?")
        guess: int = int(input("What is your guess? "))
            
        if guess == SECRET:
            print("You guessed correctly!!!")
            print("Have a wonderful day")
        else: 
            print("Have a wonderful day!")

print("Game over.")