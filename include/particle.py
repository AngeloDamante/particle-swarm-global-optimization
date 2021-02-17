import numpy as np


class Particle(object):
    """docstring for Particle."""

    def __init__(self, dimension, num_iterations):
        super(Particle, self).__init__()
        self.position = np.empty((num_iterations, dimension))
