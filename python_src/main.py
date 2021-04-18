from typing import Callable, Literal, Optional, TypedDict

# Typing function parameters (keep return type implicit)
def greet(name: str):
    return f"Hello {name}"


greet_alt_2: Callable[[str], str] = lambda name: f"Hello {name}"

# Typing function return parameters
def judge_my_age(age: int) -> str:
    if age < 5:
        return "So cuuute!"

    if age < 18:
        return "Wow, you have grown since last year!"

    return "Welcome to adulthood!"


# Optional function parameter
def optional_foo(bar: Optional[str]):
    return bar or "No input"


# Classes
class Human:
    def __init__(self):
        self.nr_of_legs = 2


class Person:
    _id_counter = 0

    def __init__(self, name: str, age: Optional[int]):
        self._id = Person.get_id()
        self.name = name
        self.age = age or 0

    @staticmethod
    def get_id():
        Person._id_counter = Person._id_counter + 1
        return Person._id_counter

    @property
    def age_and_name(self):
        return f"{self.name} [{self.age}]" if self.age else self.name

    def rename(self, new_name: str):
        self.name = new_name


# Typed Dict
class Movie(TypedDict, total=False):
    title: str
    release_year: int
    rating: Literal[1, 2, 3, 4, 5]
    comments: list[str]
    sequel: Optional[str]


m_1: Movie = {
    "title": "Star Wars: A New Hope",
    "release_year": 1977,
    "rating": 5,
    "comments": [],
}
