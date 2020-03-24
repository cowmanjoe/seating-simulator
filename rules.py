from classroom import Classroom
from util import Position


class Rule:

    def calculate_cost(self, person_position: Position, seat_position: Position, classroom: Classroom) -> float:
        pass


class FrontOfClassRule(Rule):
    weight: float

    def __init__(self, weight: float):
        assert weight >= 0

        self.weight = weight

    def calculate_cost(self, person_position: Position, seat_position: Position, classroom: Classroom) -> float:
        return seat_position.y * self.weight

