from typing import Optional

import numpy as np

from util import Position


class Classroom:
    _layout: np.ndarray
    _seating: np.ndarray

    width: int
    length: int
    entrance_position: Position

    def __init__(self, width: int, length: int, entrance_position: Position):
        self._layout = np.zeros((length, width), dtype=int)
        self._seating = np.zeros((length, width), dtype=int)
        self.width = width
        self.length = length
        self.entrance_position = entrance_position

    def sit_at(self, position: Position, person_id: int):
        self._layout[position.y, position.x] = 1
        self._seating[position.y, position.x] = person_id

    def get_seat(self, position: Position) -> int:
        return self._layout[position.y, position.x]

    def get_id_seated_at(self, position: Position) -> Optional[int]:
        return None if self._seating[position.y, position.x] == 0 else self._seating[position.y, position.x]
