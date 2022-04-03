"""Utility class for numerical operations."""

from __future__ import annotations

# from typing import Union

__author__ = "730466987"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Declares a new Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """Converts a Simpy object to a str object."""
        return f"Simpy: ({self.values})"

    def fill(self, filling: float, fill_number: int) -> None:
        """Fills a Simpy object's list with a set number of repetitions of a set value."""
        i: float = 0.0
        self.values: list = []

        while i < fill_number:
            self.values.append(filling)
            i += 1.0

# In O.H.: how do you get "step" to be the equal amount of distance between each item in the input list, even if it increases by 0.25? (like it does with "fractional")

    # def arange(self, start: float, stop: float, step: float = 1.0):
    #     """Returns the values within a set input, increasing by "step" value each time."""
    #     assert step != 0.0

    #     self.values: list = [start]
    #     i: float = 1.0

    #     step = (stop/start)

    #     while i < stop:
    #         self.values. append(start + step)
    #         step += 1.0
    #         i += 1

# NOTE: once you fix "arange," this function should return 45 instead of 55!

    def sum(self) -> float:
        """Sums all of the items in each index of the input Simpy."""
        summed: float = 0.0
        i: int = 0

        while i < len(self.values):
            summed += self.values[i]
            i += 1

        return summed

    # def __add__(lhs: Union[Simpy, float], rhs: Union[Simpy, float]) -> Simpy:

    # def __pow__(lhs: Union[Simpy, float], rhs: Union[Simpy, float]) -> Simpy:

    # def __eq__ (mask: list[bool], object_one: Union[Simpy, float]) -> list[bool]:

    # def __gt__()

    # def __getitem__()