from local_search_methods import coordinate_descent
from swarm import Swarm
from cost_function import sphere, ackley, schwefel
import numpy as np

__author__ = 'Angelo D.Amante'
__mail__ = 'angelo.damante16@gmail.com'
__git__ = 'https://github.com/AngeloDamante/particle-swarm-global-optimization'


def compute_coefficients(iter, num_iter):
    t, n = iter, num_iter
    w = (0.4 / n**2) * (t - n) ** 2 + 0.4
    c1 = -3 * t / n + 3.5
    c2 = 3 * t / n + 0.5

    return w, c1, c2
# end


def standard_pso(num_iterations, num_particles, bounds, fitness_func):
    my_swarm = Swarm(num_particles, bounds)  # initial population
    my_swarm.find_global_best(fitness_func)  # set global best for swarm
    for k in range(0, num_iterations):

        # coefficients policy
        # inertial, cognitive, social = compute_coefficients(k, num_iterations)
        inertial, cognitive, social = 0.729, 2.05, 2.05

        # move swarm
        my_swarm.move(inertial, cognitive, social)

        # evaluate local_best for swarm
        my_swarm.compute_local_best(fitness_func)

        # evaluate global_best for swarm
        my_swarm.find_global_best(fitness_func)

        print(f"{k}:  {fitness_func(my_swarm.global_best)}")

    # end

    print(f"final solution is: {my_swarm.global_best}")
# end


def memetic_pso(num_iterations, num_particles, bounds, fitness_func, local_search_method):
    my_swarm = Swarm(num_particles, bounds)  # initial population
    my_swarm.find_local_best(coordinate_descent, fitness_func, bounds, initial_step=5)
    my_swarm.find_global_best(fitness_func)  # set global best for swarm
    for k in range(0, num_iterations):

        # coefficients policy
        # inertial, cognitive, social = compute_coefficients(k, num_iterations)
        inertial, cognitive, social = 0.729, 2.05, 2.05

        # move swarm
        my_swarm.move(inertial, cognitive, social)

        # evaluate local_best for swarm
        my_swarm.find_local_best(
            coordinate_descent, fitness_func, bounds, initial_step=5)

        # evaluate global_best for swarm
        my_swarm.find_global_best(fitness_func)

        print(f"{k}:  {fitness_func(my_swarm.global_best)}")

    # end

    print(f"final solution is: {my_swarm.global_best}")
# end


if __name__ == '__main__':
    """A simple test function before implement notebook jupyter."""

    num_iterations = 50
    num_particles = 30

    # test for ackley
    # bounds = np.array([[-5, +5], [-5, +5], [-5, +5]])
    # fitness_func = ackley

    # test for schwefel
    bounds = np.array([[-500, +500], [-500, +500], [-500, 500]])
    fitness_func = schwefel

    # Two function implemented
    # standard_pso(num_iterations, num_particles, bounds, fitness_func)
    memetic_pso(num_iterations, num_particles, bounds, fitness_func, coordinate_descent)

# end
