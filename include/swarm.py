import numpy as np
from random import random
from particle import Particle


class Swarm(object):
    """docstring for Particle."""

    def __init__(self, num_particles, bounds):
        super(Swarm, self).__init__()

        self.num_particles = num_particles
        self.particles = []
        self.local_best = []
        self.global_best = None

        for i in range(0, num_particles):
            self.particles.append(Particle(bounds))
        # end

        self.best_local = self.particles
    # end

    def get_particles_position(self):
        for i in range(0, self.num_particles):
            print(self.particles[i].position)
        # end
    # end

    def get_particles_velocity(self):
        for i in range(0, self.num_particles):
            print(self.particles[i].velocity)
        # end
    # end

    def compute_global_(cost_function):
        g = cost_function(self.particles[0].local_best)
        for i in range(1, num_particles):
            value = cost_function(self.particles[i].local_best)
            if g > value:
                g = value
        # end
        self.global_best = g
    # end

    def update(self, inertia, cognitive, social):
        w, c1, c2 = inertia, cognitive, social

        for i in range(0, self.num_particles):
            self.particles[i].update_velocity(w, c1, c2, self.global_best)
            self.particles[i].update_position()
        # end
    # end

# end
