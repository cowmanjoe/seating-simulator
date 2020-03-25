import math

from classroom import Classroom
from util import Position


class Rule:

    def calculate_cost(self, seat_position: Position, classroom: Classroom) -> float:
        pass


class FrontOfClassRule(Rule):
    _weight: float

    def __init__(self, weight: float):
        assert weight >= 0

        self._weight = weight

    def calculate_cost(self, seat_position: Position, classroom: Classroom) -> float:
        return seat_position.y * self._weight


class FarFromStrangersRule(Rule):
    _weight: float
    _neighbourhood: int

    def __init__(self, weight: float, neighbourhood: int = 1):
        self._weight = weight
        self._neighbourhood = neighbourhood

    def calculate_cost(self, seat_position: Position, classroom: Classroom) -> float:
        cost = 0

        for i in range(-self._neighbourhood, self._neighbourhood + 1):
            for j in range(-self._neighbourhood, self._neighbourhood + 1):
                if i == 0 and j == 0:
                    continue

                x = seat_position.x + i
                y = seat_position.y + j
                if x < 0 or x >= classroom.width or y < 0 or y >= classroom.length:
                    continue

                if classroom.get_seat(Position(x, y)):
                    cost += self._weight / math.sqrt(i ** 2 + j ** 2)

        return cost


class CloseToEntranceRule(Rule):
    _weight: float

    def __init__(self, weight: float):
        self._weight = weight

    def calculate_cost(self, seat_position: Position, classroom: Classroom) -> float:
        return self._weight * math.sqrt((classroom.entrance_position.x - seat_position.x) ** 2 +
                         (classroom.entrance_position.y - seat_position.y) ** 2)
