import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation

from classroom import Classroom
from person import Person
from rules import Rule, FrontOfClassRule, FarFromStrangersRule, CloseToEntranceRule
from util import Position

STEPS = 100


if __name__ == '__main__':
    classroom = Classroom(16, 12, entrance_position=Position(25, 15))
    images = []

    for i in range(STEPS):
        person = Person([FrontOfClassRule(1), FarFromStrangersRule(1, neighbourhood=3), CloseToEntranceRule(1)])
        person.sit_down(classroom)

        x = plt.imshow(classroom._layout, animated=True)
        images.append([x])
        print(i)

    fig = plt.figure("ASDF")

    animation = ArtistAnimation(fig, images, repeat_delay=0, blit=True)
    plt.show()

