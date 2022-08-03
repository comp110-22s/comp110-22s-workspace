"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730465187"


class Simpy:
    """Simpler, single dimension NumPy."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Simpy constructor."""
        self.values = values

    def __str__(self) -> str:
        """Turn a simpy into a string."""
        return f"Simpy({str(self.values)})"
    
    def fill(self, value: float, num: int) -> None:
        """Fill a simpy with repeating values."""
        self.values = []
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a Simpy of values increasing by an increment of your choice."""
        assert step != 0
        i: int = 0
        counter: float = start
        if stop > start:
            while counter < stop:
                self.values.append(start + (step * i))
                counter += step
                i += 1
        elif start > stop:
            while stop < counter:
                self.values.append(start + (step * i))
                counter += step
                i += 1

    def sum(self) -> float:
        """Sum a Simpy."""
        s: float = sum(self.values)
        return s

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add a Simpy with a float or another Simpy."""
        n: list[float] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                n.append(self.values[i] + rhs.values[i])
                i += 1
            return Simpy(n)
        elif isinstance(rhs, float):
            while i < len(self.values):
                n.append(self.values[i] + rhs)
                i += 1
            return Simpy(n)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise a Simpy to a float or another Simpy."""
        n: list[float] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                n.append(self.values[i] ** rhs.values[i])
                i += 1
            return Simpy(n)
        elif isinstance(rhs, float):
            while i < len(self.values):
                n.append(self.values[i] ** rhs)
                i += 1
            return Simpy(n)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if the values in two Simpies are equal."""
        n: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    n.append(True)
                else:
                    n.append(False)
                i += 1
            return n
        elif isinstance(rhs, float):
            while i < len(self.values):
                if self.values[i] == rhs:
                    n.append(True)
                else:
                    n.append(False)
                i += 1
            return n

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Check if the values in one Simpy are greater than a float or another Simpy."""
        n: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    n.append(True)
                else:
                    n.append(False)
                i += 1
            return n
        elif isinstance(rhs, float):
            while i < len(self.values):
                if self.values[i] > rhs:
                    n.append(True)
                else:
                    n.append(False)
                i += 1
            return n

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use subscription notation for a Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            n: list[float] = []
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    n.append(self.values[i])
                i += 1
            return Simpy(n)