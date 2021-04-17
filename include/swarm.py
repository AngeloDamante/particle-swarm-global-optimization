import numpy as np
from random import random
from uniform import uniform
from particle import Particle


class Swarm(object):

    def __init__(self, numParticles, bounds):
        super(Swarm, self).__init__()

        self.particles = []

        for k in range(0, numParticles):
            self.particles[k].append(Particle(bounds))
        # end

    # end
