from typing import Optional

import numpy as np

from util import Position


EMPTY_SEAT = 0
NO_SEAT = -1
ENTRANCE = -2


class Classroom:
    _seating: np.ndarray

    width: int
    length: int
    entrance_position: Position

    def __init__(self, width: int, length: int, entrance_position: Position):
        self._seating = self._init_seating(width, length, entrance_position)
        self.width = width
        self.length = length
        self.entrance_position = entrance_position

    def sit_at(self, position: Position, person_id: int):
        self._set_seat(position, person_id)

    def is_seat_occupied(self, position: Position) -> bool:
        return self._get_seat(position) > 0

    def is_seat_available(self, position: Position) -> bool:
        return self._get_seat(position) == 0

    def get_id_seated_at(self, position: Position) -> Optional[int]:
        return None if self._seating[position.y, position.x] <= 0 else self._seating[position.y, position.x]

    def get_occupancy_matrix(self) -> np.ndarray:
        return np.minimum(self._seating, np.full_like(self._seating, 1))

    def _init_seating(self, width: int, length: int, entrance_position: Position) -> np.ndarray:
        assert 0 <= entrance_position.x < width
        assert 0 <= entrance_position.y < length

        seating = np.zeros((length, width), dtype=int)

        seating[:, 0] = np.full_like(seating[:, 0], NO_SEAT)
        seating[:, width - 1] = np.full_like(seating[:, 0], NO_SEAT)
        seating[0] = np.full_like(seating[0], NO_SEAT)
        seating[length - 1] = np.full_like(seating[0], NO_SEAT)

        seating[entrance_position.y, entrance_position.x] = ENTRANCE

        return seating

    def _get_seat(self, position: Position) -> int:
        return self._seating[position.y, position.x]

    def _set_seat(self, position: Position, value: int) -> None:
        self._seating[position.y, position.x] = value
