class Student:
    """
    Attributes:
        name: str
        courses: list[str]
        code: int
    """
    name: str
    courses: list[str]
    code: int

    def __init__(self, name: str, courses: list[str], code: int) -> None:
        self.name = name
        self.courses = courses
        self.code = code
    
    def add(self, a: int, b: int) -> int:
        raise NotImplementedError

class MathStudent(Student):
    """Math student."""
    def __init__(self, name: str, courses: list[str], code: int, extra_courses: list[str]) -> None:
        super().__init__(name, courses, code)  # Correct usage of super() to call the parent class's __init__
        self.extra_courses = extra_courses
    
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == "__main__":
    bobby = MathStudent("bob", ["csc148"], 1480, ["mat102"])
    print(bobby.add(2, 4))
    print(bobby.name)
