"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730466987"


class Simpy:
    values: list[float]

    def __init__(self, new_object: list[float]):
        """Declares a new Simpy object."""
        self.values = new_object
    
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

    def __add__(self, lhs: Union [float, Simpy], rhs: Union[float, Simpy]) -> Simpy:
        """Adds Simpy and float objects."""
        result: Simpy = (lhs + rhs)

        if lhs == Simpy and rhs == Simpy:
            assert len(lhs) == len(rhs)
            added: Simpy = 

        elif lhs == float and rhs == Simpy:
            

        elif lhs == Simpy and rhs == float:


        else:

        if isinstance(lhs, Simpy and rhs, Simpy):
            for i in range(0, len(self.items)):
                # For the code above, know that it's basically the same as using a for-in loop to go through each item in the list.
                result.append(self.items[i] + " " + rhs.items[i])
                # The above line of code says that self and rhs are each applied to StrArray objects, and the "i"s line up their lists so that
                # self[1], for example, can only be added to rhs[1].
                # Also, there is a space added in the middle for easier reading of the print object.
        
        return StrArray(result)

        return result


    def __pow__(lhs: Union[Simpy, float], rhs: Union[Simpy, float]) -> Simpy:




    # def __eq__ (mask: list[bool], object_one: Union[Simpy, float]) -> list[bool]:

    # def __gt__()

    # def __getitem__()