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

    # def __getitem__(self, rhs: int) -> float:
    #     """Overload that returns the subscription notation of the unput float."""
    #     result: float = 0.0

    #     for i in self:
    #         result += self.values[rhs]
    #     return result