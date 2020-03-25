import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from classroom import Classroom
from person import Person, create_person
from rule_configuration import RuleConfiguration, RandomFloatRuleParameter, RandomIntRuleParameter
from rules import FrontOfClassRule, FarFromStrangersRule, CloseToEntranceRule
from util import Position

STEPS = 100


if __name__ == '__main__':
    classroom = Classroom(16, 12, entrance_position=Position(25, 15))
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


    for i in range(STEPS):
        person = create_person(rule_configurations)
        person.sit_down(classroom)


        x = plt.imshow(classroom._layout, animated=True)
        images.append([x])
        print(f"Finished step {i}")

    fig = plt.figure("animation")


    animation = ArtistAnimation(fig, images, repeat_delay=0, blit=True)
    plt.show()

