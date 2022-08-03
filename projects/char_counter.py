"""Counts the character occurances in a string."""


def count_characters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

    
print(count_characters("Greensboro, North Carolina."))