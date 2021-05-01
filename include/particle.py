import numpy as np
from random import random


class Particle(object):
    """docstring for Particle."""

    def __init__(self, bounds):
        super(Particle, self).__init__()

        n_dim = len(bounds)
        lower = bounds[:, 0]
        upper = bounds[:, 1]

        # self.position = np.array([5., 5.]).reshape(n_dim, 1)
        self.position = np.random.uniform(lower, upper).reshape(n_dim, 1)

        self.velocity = np.random.uniform(size=(n_dim, 1))

        self.local_best = self.position.copy()
    # end

    def update_velocity(self, w, c1, c2, global_best):
        inertial_term = w * self.velocity
        cognitive_term = c1 * random() * (self.local_best - self.position)
        social_term = c2 * random() * (global_best - self.position)

        self.velocity = inertial_term + cognitive_term + social_term
    # end

    def update_position(self):
        self.position += self.velocity
    # end

    def evaluate(self, cost_function):
        value = cost_function(self.position)
        if value < cost_function(self.local_best):
            self.local_best = self.position.copy()
    # end

# end
