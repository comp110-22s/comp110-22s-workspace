
def main() -> None:
    inventory: dict[str, int] = {"apples": 5, "chips": 1, "bananas": 4}
    grocerylist: dict[str, int] = {"apples": 6, "chips": 1, "bananas": 3}
    groceries(inventory, grocerylist)


def groceries(a: dict[str, int], b: dict[str, int]) -> list[str]:
    grocery_list: list[str] = []
    for item in a:
        if item in b and b[item] <= a[item]:
            grocery_list.append(item)
    return grocery_list

main()