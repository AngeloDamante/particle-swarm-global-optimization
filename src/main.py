import numpy as np
# from particle import Particle
import cost_function
from swarm import Swarm


if __name__ == '__main__':

    # pso simple

    num_iterations = 50
    num_particles = 30
    bounds = [[-5, +5], [-5, +5]]

    my_swarm = Swarm(num_particles, bounds)
    for k in range(1, num_iterations):
        # coefficients
        my_swarm.update(inertial, cognitive, social)
    # end

# end
