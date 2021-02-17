import matplotlib.pyplot as plt
import numpy as np


def function():
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
