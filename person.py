from typing import List

import numpy as np

from classroom import Classroom
from rules import Rule
from util import Position


class Person:
    position: Position
    rules: List[Rule]

    def __init__(self, position: Position, rules: List[Rule]):
        self.position = position
        self.rules = rules

    def sit_down(self, classroom: Classroom):
        seat_position = self._choose_seat(classroom)
        classroom.sit_at(seat_position)

    def _choose_seat(self, classroom: Classroom) -> Position:
        costs = self._calculate_costs(classroom)
        min_cost_index = costs.argmin()
        cost_position = np.unravel_index(min_cost_index, costs.shape)

        return Position(cost_position[0], cost_position[1])

    def _calculate_costs(self, classroom: Classroom) -> np.ndarray:
        costs = np.zeros((classroom.length, classroom.width))
        for y in range(classroom.length):
            for x in range(classroom.width):
                for rule in self.rules:
                    costs[y, x] += rule.calculate_cost(self.position, Position(x, y), classroom)

        return costs


