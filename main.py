from classroom import Classroom
from person import Person
from rules import Rule, FrontOfClassRule, FarFromStrangersRule
from util import Position

if __name__ == '__main__':
    classroom = Classroom(20, 10)

    for i in range(20):
        person = Person(Position(10, 5), [FrontOfClassRule(0), FarFromStrangersRule(1, neighbourhood=3)])
        person.sit_down(classroom)

    print(classroom._layout)
