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
        self.values = []

        while i < fill_number:
            self.values.append(filling)
            i += 1.0

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Returns the values within a set input."""
        

    # def sum() -> float:

    # def __add__(lhs: Union[Simpy, float], rhs: Union[Simpy, float]) -> Simpy:

    # def __pow__(lhs: Union[Simpy, float], rhs: Union[Simpy, float]) -> Simpy:

    # def __eq__ (mask: list[bool], object_one: Union[Simpy, float]) -> list[bool]:

    # def __gt__()

    # def __getitem__()