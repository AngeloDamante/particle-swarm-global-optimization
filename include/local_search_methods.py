import numpy as np
from random import random


def coordinate_descent(x, function, bounds, initial_step=1):
    """Implements derivative free method, coordinate descent.

    The stopping rule has been implemented, observing the proximity
    of the step with zero.

    Args:
        x(ndarray): initial point to minimize with shape (dim, 1)
        function(function): function to minimize
        bounds(ndarray): bounds per axis (nx2), with n-dimensions
        initial_step(double): initial step for local search method

    """

    dim = len(x)
    directions = np.hsplit(np.eye(dim), dim) + np.hsplit(-np.eye(dim), dim)

    lower = bounds[:, 0].reshape((dim, 1))
    upper = bounds[:, 1].reshape((dim, 1))

    alpha, theta = initial_step, random()
    while (abs(alpha - 0) > 0.2):

        exist_dir, i = False, 0
        while(exist_dir is False and i < len(directions)):
            new_position = np.clip(x + alpha * directions[i], lower, upper)
            if function(new_position) < function(x):
                d_star = directions[i]
                exist_dir = True
            else:
                i += 1
        # end

        if (exist_dir):
            x += alpha * d_star
            x = np.clip(x, lower, upper)
        else:
            alpha = theta * alpha
        # end

    # end

    return x
# end
