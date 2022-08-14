"""Code generator and decoder!"""


def codify(message: str) -> str:
    code: str = ""
    for c in message:
        if c == "a":
            code += "9"
        elif c == "b":
            code += "8"
        elif c == "c":
            code += "7"
        elif c == "d":
            code += "6"
        elif c == "e":
            code += "5"
        elif c == "f":
            code += "4"
        elif c == "g":
            code += "3"
        elif c == "h":
            code += "2"
        elif c == "i":
            code += "1"
        elif c == "j":
            code += "0"
        elif c == "k":
            code += "q"
        elif c == "l":
            code += "w"
        elif c == "m":
            code += "e"
        elif c == "n":
            code += "r"
        elif c == "o":
            code += "t"
        elif c == "p":
            code += "y"
        elif c == "q":
            code += "u"
        elif c == "r":
            code += "i"
        elif c == "s":
            code += "o"
        elif c == "t":
            code += "p"
        elif c == "u":
            code += "a"
        elif c == "v":
            code += "s"
        elif c == "w":
            code += "d"
        elif c == "x":
            code += "f"
        elif c == "y":
            code += "g"
        elif c == "z":
            code += "h"
        elif c == "1":
            code += "j"
        elif c == "2":
            code += "k"
        elif c == "3":
            code += "l"
        elif c == "4":
            code += "z"
        elif c == "5":
            code += "x"
        elif c == "6":
            code += "c"
        elif c == "7":
            code += "v"
        elif c == "8":
            code += "b"
        elif c == "9":
            code += "n"
        elif c == "0":
            code += "m"
        elif c == ".":
            code += "?"
        elif c == "!":
            code += "."
        elif c == "?":
            code += "!"
        else:
            code += c
    return code


def decode(message: str) -> str:
    code: str = ""
    for c in message:
        if c == "9":
            code += "a"
        elif c == "8":
            code += "b"
        elif c == "7":
            code += "c"
        elif c == "6":
            code += "d"
        elif c == "5":
            code += "e"
        elif c == "4":
            code += "f"
        elif c == "3":
            code += "g"
        elif c == "2":
            code += "h"
        elif c == "1":
            code += "i"
        elif c == "0":
            code += "j"
        elif c == "q":
            code += "k"
        elif c == "w":
            code += "l"
        elif c == "e":
            code += "m"
        elif c == "r":
            code += "n"
        elif c == "t":
            code += "o"
        elif c == "y":
            code += "p"
        elif c == "u":
            code += "q"
        elif c == "i":
            code += "r"
        elif c == "o":
            code += "s"
        elif c == "p":
            code += "t"
        elif c == "a":
            code += "u"
        elif c == "s":
            code += "v"
        elif c == "d":
            code += "w"
        elif c == "f":
            code += "x"
        elif c == "g":
            code += "y"
        elif c == "h":
            code += "z"
        elif c == "j":
            code += "1"
        elif c == "k":
            code += "2"
        elif c == "l":
            code += "3"
        elif c == "z":
            code += "4"
        elif c == "x":
            code += "5"
        elif c == "c":
            code += "6"
        elif c == "v":
            code += "7"
        elif c == "b":
            code += "8"
        elif c == "n":
            code += "9"
        elif c == "m":
            code += "0"
        elif c == "?":
            code += "."
        elif c == ".":
            code += "!"
        elif c == "!":
            code += "?"
        else:
            code += c
    return code


start: str = input("Would you like to code a message or decode a message? ")
if start.lower() == "code":
    message: str = input("What message would you like to code? ")
    message = message.lower()
    code: str = codify(message)
    print(code)
    quit()
elif start.lower() == "decode":
    message: str = input("What message would you like to decode? ")
    message = message.lower()
    code: str = decode(message)
    print(code)
    quit()
else:
    print("Invalid input")
    quit()

print(code)