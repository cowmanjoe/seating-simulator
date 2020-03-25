
import numpy as np

from util import Position


class Classroom:
    _layout: np.ndarray

    width: int
    length: int
    entrance_position: Position

    def __init__(self, width: int, length: int, entrance_position: Position):
        self._layout = np.zeros((length, width))
        self.width = width
        self.length = length
        self.entrance_position = entrance_position

    def sit_at(self, position: Position):
        self._layout[position.y, position.x] = 1

    def get_seat(self, position: Position) -> int:
        return self._layout[position.y, position.x]

