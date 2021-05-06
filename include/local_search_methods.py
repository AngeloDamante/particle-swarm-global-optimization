import numpy as np
from random import random


def coordinate_descent(x, function, initial_step=1):
    """Implements derivative free method, coordinate descent.

    The stopping rule has been implemented, observing the proximity
    of the step with zero.

    Args:
        x(ndarray): initial point to minimize with shape (dim, 1)
        function(function): function to minimize
        initial_step(double): initial step for local search method

    """

    dim = len(x)
    directions = np.hsplit(np.eye(dim), dim) + np.hsplit(-np.eye(dim), dim)

    alpha, theta = initial_step, random()
    while (abs(alpha - 0) > 0.5):

        exist_dir, i = False, 0
        while(exist_dir is False and i < len(directions)):
            if function(x + alpha * directions[i]) < function(x):
                d_star = directions[i]
                exist_dir = True
            else:
                i += 1
        # end

        if (exist_dir):
            x += alpha * d_star
        else:
            alpha = theta * alpha
        # end

    # end

    return x
# end
