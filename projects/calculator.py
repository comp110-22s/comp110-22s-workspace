"""Calculator program!"""


def addition():

    print("Addition")
    n = float(input("Enter a number: "))
    ans: float = 0
    while n != "quit":
        ans += n
    return [ans]


def subtraction():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t: float = 0
    ans: float = 0
    while n != 0:
        ans -= n
        t += 1
    n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t: float = 0
    ans: float = 1
    while n != 0:
        ans = ans * n
        t += 1
    n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]


def division():
    print("Division")
    n = float(input("Enter the number: "))
    t: float = 0
    ans: float = 1
    while n != 0:
        ans = ans / n
        t += 1
    n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]

# main...


while True:

    l1: list = []

    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            l1 = addition()
            print("Ans = ", l1[0], " total inputs ", l1[1])
        elif c == 's':
            l1 = subtraction()
            print("Ans = ", l1[0], " total inputs ", l1[1])
        elif c == 'm':
            l1 = multiplication()
            print("Ans = ", l1[0], " total inputs ", l1[1])
        elif c == 'v':
            l1 = division()
            print("Ans = ", l1[0], " total inputs ", l1[1])
        else:
            print("Invalid input.")
            break