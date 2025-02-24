from typing import Any

class WeirdList(list):
    """ Class which subclasses Python's list. """
    def __str__(self) -> str:
        """ Return a string containing the size of the list.
        >>> f = WeirdList([1, 2, 3])
        >>> str(f)
        '3'
        """
        # TODO: Fill in the blank to make this method work correctly for any WeirdList!
        return str(len(self))
    
    def last(self) -> Any:
        """ Return the last element in the list.
        Precondition: the list has at least 1 element.
        >>> f = WeirdList([1, 4, 25])
        >>> f.last()
        25
        """
        # TODO: Fill in the blank to make this method work correctly for any WeirdList!
        return self[-1]

if __name__ == "__main__":
    weird = WeirdList([1,3,2,4,5,6])
    print(weird)