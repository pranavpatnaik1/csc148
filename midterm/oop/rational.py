"""
Rational numbers
A rational number consists of a
numerator and denominator; the denominator cannot be 0.
Rational numbers are written like 7/8. Typical operations include
determining whether the rational is positive,
multiplying two rationals, comparing two rationals,
and converting a rational to a string.
"""

from __future__ import annotations

class Rational:
    """Class for rational numbers.
    
    Attributes:
        - numerator: int
        - denominator: int
        - is_positive: bool
        
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
        
        if self.numerator < 0 or self.denominator < 0:
            self.is_positive = False
        else:
            self.is_positive = True

        if self.denominator == 0:
            raise ArithmeticError("Denominator cannot be 0.")
    
    def add(self, other: Rational) -> None:
        """
        Add fractions.

        >>> a = Rational(2,3)
        >>> b = Rational(3,4)
        >>> a.add(b)
        >>> print(a)
        17/12
        """


        if self.denominator != other.denominator:
            temp = self.denominator
            temp2 = other.denominator
            self.denominator = self.denominator * other.denominator
            other.denominator = self.denominator

            self.numerator *= temp2
            other.numerator *= temp

            self.numerator += other.numerator
        else:
            self.numerator += other.numerator
        
        if self.numerator < 0 or self.denominator < 0:
            self.is_positive = False
        else:
            self.is_positive = True
        
    def multiply(self, other: Rational) -> None:
        """Multiply two rationals.
        
        >>> a = Rational(2,3)
        >>> b = Rational(3,4)
        >>> a.multiply(b)
        >>> print(a)
        6/12
        """
        self.numerator *= other.numerator
        self.denominator *= other.denominator
    
    def greater_than(self, other: Rational) -> bool:
        """Comparing greater than.
        
        >>> a = Rational(2,3)
        >>> b = Rational(3,4)
        >>> a.greater_than(b)
        False
        """
        return (self.numerator / self.denominator) > (other.numerator / other.denominator)
    


    def __str__(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


            
    
