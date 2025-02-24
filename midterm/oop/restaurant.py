"""
Restaurant recommendation

The recommendation system, in addition to actually making recommendations,
should be able to report statistics like the number of times a certain person has used the system,
the number of times it has recommended each restaurant, and the
last recommendation made for a given group of people.
"""

class Person:
    """Class for a Person.
    
    Attributes:
        - name: str
        - location: str
        - diet_restricts: list[str]
        - ratings: dict[str, int]
        - comments: dict[str, str]
    """
    name: str
    location: str
    diet_restricts: list[str]
    ratings: dict[str, int]
    comments: dict[str, str]

    def __init__(self, name: str, location: str, 
                 diet_restricts: list[str], ratings: dict[str, int],
                 comments: dict[str, str]) -> None:
        self.name = name
        self.location = location
        self.diet_restricts = diet_restricts
        self.ratings = ratings
        self.comments = comments

class Restaurant:
    """Class for restaurants.
    
    Attributes:
        - name: str
        - menu: list[str]
        - location: str
    """
    name: str
    menu: list[str]
    location: str
    
    def __init__(self, name: str, menu: list[str], location: str) -> None:
        self.name = name
        self.menu = menu
        self.location = location
    
    
