"""Dictionary functions."""

__author__ = "730405989"


def invert(orig: dict[str, str]) -> dict[str, str]:
    """Function that inverts dictionary given."""
    invdict: dict = {}
    # For each value in original list, code the value of that key to equal the value 
    for key in orig:
        if orig[key] in invdict:
            raise KeyError("Repeat value in dictionary. Unable to invert! ")
        else:
            invdict[orig[key]] = key
    return invdict


def favorite_color(record: dict[str, str]) -> str:
    """Counts people's favorite color and returns string of favorite color."""
    # If empty, return no favorite color
    if record == {}:
        return 'No favorite color'
    # Saves colors as list, in order to avoid some key errors
    colorlist: list[str] = list()
    for names in record:
        colorlist.append(record[names])
    coldict: dict[str, int] = {}
    # put colors from list into coldict one at a time, if had put in, if not had add 1
    for colors in colorlist:
        if colors in coldict:
            coldict[colors] += 1
        else:
            coldict[colors] = 1
    # Initialie fav to the first string, but then have it change if next color has more
    fav: str = colorlist[0]
    for colors2 in coldict:
        if coldict[colors2] > coldict[fav]:
            fav = colors2
    return fav


def count(givenlist: list[str]) -> dict[str, int]:
    """Counts string number in list."""
    if givenlist == []:
        return {}
    number: dict[str, int] = {}
    for givenkey in givenlist:
        if givenkey in number:
            number[givenkey] += 1
        else: 
            number[givenkey] = 1
    return number