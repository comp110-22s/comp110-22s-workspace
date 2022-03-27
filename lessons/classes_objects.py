"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate price of a Pizza."""
        total: float = 0.0
        # TODO -- compute price
        if self.size == "large":
            total += 10.0
        else:
            total += 8

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"A Pizza Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Another Pizza Price: ${another_pizza.price(1.05)}")