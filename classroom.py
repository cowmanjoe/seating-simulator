from typing import Optional

import numpy as np

from util import Position


class Classroom:
    _seating: np.ndarray

    width: int
    length: int
    entrance_position: Position

    def __init__(self, width: int, length: int, entrance_position: Position):
        self._seating = np.zeros((length, width), dtype=int)
        self.width = width
        self.length = length
        self.entrance_position = entrance_position

    def sit_at(self, position: Position, person_id: int):
        self._seating[position.y, position.x] = person_id

    def is_seat_occupied(self, position: Position) -> bool:
        return self._seating[position.y, position.x] > 0

    def get_id_seated_at(self, position: Position) -> Optional[int]:
        return None if self._seating[position.y, position.x] == 0 else self._seating[position.y, position.x]

    def get_occupancy_matrix(self):
        return np.minimum(self._seating, np.full_like(self._seating, 1))