"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730405989"


class Simpy:
    """Class imitating Numpy methods."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor method for Simpy."""
        self.values = values
    
    def __str__(self) -> str:
        """String representation method."""
        return f"Simpy({self.values})"

    def fill(self, number: float, repeat: int) -> None:
        """Method filling Simpy with repeated number of certain number."""
        self.values = []
        i = 0
        while i < repeat:
            self.values.append(number)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create Simpy with values building from start to end values."""
        assert step != 0.0
        i: float = start
        while i != stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Compute sum of Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add stuff."""
        addlist: list[float] = []
        if isinstance(rhs, float):
            for nums in self.values:
                addlist.append(nums + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                addlist.append(self.values[i] + rhs.values[i])
                i += 1
        return Simpy(addlist)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise stuff to a power."""
        powlist: list[float] = []
        if isinstance(rhs, float):
            for nums in self.values:
                powlist.append(nums ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                powlist.append(self.values[i] ** rhs.values[i])
                i += 1
        return Simpy(powlist)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test if equal to."""
        result: list[bool] = []
        if isinstance(rhs, float): 
            for nums in self.values:
                result.append(nums == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test if greater than."""
        result: list[bool] = []
        if isinstance(rhs, float): 
            for nums in self.values:
                result.append(nums > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get subscription operator for Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            result: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
            