import numpy as np
from random import random
from particle import Particle


class Swarm(object):
    """Implements Swarm with its particles and actions.

    Attributes:
        num_particles(int): number of particles for the swarm
        dim(int): n-dimensions
        particles(list): instantiated particles
        global_best(ndarray): best position for the swarm (dimx1)

    """

    def __init__(self, num_particles, bounds):
        """ Randomly initializes the population.

        Args:
            num_particles(int): number of particles for the swarm
            bounds(ndarray): bounds per axis (nx2), with n-dimensions

        """
        super(Swarm, self).__init__()

        self.num_particles = num_particles
        self.dim = len(bounds)

        self.particles = []
        for i in range(0, num_particles):
            self.particles.append(Particle(bounds))
        # end

        self.global_best = self.particles[0].local_best

    # end

    def get_global_best():
        """A simply get method.

        Returns:
            global_best(ndarray): with shape (dim, 1)

        """

        p_star = self.global_best.copy()
        return p_star
    # end

    def find_global_best(self, cost_function):
        """Compute global best for the entire swarm.

        Args:
            cost_function(function): fitness function to evaluate positions

        """
        # g = cost_function(self.particles[0].local_best)
        g = cost_function(self.global_best)
        for i in range(0, self.num_particles):
            if g > cost_function(self.particles[i].local_best):
                self.global_best = (self.particles[i].local_best).copy()
                g = cost_function(self.particles[i].local_best)
        # end
    # end

    def get_particles_position(self):
        """A simply get method that return all position of swarm's particles.

        Returns:
            positions(ndarray): with shape (num_particles, dim)

        """
        actual_position = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            actual_position[i] = np.transpose(self.particles[i].get_position())
        # end
        return actual_position
    # end

    def get_particles_velocity(self):
        """A simply get method that return all velocity of swarm's particles.

        Returns:
            velocities(ndarray): with shape (num_particles, dim)

        """
        actual_velocity = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            actual_velocity[i] = np.transpose(self.particles[i].get_velocity())
        # end
        return actual_velocity
    # end

    def get_particles_local_best(self):
        """A simply get method that return all individual best of particles.

        Returns:
            local_best(ndarray): with shape (num_particles, dim)

        """
        local_best = np.zeros((self.num_particles, self.dim))
        for i in range(0, self.num_particles):
            local_best[i] = np.transpose(self.particles[i].get_local_best())
        # end
        return local_best
    # end

    def get_state(self):
        """A simply get method that return state of swarm.

        Returns:
            state(list): [positions | velocities | local_best | global_best]

        """
        positions = self.get_particles_position()
        velocities = self.get_particles_velocity()
        local_best = self.get_particles_local_best()
        global_best = self.global_best

        state = [positions, velocities, local_best, global_best]
        return state
    # end

    def move(self, inertia, cognitive, social):
        """In according to PSO theory, move the swarm following two equations.

        Args:
            inertia(double): inertia constant
            cognitive(double): cognitive constant
            social(double): cognitive constant

        """
        w, c1, c2 = inertia, cognitive, social

        for i in range(0, self.num_particles):
            self.particles[i].update_velocity(w, c1, c2, self.global_best)
            self.particles[i].update_position()
        # end
    # end

    def compute_local_best(self, cost_function):
        """To evaluate all position and update individual best of swarm.

        This method updates the individual bests simply by comparing the
        current position and the previous individual best with the cost
        function, in according to PSO standard theory.

        Args:
            cost_function(function): cost function to evaluate swarm's position.

        """
        for i in range(0, self.num_particles):
            self.particles[i].evaluate_local_best(cost_function)
        # end
    # end

    def find_local_best(self, local_search_method, cost_function, bounds, initial_step=1):
        """To implement memetic variant to standard PSO.

        This method, equips PSO with a local_search_method to improve
        perfomances of PSO.

        Args:
            local_search_method(function): local_search_method used
            cost_function(function): cost function to minimize
            initial_step(double): initial step for local_search_method

        """
        for i in range(0, self.num_particles):
            x = self.particles[i].position
            self.particles[i].local_best = local_search_method(
                x, cost_function, bounds, initial_step)
        # end
    # end


# end
