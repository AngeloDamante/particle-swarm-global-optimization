import numpy as np
from cost_function import sphere, ackley
from swarm import Swarm


def standard_pso(num_iterations, num_particles, bounds, fitness_func):
    my_swarm = Swarm(num_particles, bounds)
    my_swarm.compute_global_best(fitness_func)
    for k in range(0, num_iterations):

        # coefficients policy
        inertial, cognitive, social = compute_coefficients(k, num_iterations)
        # inertial, cognitive, social = 0.5, 1, 2

        # move swarm
        my_swarm.move(inertial, cognitive, social)

        # evaluate local_best for swarm
        my_swarm.compute_local_best(fitness_func)

        # evaluate global_best for swarm
        my_swarm.compute_global_best(fitness_func)

        print(f"{k}:  {fitness_func(my_swarm.global_best)}")

    # end

    print(f"final solution is: {my_swarm.global_best}")
# end


def compute_coefficients(iter, num_iter):
    t, n = iter, num_iter
    w = (0.4 / n**2) * (t - n) ** 2 + 0.4
    c1 = -3 * t / n + 3.5
    c2 = 3 * t / n + 0.5

    return w, c1, c2
# end


def memetic_pso(num_iterations, num_particles, bounds, fitness_func):
    pass
# end


if __name__ == '__main__':

    num_iterations = 50
    num_particles = 30
    bounds = np.array([[-5, +5], [-5, +5]])
    fitness_func = sphere

    # standard_pso(num_iterations, num_particles, bounds, fitness_func)
    memetic_pso(num_iterations, num_particles, bounds, fitness_func)
# end
