import matplotlib.pyplot as plt
import numpy as np
import sphere as sphere

if __name__ == '__main__':
    # sphere function
    domain = {"start": -3, "end": +3}
    nSample = 100

    x = np.linspace(domain["start"], domain["end"], num=nSample)
    y = np.linspace(domain["start"], domain["end"], num=nSample)
    xv, yv = np.meshgrid(x, y)
    z = np.power(xv, 2) + np.power(yv, 2)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(xv, yv, z, rstride=1, cstride=1, cmap='coolwarm')
    fig.savefig('/plots/myGraph.pdf', format='pdf')
