import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from simulation_configuration import SimulationConfiguration


class Simulation:
    configuration: SimulationConfiguration

    def __init__(self, configuration: SimulationConfiguration):
        self.configuration = configuration

    def run_simulation(self):
        images = []

        for i, person in enumerate(self.configuration.people):
            person.sit_down(self.configuration)
            x = plt.imshow(self.configuration.classroom._layout, animated=True)
            images.append([x])
            print(f"Finished step {i}")

        fig = plt.figure("animation")

        animation = ArtistAnimation(fig, images, interval=200, repeat_delay=0, blit=True)
        plt.show(animation)

