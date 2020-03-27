import math

from simulation_configuration import SimulationConfiguration
from util import Position


class Rule:
    def calculate_cost(self, seat_position: Position, simulation_configuration: SimulationConfiguration, person_id: int) -> float:
        pass


class FrontOfClassRule(Rule):
    _weight: float

    def __init__(self, weight: float):
        assert weight >= 0

        self._weight = weight

    def calculate_cost(self, seat_position: Position, simulation_configuration: SimulationConfiguration, person_id: int) -> float:
        return seat_position.y * self._weight


class FarFromStrangersRule(Rule):
    _weight: float
    _neighbourhood: int

    def __init__(self, weight: float, neighbourhood: int = 1):
        self._weight = weight
        self._neighbourhood = neighbourhood

    def calculate_cost(self, seat_position: Position, simulation_configuration: SimulationConfiguration, person_id: int) -> float:
        cost = 0

        for i in range(-self._neighbourhood, self._neighbourhood + 1):
            for j in range(-self._neighbourhood, self._neighbourhood + 1):
                if i == 0 and j == 0:
                    continue

                x = seat_position.x + i
                y = seat_position.y + j
                if (
                        x < 0 or x >= simulation_configuration.classroom.width or
                        y < 0 or y >= simulation_configuration.classroom.length
                ):
                    continue

                id_seated_at = simulation_configuration.classroom.get_id_seated_at(Position(x, y))

                if id_seated_at is not None and simulation_configuration.friend_graph.are_friends(person_id, id_seated_at):
                    print(f"Found friendship between {person_id, id_seated_at}!")
                    continue


                if simulation_configuration.classroom.get_seat(Position(x, y)):
                    cost += self._weight / math.sqrt(i ** 2 + j ** 2)

        return cost


class NextToFriendsRule(Rule):
    _weight: float

    def __init__(self, weight: float):
        self._weight = weight

    def calculate_cost(self, seat_position: Position, simulation_configuration: SimulationConfiguration, person_id: int) -> float:
        cost = 0

        left_adjacent_x = seat_position.x - 1
        if left_adjacent_x >= 0:
            left_adjacent_id = simulation_configuration.classroom.get_id_seated_at(Position(left_adjacent_x, seat_position.y))
            if left_adjacent_id and simulation_configuration.friend_graph.are_friends(person_id, left_adjacent_id):
                print(f"Found friendship between {person_id, left_adjacent_id}")
                cost -= self._weight

        right_adjacent_x = seat_position.x + 1
        if right_adjacent_x < simulation_configuration.classroom.width:
            right_adjacent_id = simulation_configuration.classroom.get_id_seated_at(Position(right_adjacent_x, seat_position.y))
            if right_adjacent_id and simulation_configuration.friend_graph.are_friends(person_id, right_adjacent_id):
                print(f"Found friendship between {person_id, right_adjacent_id}")
                cost -= self._weight

        return cost


class CloseToEntranceRule(Rule):
    _weight: float

    def __init__(self, weight: float):
        self._weight = weight

    def calculate_cost(self, seat_position: Position, simulation_configuration: SimulationConfiguration, person_id: int) -> float:
        return self._weight * math.sqrt((simulation_configuration.classroom.entrance_position.x - seat_position.x) ** 2 +
                                        (simulation_configuration.classroom.entrance_position.y - seat_position.y) ** 2)
