"""
You are the CEO of a large company and are trying to keep track of employee performance.
You notice that a few of your employees are not performing as well as you would like,
and you would like to tell them to improve their performance.

Unfortunately as the CEO, you are very busy and cannot be tasked with the job of telling each employee
to improve their performance. You decide to write a program to do this for you
(Because apparently you have time to write a program but not to talk to your employees.
I would not want to work for you :P).

Given two employees who are under-performing, you want to find the lowest common manager of the two employees.
The lowest common manager is the employee who is the lowest in the hierarchy and is the manager of both employees
(or at least, the employee reports to the manager in some capacity).

Firstly, decide how you want to model the employees and their relationships in your program in
such a way that is easy to traverse. You are encouraged to use your skills from Weeks 2-3 to model
the employees in Python :)

Hint: What is this problem asking you to do? How can we relate it to computer science concepts
we’ve learned so far (possibly from the weekly recap?)

Once you’ve decided on a model, write a method lowest_common_manager which takes in two
employees and returns the lowest common manager of the two employees. If there is no common manager, return None.
"""

from typing import Optional
from __future__ import annotations

class Employee:
    def __init__(self, name: str, subordinates: list[Employee]):
        self.name = name
        self.subordinates = subordinates

    def find_lca(self, target1: Employee, target2: Employee):
        if self is None:
            return None
        
        if self == target1 or self == target2:
            return self

        matches = []

        for subordinate in self.subordinates:
            result = subordinate.find_lca(target1, target2)
            if result:
                matches.append(result)