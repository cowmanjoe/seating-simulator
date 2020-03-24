from classroom import Classroom
from person import Person
from rules import Rule, FrontOfClassRule
from util import Position

if __name__ == '__main__':
    classroom = Classroom(20, 10)
    person = Person(Position(10, 5), [FrontOfClassRule(0.5)])

    person.sit_down(classroom)

    print(classroom._layout)
