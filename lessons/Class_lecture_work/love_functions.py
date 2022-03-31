"""Some examples of functions from lecture on 2/3/22."""


def love(result: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return (f"I love you, {result}!")


print(love("name"))

# To interact with the funtion in the REPL...
# open a Python session in the Terminal and import the function.

# Result:
# >>> from lessons.love_functions import love
# I love you, name!

# Here, the name in line 9 gets lined up with the definition parameter.
# Remember, if you make changes after testing 1 version of the code in the REPL, you will need to quit and restart the REPL session.

# Next part:


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    
    love_note: str = ""
    i: int = 0

    while i < n:
        love_note = love(to) + "\n"
        i = i + 1
    return love_note


# Note: the relative reassignment operator is "+=," and it means the same thing as i = i + 1.
# Also, remember that the parameters and argument must line up for the function to work, so remember to just put the ARGUMENT in
# parenthesis to get them to line up; don't add it in on its own.

# "\n" means that there will be a line break; remember the notes from (_last week, LS??_)

# So, this function will return the value of the "love" function, which should look like this in the REPL
# >>> from lessons.love_functions import love
# I love you, name!
# >>> spread_love("Mom", 3)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'spread_love' is not defined
# >>> from lessons.love_functions import spread_love 
# >>> spread_love("Mom", 3)
# 'I love you, Mom!\n'