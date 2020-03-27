from simulation_configuration import SimulationConfiguration
from simulation import Simulation

from classroom import Classroom
from friend_graph import FriendGraph
from person import create_person
from rule_configuration import RuleConfiguration, RandomFloatRuleParameter, RandomIntRuleParameter
from rules import FrontOfClassRule, FarFromStrangersRule, CloseToEntranceRule, NextToFriendsRule
from util import Position

STEPS = 300


if __name__ == '__main__':
    classroom = Classroom(40, 31, entrance_position=Position(40, 15))
    images = []

    rule_configurations = [
        RuleConfiguration(
            FrontOfClassRule,
            [RandomFloatRuleParameter("weight", 0.1, 0.1)]
        ),
        RuleConfiguration(
            FarFromStrangersRule,
            [RandomFloatRuleParameter("weight", 5, 10), RandomIntRuleParameter("neighbourhood", 2, 4)]
        ),
        RuleConfiguration(
            CloseToEntranceRule,
            [RandomFloatRuleParameter("weight", 0.1, 0.1)]
        ),
        RuleConfiguration(
            NextToFriendsRule,
            [RandomFloatRuleParameter("weight", 5, 10)]
        )
    ]

    people = []
    for i in range(STEPS):
        people.append(create_person(rule_configurations))

    friend_graph = FriendGraph([person.id for person in people])
    friend_graph.randomize_friendships(50)

    simulation = Simulation(SimulationConfiguration(classroom, friend_graph, people))
    simulation.run_simulation()
