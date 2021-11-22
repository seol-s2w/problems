import itertools


class Small:
    def __init__(self, decimals: list = []):
        if decimals:
            self.__decimals = decimals
        else:
            self.__decimals = [0]

        self._str = self.__create_decimal_str(self.__decimals)

    def __str__(self) -> str:
        return self._str

    def __repr__(self) -> str:
        return f"Small({self.__decimals})"

    def __hash__(self) -> int:
        return hash(self._str)

    def __abs__(self) -> float:
        return float(self._str)

    def __len__(self) -> int:
        return len(self.__decimals)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__decimals[key]

        sliced_decimals = [0] * self.__len__()
        sliced_decimals[key] = self.__decimals[key]

        return self.__create_decimal_str(sliced_decimals)

    def __create_decimal_str(self, decimals: list) -> str:
        return "".join([str(digit) for digit in itertools.chain("0.", decimals)])
