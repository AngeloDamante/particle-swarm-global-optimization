import numpy as np
from random import random


class Particle(object):
    """Implements Particle object with its property and activities.

    Attributes:
        position(ndarray): x-vector of particle (dimx1)
        velocity(ndarray): v-vector of particle (dimx1)
        local_best(ndarray): p-vector of particle (dimx1)

    """

    def __init__(self, bounds):
        """Initilizes position and velocity of a particle.

        Args:
            bounds(ndarray): bounds per axis (nx2), with n-dimensions

        """
        super(Particle, self).__init__()

        n_dim = len(bounds)
        lower = bounds[:, 0]
        upper = bounds[:, 1]

        self.position = np.random.uniform(lower, upper).reshape(n_dim, 1)
        self.velocity = np.random.uniform(size=(n_dim, 1))
        self.local_best = self.position.copy()
    # end

    def get_position(self):
        """A simply get method.

        Returns:
            position(ndarray): with shape (dim, 1)

        """
        position = self.position.copy()
        return position
    # end

    def get_velocity(self):
        """A simply get method.

        Returns:
            velocity(ndarray): with shape (dim, 1)
        """
        velocity = self.velocity.copy()
        return velocity
    # end

    def get_local_best(self):
        """A simply get method.

        Returns:
            local_best(ndarray): with shape (dim, 1)

        """
        p = self.local_best.copy()
        return p
    # end

    def update_position(self):
        """In according with PSO theory, this method updates position."""
        self.position += self.velocity
    # end

    def update_velocity(self, w, c1, c2, global_best):
        """In according with PSO theory, this method updates velocity.

        Args:
            w(double): inertial constant
            c1(double): cognitive constant
            c2(double): social constant
            global_best(ndarray): best global position of the swarm

        """
        inertial_term = w * self.velocity
        cognitive_term = c1 * random() * (self.local_best - self.position)
        social_term = c2 * random() * (global_best - self.position)

        self.velocity = inertial_term + cognitive_term + social_term
    # end

    def evaluate_local_best(self, cost_function):
        """Compute the local best as the minimum value taken by the cost function.

        Args:
            cost_function(function): to evaluate particle's position

        """
        value = cost_function(self.position)
        if value < cost_function(self.local_best):
            self.local_best = self.position.copy()
    # end

# end
