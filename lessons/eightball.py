"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question ")

response: int = randint(0, 3)

if response == 0:
    print("HELL YEAH!!!")
elif response == 1:
    print("yes no yes")
elif response == 2:
    print("hmmm bagels")
else:
    print("How much wood could a wood chuck chuck if a wood chuck could chuck wood?")