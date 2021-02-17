import numpy as np


class Particle(object):
    """docstring for Particle."""

    def __init__(self, dimension, num_iterations):
        super(Particle, self).__init__()
        self.position = np.empty((num_iterations, dimension))
        self.velocity = np.empty((num_iterations, dimension))
        self.best_position = np.empty((num_iterations, dimension))

        self.fitness = None
        self.best_fitness = None

    def update_position():
        pass

    def update_velocity():
        pass

    def evaluate():
        pass
