from typing import Type


class Vector:
    """A class to represent a Euclidean vector with magnitude and direction"""

    def __init__(self, *numbers: float) -> None:
        #print(numbers)
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} must be float or int not {type(number)}")

        if len(numbers) <= 0:
            raise ValueError("Vectors can't be empty")

        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self) -> tuple:
        return self._numbers

        
    # (2,3) + (1,1,1) not okay
    # (2,3) + (1,1) = (3,4)
    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vectors(other):
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)
    
    def __len__(self) -> int:
        """Returns number of components in a Vector not the Euclidan lenght"""
        return len(self.numbers)

    def validate_vectors(self, other: "Vector") -> bool:
        """ Validate that two vectors have same dimensions"""
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both must be vector and same lenght")
        return len(self) == len(other)

    def __repr__(self) -> str:
        return f"Vector{self.numbers}"

    def __str__(self) -> str:
        return f"{self.numbers}"

    def __getitem__(self, item: int) -> float:
        return self.numbers[item]