import numpy as np
from random import random
# from uniform import uniform


class Particle(object):
    """docstring for Particle."""

    def __init__(self, bounds):
        super(Particle, self).__init__()
        dimension = len(bounds)

        self.position = np.random.uniform(
            bounds[0][0], bounds[1][1], (dimension, 1))  # FIXME
        self.velocity = np.zeros((dimension, 1))

    # end

    def update_velocity(self, w, c1, c2, local_best, global_best):
        inertial_term = w * self.velocity
        cognitive_term = c1 * random() * (local_best - self.position)
        social_term = c2 * random() * (global_best - self.position)

        self.velocity = inertial_term + cognitive_term + social_term
    # end

    def update_position(self):
        pass
    # end

    def evaluate():
        pass
    # end

# end
