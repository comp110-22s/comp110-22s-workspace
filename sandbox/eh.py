def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """A list which is a subset of the given list, between the specified start index and the end index -1."""
    copy_list: list[int] = list()
    i: int = 0
    while i < len(a_list):
        copy_list.append(a_list[i])
        i += 1

    if (a_list == list()):
        x = int()
        y = int()
        return a_list

    if (x >= len(a_list)) or y <= 0:
        a_list = list()
        return a_list
    if x < 0:
        x = 0
    if y >= len(a_list):
        y = (len(a_list) - 1)

    under: int = 0
    over: int = (len(copy_list) - 1)
    replacer: int = 0
    replacer_two: int = len(copy_list) - 1

    if y < over:
        while replacer_two > y:
            copy_list.pop(over)
            replacer_two -= 1
            print(copy_list)
  
    if x > under:
        while replacer < x:
            copy_list.pop(under)
            replacer += 1
    return copy_list


a_list: list[int] = [1, 2, 3]
print(sub(a_list, 1, 1))
