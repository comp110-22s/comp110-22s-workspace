"""This is a review of #5 from QU03 (function writing)."""

from pkg_resources import EGG_DIST


class Basket:
    eggs: list[str]

    def __init__(self, eggs: list[str]):
        self.eggs = eggs

    def