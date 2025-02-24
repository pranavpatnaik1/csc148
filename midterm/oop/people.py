from __future__ import annotations

class Person:
    """Class of describing a person.
    
    Attributes:
        - name: str
        - mood: str
        - age: int
        - fav_food: str
    """
    name: str
    mood: str
    age: int
    fav_food: str

    def __init__(self, name: str, mood: str, age: int, fav_food: str) -> None:
        self.name = name
        self.mood = mood
        self.age = age
        self.fav_food = fav_food
    
    def give_age(self) -> int:
        return str(self.age) + " years old"

    def greet(self, other: Person) -> str:
        return "Hello, " + other.name + ",  it's nice to meet you! I'm " + self.name + "."
    
    def change_name(self, new_name: str) -> None:
        self.name = new_name

    def change_mood(self, new_mood: str) -> None:
        self.mood = new_mood
    
    def eat(self, food: str) -> None:
        if food == self.fav_food:
            self.change_mood("ecstatic")
