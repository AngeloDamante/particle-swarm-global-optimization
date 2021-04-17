import matplotlib.pyplot as plt
import numpy as np


def sphere(x):
    return np.sum(np.power(x, 2))
# end


def ackley(x):
    d = len(x)
    v1 = -20 * np.exp(-0.2 * np.sqrt((1 / d) * (np.sum(np.power(x, 2)))))
    v2 = -np.exp((1 / d) * np.sum(np.cos(2 * np.pi * x))) + 20 + np.e
    return (v1 + v2)
# end


def print_f():
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

    fig = plt.figure('level set')
    bx = plt.axes(projection='rectilinear')
    x = np.linspace(-3, 3, num=100)
    y = np.linspace(-2, 2, num=100)
    bx.scatter(x, y, marker='o', c='r')
    plt.contour(xv, yv, z, levels=10)
    fig.savefig('/plots/cont.pdf', format='pdf')

# end
