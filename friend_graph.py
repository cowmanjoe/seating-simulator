import random
from typing import List, Dict

import numpy as np


class FriendGraph:
    _num_people: int
    _adj_matrix: np.ndarray
    _people_index: Dict[int, int] = {}
    _people_list: List[int] = []

    _num_friendships: int = 0

    # Assumes that all Person objects have unique IDs
    def __init__(self, person_ids: List[int]):
        self._num_people = len(person_ids)
        self._adj_matrix = np.zeros((self._num_people, self._num_people), dtype=int)

        for i, person_id in enumerate(person_ids):
            self._people_index[person_id] = i
            self._people_list.append(person_id)

    def randomize_friendships(self, num_friendships: int) -> None:
        self._adj_matrix = np.zeros_like(self._adj_matrix)
        self._num_friendships = 0

        while self._num_friendships < num_friendships:
            person_index1 = random.randint(0, self._num_people - 1)
            person_index2 = random.randint(0, self._num_people - 1)

            self._make_friends(self._people_list[person_index1], self._people_list[person_index2])

    def are_friends(self, person_id1: int, person_id2: int) -> bool:
        person_index1 = self._people_index[person_id1]
        person_index2 = self._people_index[person_id2]

        return self._adj_matrix[person_index1][person_index2] == 1

    def _make_friends(self, person_id1: int, person_id2: int) -> None:
        if self.are_friends(person_id1, person_id2) or person_id1 == person_id2:
            return

        person_index1 = self._people_index[person_id1]
        person_index2 = self._people_index[person_id2]

        self._adj_matrix[person_index1][person_index2] = 1
        self._adj_matrix[person_index2][person_index1] = 1

        self._num_friendships += 1
