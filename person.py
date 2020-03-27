import random
from typing import List, Optional

import numpy as np

from rule_configuration import RuleConfiguration
from rules import Rule
from simulation_configuration import SimulationConfiguration
from util import Position


def create_person(rule_configurations: List[RuleConfiguration]):
    return Person([config.create_rule() for config in rule_configurations])


class Person:
    # id should always be a positive integer
    id: int
    rules: List[Rule]

    def __init__(self, rules: List[Rule]):
        self.id = random.randint(1, 1E9)
        self.rules = rules

    def sit_down(self, simulation_config: SimulationConfiguration):
        seat_position = self._choose_seat(simulation_config)

        if seat_position:
            simulation_config.classroom.sit_at(seat_position, self.id)

    def _choose_seat(self, simulation_config: SimulationConfiguration) -> Optional[Position]:
        costs = self._calculate_costs(simulation_config)
        flattened_costs = costs.flatten()
        cost_indices_sorted = np.argsort(flattened_costs)
        for index in cost_indices_sorted:
            unraveled = np.unravel_index(index, costs.shape)
            position = Position(unraveled[1], unraveled[0])
            if not simulation_config.classroom.is_seat_occupied(position):
                return position

        return None

    def _calculate_costs(self, simulation_configuration: SimulationConfiguration) -> np.ndarray:
        costs = np.zeros((simulation_configuration.classroom.length, simulation_configuration.classroom.width))
        for y in range(simulation_configuration.classroom.length):
            for x in range(simulation_configuration.classroom.width):
                for rule in self.rules:
                    costs[y, x] += rule.calculate_cost(Position(x, y), simulation_configuration, self.id)

        return costs


