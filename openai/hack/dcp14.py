
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)


def unifRand(a,b, S):
    # defines a uniform random between [a,b] with S points
    r = a+(b-a)*np.random.rand(S)
    return r


def monteCarloPI(epoch = 200):
    inside = 0
    radius = 4
    # area is \pi*4
    x = unifRand(-radius, radius, epoch)
    y = unifRand(-radius, radius, epoch)
    rs = x**2 + y **2
    # using PMTK method.
    pihat = np.mean(4*(rs<=radius**2))
    
    plt.figure(num=1)
    plt.plot(x[rs<=radius**2], y[rs<=radius**2], 'ro')
    plt.plot(x[rs>radius**2], y[rs>radius**2], 'bo')
    plt.axis('equal')
    return pihat
    

print("Estimated Pi = {:.3f}".format(monteCarloPI(2010)))