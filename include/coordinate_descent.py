import numpy as np


def coordinate_descent(x, fitness_func):
    dim = len(x)
    directions = np.hsplit(np.eye(dim), dim) + np.hsplit(-np.eye(dim), dim)

    k = 0

    return local_best
# end
