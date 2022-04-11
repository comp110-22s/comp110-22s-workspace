"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730466987"


class Simpy:
    """This class manipulates input numerical data like a simpler version of the NumPy library."""
    # Don't forget to include a DocString describing new classes from now on!
    values: list[float]

    def __init__(self, new_object: list[float]):
        """Declares a new Simpy object."""
        self.values = new_object
    
    def __str__(self) -> str:
        """Converts a Simpy object to a str object."""
        return f"Simpy({self.values})"

    def fill(self, filling: float, fill_number: int) -> None:
        """Fills a Simpy object's list with a set number of repetitions of a set value."""
        i: int = 0
        self.values = []

        while i < fill_number:
            self.values.append(filling)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Returns the values within a set input, increasing by "step" value each time."""
        assert step != 0.0
        
        result: list = []
        i: float = start + step
        current: float = start

        result.append(start)
        
        while i != stop:
            current += step
            result.append(current)
            i += step
        self.values = result

        # Here, "step" doesn't change itself, but it is changed depending on the value of "start."
        # This way, it is set as +1 by default, but if it needs to be changed, then it can be.

        # Also, note that the "current" variable is necessary here because it removes some of the abstraction from where the function is in its while loop!

    def sum(self) -> float:
        """Sums all of the items in the input Simpy."""
        summed: float = 0.0
        i: int = 0

        while i < len(self.values):
            summed += self.values[i]
            i += 1

        return summed

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds Simpy and float objects together."""
        result: list[float] = []

        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs)

        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises Simpy and float objects to the values of each other."""
        result: list[float] = []

        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            
        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs)

        return Simpy(result)

        # __pow__ is supposed to look similar to __add__, because they follow the same rules for which operators to use on the input objects,
        # whether they are Simpy or float objects.

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overload that returns the matching values between an input Simpy and float."""
        matching: list[bool] = []

        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    matching.append(True)
                else:
                    matching.append(False)
            return matching

        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                if self.values[i] == rhs:
                    matching.append(True)
                else:
                    matching.append(False)
            return matching

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload that returns the values in an input value that are greater than the items at the same indices in rhs."""
        greater_than: list[bool] = []

        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    greater_than.append(True)
                else:
                    greater_than.append(False)
            return greater_than

        if isinstance(rhs, float):
            for i in range(0, len(self.values)):
                if self.values[i] > rhs:
                    greater_than.append(True)
                else:
                    greater_than.append(False)
            return greater_than

        return greater_than

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload that returns the subscription notation of the input int or list[bool]."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            list_output: list[float] = []
            
            i: int = 0

            while i < len(rhs):
                if rhs[i] is True:
                    list_output.append(self.values[i])
                    i += 1
                else:
                    i += 1
            
            return Simpy(list_output)

        # Note that this function returns a float if rhs is an int, but it returns a Simpy if rhs is a list[bool].
        # This difference is important because the operator overload masks for both types of objects, but in different ways,
        # depending on the input object's type.