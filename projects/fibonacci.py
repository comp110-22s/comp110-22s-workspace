"""Prints a fibonacci series of n terms."""


length = input("How long would you like your series to be? ")

length = int(length)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

 
# check if the number of terms is valid
if length <= 0:
    print("The length must be greater than 0")
else:
    print("Fibonacci series:")
for i in range(length):
    print(fibonacci(i))