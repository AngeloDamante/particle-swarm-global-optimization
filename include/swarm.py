import numpy as np
from random import random
# from uniform import uniform
from particle import Particle


class Swarm(object):
    """docstring for Particle."""

    def __init__(self, num_particles, bounds):
        super(Swarm, self).__init__()
        self.particles = []
        self.num_particles = num_particles

        for k in range(0, num_particles):
            self.particles.append(Particle(bounds))
        # end

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

    def update(self, inertia, cognitive, social):
        for i in range(0, self.num_particles):
            self.particles[i].update_velocity(inertial, cognitive, social)
            self.particles[i].update_position()
        # end
    # end

# end
