from simulation_configuration import SimulationConfiguration
from simulation import Simulation

from classroom import Classroom
from friend_graph import FriendGraph
from person import create_person
from rule_configuration import RuleConfiguration, RandomFloatRuleParameter, RandomIntRuleParameter
from rules import FrontOfClassRule, FarFromStrangersRule, CloseToEntranceRule
from util import Position

STEPS = 100


if __name__ == '__main__':
    classroom = Classroom(16, 14, entrance_position=Position(8, 15))
    images = []

    rule_configurations = [
        RuleConfiguration(
            FrontOfClassRule,
            [RandomFloatRuleParameter("weight", 0.1, 1)]
        ),
        RuleConfiguration(
            FarFromStrangersRule,
            [RandomFloatRuleParameter("weight", 0.1, 1), RandomIntRuleParameter("neighbourhood", 2, 4)]
        ),
        RuleConfiguration(
            CloseToEntranceRule,
            [RandomFloatRuleParameter("weight", 0.1, 1)]
        )
    ]

    people = []
    for i in range(STEPS):
        people.append(create_person(rule_configurations))

    friend_graph = FriendGraph([person.id for person in people])
    friend_graph.randomize_friendships(300)

    simulation = Simulation(SimulationConfiguration(classroom, friend_graph, people))
    simulation.run_simulation()
