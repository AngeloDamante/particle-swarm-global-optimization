import matplotlib.pyplot as plt
import numpy as np
# from particle import Particle
import cost_function
from swarm import Swarm


if __name__ == '__main__':
    # num_dimension = 2
    # num_iterations = 30
    # p = Particle(num_dimension, num_iterations)

    # PSO(cost_function, num_dimension, )
    # population_generator()

    bounds = [-5, +5]
    numParticles = 30
    mySwarm = Swarm(numParticles, bounds)
    print(mySwarm.particles[1].position)
    # cost_function.print_f()

# end
