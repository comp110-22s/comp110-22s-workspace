"""This is a review of #5 from QU03 (function writing)."""


class Basket:
    eggs: list[str]

    def __init__(self, eggs: list[str]):
        """Constructs a new Basket object."""
        if eggs is None:
            self.eggs = []
        else:
            self.eggs = eggs

    def is_full(self) -> bool:
        full: bool = False

        if len(self.eggs) < 5:
            full = False
        else:
            full = True
        return full

    def same_color(self, new_basket: Basket) -> bool:
        i: int = 0
        same_egg: bool = False

        while i < len(self.eggs):
            ii: int = 0

            while ii < len(new_basket):
                if self.eggs[i] == new_basket[ii]:
                    same_egg = True
                ii += 1
            i += 1
        return same_egg


a: Basket = Basket(["blue", "red", "green"])
print(a.eggs)

b: Basket = Basket(["yellow", "green", "red", "pink", "white"])
print(b.eggs)

print(a.is_full())
print(b.is_full())

print(a.same_color(b))