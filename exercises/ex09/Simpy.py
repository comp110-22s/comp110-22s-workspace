"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730472535"


class Simpy:
    """Like only the best type of class besides numpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Construct an initial list."""
        self.values = values

    def __str__(self) -> str:
        """Changes the list to str values."""
        return f"Simpy({str(self.values)})"

    def fill(self, new_value: float, n: int) -> None:
        """Fills the simpy with a new value."""
        i: int = 0
        self.values = []
        while i < n:
            self.values.append(new_value)
            i += 1
        return

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values regarding the range or something."""
        assert step != 0.0
        self.values = []
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Applies the `sum` command to a Simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the `+` command so two Simpy objects may be added."""
        return_simpy = Simpy([])      
        if isinstance(rhs, float):
            for value in self.values:
                return_simpy.values.append(value + rhs)
            return(return_simpy)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                return_simpy.values.append(value + rhs.values[i])
                i += 1
            return return_simpy

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the `**` command so two Simpy objects may be powers of eachother."""
        return_simpy = Simpy([])      
        if isinstance(rhs, float):
            for value in self.values:
                return_simpy.values.append(value ** rhs)
            return return_simpy
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                return_simpy.values.append(value ** rhs.values[i])
                i += 1
            return return_simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Similar to the mask function, compares values of a Simpy object."""
        return_list: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                return_list.append(value == rhs)
            return return_list
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                return_list.append(value == rhs.values[i])
                i += 1
            return return_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Similar to the mask function, compares values of a Simpy object greater than or less than."""
        return_list: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                return_list.append(value > rhs)
            return return_list
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                return_list.append(value > rhs.values[i])
                i += 1
            return return_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allowes you to pull values at a certain index or values that are true under a certain parameter."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            return_simpy = Simpy([])
            assert len(rhs) == len(self.values)
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    return_simpy.values.append(self.values[i])
                i += 1
            return return_simpy