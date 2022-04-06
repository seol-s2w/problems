from functools import total_ordering
from math import gcd


@total_ordering
class fraction:
    def __init__(self, numerator, denominator=None) -> None:
        if isinstance(numerator, str):
            numerator, denominator = map(int, numerator.split("/"))

        self._numerator = numerator
        self._denominator = denominator
        self._sign: int = -1 if bool(numerator >= 0) ^ bool(denominator >= 0) else 1
        self.__reduce()

    def __reduce(self) -> "fraction":
        gcd_ = gcd(self._numerator, self._denominator)
        self._numerator //= gcd_
        self._denominator //= gcd_
        return self

    def __repr__(self) -> str:
        return f"fraction({self._sign*self._numerator}, {self._denominator})"

    def __str__(self) -> str:
        return f"{self._sign*self._numerator}/{self._denominator}"

    def __abs__(self) -> float:
        return abs(self._sign * self._numerator / self._denominator)

    def __add__(self, o) -> "fraction":
        pass

    def __sub__(self, other) -> "fraction":
        pass

    def __mul__(self, other) -> "fraction":
        pass

    def __eq__(self, __o: object) -> bool:
        pass

    def __lt__(self, __o: object) -> bool:
        pass


a = fraction("123/456")
print(a)
