
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy import optimize as sco

x, y = np.mgrid[-2.03:4.2:.04, -1.6:3.2:.04]
x = x.T
y = y.T

pl.figure(1, figsize = (3,2.5))
pl.clf()
pl.axes([0,0,1,1])

fn = lambda x, y: (x-3)**2 + (y-2)**2 # equation of a circle.

cont = pl.contour( np.sqrt(fn(x,y)), 
				   extent = [-2.03, 4.2, -1.6, 3.2],
				   cmap = pl.cm.gnuplot )

pl.clabel(cont, inline = 1, fmt = '%1.1f', fontsize = 14)

pl.plot([-1.5,    0,  1.5,    0, -1.5],
        [   0,  1.5,    0, -1.5,    0], 'k', linewidth=2)
pl.fill_between([ -1.5,    0,  1.5],
                [    0, -1.5,    0],
                [    0,  1.5,    0],
                color='.8')
pl.axvline(0, color='k')
pl.axhline(0, color='k')

pl.text(-.9, 2.8, '$x_2$', size=20)
pl.text(3.6, -.6, '$x_1$', size=20)
pl.axis('tight')
pl.axis('off')

################

accumulator = list()
def f(x):
	accumulator.append(x)
	return fn(x[0], x[1])

def constraint(x):
    return np.atleast_1d(1.5 - np.sum(np.abs(x)))

sco.minimize(f, np.array([0, 0]), method="SLSQP",
                     constraints={"fun": constraint, "type": "ineq"})

accumulated = np.array(accumulator)
pl.plot(accumulated[:, 0], accumulated[:, 1])
pl.show()


