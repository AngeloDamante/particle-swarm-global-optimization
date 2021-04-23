import numpy as np
# from particle import Particle
from cost_function import sphere, ackley
from swarm import Swarm


if __name__ == '__main__':

    num_iterations = 50
    num_particles = 30
    bounds = np.array([[-5, +5], [-5, +5]])

    fitness_func = sphere

    # pso simple
    my_swarm = Swarm(num_particles, bounds)
    my_swarm.compute_global_best(fitness_func)
    for k in range(0, num_iterations):

        # coefficients policy
        inertial, cognitive, social = 0.5, 1, 2

        # move swarm
        my_swarm.update(inertial, cognitive, social)

        # evaluate local_best for swarm
        my_swarm.compute_local_best(fitness_func)

        # evaluate global_best for swarm
        my_swarm.compute_global_best(fitness_func)

        print(f"{k}:  {fitness_func(my_swarm.global_best)}")

    # end

# end


def pso():
    pass
# end
