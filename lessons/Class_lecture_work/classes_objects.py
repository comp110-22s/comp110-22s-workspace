"""This is an example of a class and object instaniation (making an idea into a code model). (Lecture 3/22/22)."""

# The class below (Pizza) evaluates its own price after being established by the user (me!).


class Pizza:
    """Models the idea of a Pizza in the code."""

    # Attribute Definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    # Note that the function below does not include the extra_cheese parameter on purpose; see below.

    def __init__(self, size: str, toppings: int):
        """This is a constructor for a new Pizza object."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """This function calculates the price of a pizza."""
        total: float = 0.0
        # Remember, the pizza designed above has size == large!

        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        
        # Imagine that all additional toppings cost $0.75.

        total += self.toppings * 0.75

        # Imagine that extra cheese costs $1.

        if self.extra_cheese:
            total += 1.0

        total += tax

        return total


a_pizza: Pizza = Pizza("large", 3)

print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

# tax = $1.05
# That parameter is added to the parenthesis of the method call because it changes each time, while "self" doesn't.

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")

# tax also = $1.05 here