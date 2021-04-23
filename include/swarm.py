import numpy as np
from random import random
from particle import Particle


class Swarm(object):
    """docstring for Particle."""

    def __init__(self, num_particles, bounds):
        super(Swarm, self).__init__()

        self.num_particles = num_particles
        self.dim = len(bounds)

        self.particles = []
        for i in range(0, num_particles):
            self.particles.append(Particle(bounds))
        # end

        self.global_best = self.particles[0].local_best

    # end

    def get_particles_position(self):
        actual_position = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            actual_position[i] = np.transpose(self.particles[i].position)
        # end
        return actual_position
    # end

    def get_particles_velocity(self):
        actual_velocity = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            actual_velocity[i] = np.transpose(self.particles[i].velocity)
        # end
        return actual_velocity
    # end

    def get_local_best(self):
        local_best = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            local_best[i] = np.transpose(self.particles[i].local_best)
        # end
        return local_best
    # end

    def compute_local_best(self, cost_function):
        for i in range(0, self.num_particles):
            self.particles[i].evaluate(cost_function)
        # end
    # end

    def compute_global_best(self, cost_function):
        g = cost_function(self.global_best)
        for i in range(0, self.num_particles):
            if g > cost_function(self.particles[i].local_best):
                self.global_best = self.particles[i].local_best
        # end
    # end

    def update(self, inertia, cognitive, social):
        w, c1, c2 = inertia, cognitive, social

        for i in range(0, self.num_particles):
            self.particles[i].update_velocity(w, c1, c2, self.global_best)
            self.particles[i].update_position()
        # end
    # end

# end
