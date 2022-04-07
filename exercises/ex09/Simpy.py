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

# In O.H.: figure out how to properly mutate "filling" so that it repeats "fill_number" times!

    def fill(self, filling: float, fill_number: int) -> None:
        """Fills a Simpy object's list with a set number of repetitions of a set value."""
        return filling ** fill_number


# Also inn O.H.: how do you get "step" to be the equal amount of distance between each item in the input list, even if it increases by a fraction?

    def arange(self, start: float, stop: float, step: Union[None, float]????????):
        """Returns the values within a set input, increasing by "step" value each time."""
        step = (stop / start)
        assert step != 0.0
        
        result: list = [start]
        i: float = 1.0

        while i < stop:
            self.values. append(start + step)
            step += 1.0
            i += 1
        return result

# NOTE: once you fix "arange," this function should return 45 instead of 55!

    def sum(self) -> float:
        """Sums all of the items in each index of the input Simpy."""
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

    def __getitem__(self, rhs: int) -> float:
        """Overload that returns the subscription notation of the unput float."""
        result: float = 0.0

        for i in self:
            result += self.values[rhs]
        return result