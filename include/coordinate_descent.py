import numpy as np
from random import random


def coordinate_descent(x, function, initial_step=1):

    dim = len(x)
    directions = np.hsplit(np.eye(dim), dim) + np.hsplit(-np.eye(dim), dim)

    alpha, theta = initial_step, random()
    while (abs(alpha - 0) > 0.5):     # TODO

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
