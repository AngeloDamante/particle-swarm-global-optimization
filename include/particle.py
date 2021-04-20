import numpy as np
from random import random
# from uniform import uniform


class Particle(object):
    """docstring for Particle."""

    def __init__(self, bounds):
        super(Particle, self).__init__()
        dimension = len(bounds)

        self.position = np.random.uniform(bounds[0], bounds[1], (dimension, 1))
        self.velocity = np.zeros((dimension, 1))

    # end

    def update_position():
        pass
    # end

    def update_velocity():
        pass

    def evaluate():
        pass
    # end
