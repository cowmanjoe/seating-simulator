from typing import List, Optional

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

        if seat_position:
            classroom.sit_at(seat_position)

    def _choose_seat(self, classroom: Classroom) -> Optional[Position]:
        costs = self._calculate_costs(classroom)
        flattened_costs = costs.flatten()
        cost_indices_sorted = np.argsort(flattened_costs)
        for index in cost_indices_sorted:
            unraveled = np.unravel_index(index, costs.shape)
            position = Position(unraveled[1], unraveled[0])
            if classroom.get_seat(position) == 0:
                return position

        return None

    def _calculate_costs(self, classroom: Classroom) -> np.ndarray:
        costs = np.zeros((classroom.length, classroom.width))
        for y in range(classroom.length):
            for x in range(classroom.width):
                for rule in self.rules:
                    costs[y, x] += rule.calculate_cost(self.position, Position(x, y), classroom)

        return costs


