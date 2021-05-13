import matplotlib.pyplot as plt
import numpy as np


def sphere(x, delta=0):
    ''' return a single value '''
    return np.sum(np.power(x+delta, 2))
# end


def ackley(x, delta=0):
    ''' return a single value '''
    d = len(x)
    v1 = -20 * np.exp(-0.2 * np.sqrt((1 / d) * (np.sum(np.power((x+delta), 2)))))
    v2 = -np.exp((1 / d) * np.sum(np.cos(2 * np.pi * (x+delta)))) + 20 + np.exp(1)
    return (v1 + v2)
# end


def schwefel(x, delta=0):
    ''' returns schwefel 2D '''
    d = 2
    v = 0.
    for i in range(d):
        v += x[i] * np.sin(np.sqrt(np.abs(x[i])))
    return (418.9829*d - v)
# end


def sphere_grid(x, delta=0):
    '''return a ndarray'''
    return np.sum(np.power(x+delta, 2), axis=1)
# end


def ackley_grid(x, delta=0):
    '''return a ndarray'''
    d = 2
    v1 = -20 * np.exp(-0.2 * np.sqrt((1/d) * (np.sum(np.power(x+delta, 2), axis=1))))
    v2 = -np.exp((1 / d) * np.sum(np.cos(2 * np.pi * (x+delta)), axis=1)) + 20 + np.exp(1)
    return (v1 + v2)
# end


def print_f():
    '''My test to print curve level and particles with meshgrid'''

    # sphere function
    domain = {"start": -100, "end": +100}
    nSample = 100

    x = np.linspace(domain["start"], domain["end"], num=nSample)
    y = np.linspace(domain["start"], domain["end"], num=nSample)
    xv, yv = np.meshgrid(x, y)

    z = np.power(xv, 2) + np.power(yv, 2)

    fig = plt.figure('sphere')
    ax = plt.axes(projection='3d')
    ax.plot_surface(xv, yv, z, rstride=1, cstride=1, cmap='coolwarm')
    ax.scatter(1, 1, 0, marker='o', c='r')
    fig.savefig('/plots/myGraph.pdf', format='pdf')

    # TODO
    fig = plt.figure('level set')
    bx = plt.axes(projection='rectilinear')  # per la particella
    x = np.linspace(-3, 3, num=100)
    y = np.linspace(-2, 2, num=100)
    bx.scatter(x, y, marker='o', c='r')
    plt.contour(xv, yv, z, levels=10)
    fig.savefig('/plots/cont.pdf', format='pdf')

# end
