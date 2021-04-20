import numpy as np
from random import random
# from uniform import uniform
from particle import Particle


class Swarm(object):

    def __init__(self, numParticles, bounds):
        super(Swarm, self).__init__()
        self.particles = []
        self.numParticles = numParticles

        for k in range(0, numParticles):
            self.particles.append(Particle(bounds))
        # end

    # end

    def get_particles_position(self):
        for i in range(0, self.numParticles):
            print(self.particles[i].position)
        # end
    # end

    def get_particles_velocity(self):
        for i in range(0, self.numParticles):
            print(self.particles[i].velocity)
        # end
    # end

    def update(self, inertial, cognitive, social):
        pass
    # end

# end
