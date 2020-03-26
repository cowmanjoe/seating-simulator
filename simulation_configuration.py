from __future__ import annotations
from dataclasses import dataclass
from typing import List, TYPE_CHECKING

from classroom import Classroom
from friend_graph import FriendGraph

if TYPE_CHECKING:
    from person import Person

@dataclass
class SimulationConfiguration:
    classroom: Classroom
    friend_graph: FriendGraph
    people: List[Person]
