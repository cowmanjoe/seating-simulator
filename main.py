from simulation_configuration import SimulationConfiguration
from simulation import Simulation

from classroom import Classroom
from friend_graph import FriendGraph
from person import create_person
from rule_configuration import RuleConfiguration, RandomFloatRuleParameter, RandomIntRuleParameter
from rules import FrontOfClassRule, FarFromStrangersRule, CloseToEntranceRule, NextToFriendsRule
from util import Position

NUM_PEOPLE = 200
NUM_FRIENDSHIPS = 100

CLASS_WIDTH = 25
CLASS_HEIGHT = 15

ENTRANCE_POSITION = Position(12, 15)

FRONT_OF_CLASS_WEIGHT_LOWER = 0.1
FRONT_OF_CLASS_WEIGHT_UPPER = 1

FAR_FROM_STRANGERS_WEIGHT_LOWER = 0.5
FAR_FROM_STRANGERS_WEIGHT_UPPER = 1.5
FAR_FROM_STRANGERS_NEIGHBOURHOOD_LOWER = 2
FAR_FROM_STRANGERS_NEIGHBOURHOOD_UPPER = 4

CLOSE_TO_ENTRANCE_WEIGHT_LOWER = 0.1
CLOSE_TO_ENTRANCE_WEIGHT_UPPER = 0.5

NEXT_TO_FRIENDS_WEIGHT_LOWER = 1
NEXT_TO_FRIENDS_WEIGHT_UPPER = 3


if __name__ == '__main__':
    classroom = Classroom(CLASS_WIDTH, CLASS_HEIGHT, entrance_position=ENTRANCE_POSITION)
    images = []

    rule_configurations = [
        RuleConfiguration(
            FrontOfClassRule,
            [RandomFloatRuleParameter("weight", FRONT_OF_CLASS_WEIGHT_LOWER, FRONT_OF_CLASS_WEIGHT_UPPER)]
        ),
        RuleConfiguration(
            FarFromStrangersRule,
            [RandomFloatRuleParameter(
                "weight",
                FAR_FROM_STRANGERS_WEIGHT_LOWER, FAR_FROM_STRANGERS_WEIGHT_UPPER),
                RandomIntRuleParameter("neighbourhood", FAR_FROM_STRANGERS_NEIGHBOURHOOD_LOWER, FAR_FROM_STRANGERS_NEIGHBOURHOOD_UPPER)]
        ),
        RuleConfiguration(
            CloseToEntranceRule,
            [RandomFloatRuleParameter("weight", CLOSE_TO_ENTRANCE_WEIGHT_LOWER, CLOSE_TO_ENTRANCE_WEIGHT_UPPER)]
        ),
        RuleConfiguration(
            NextToFriendsRule,
            [RandomFloatRuleParameter("weight", NEXT_TO_FRIENDS_WEIGHT_LOWER, NEXT_TO_FRIENDS_WEIGHT_UPPER)]
        )
    ]

    people = []
    for i in range(NUM_PEOPLE):
        people.append(create_person(rule_configurations))

    friend_graph = FriendGraph([person.id for person in people])
    friend_graph.randomize_friendships(NUM_FRIENDSHIPS)

    simulation = Simulation(SimulationConfiguration(classroom, friend_graph, people))
    simulation.run_simulation()
