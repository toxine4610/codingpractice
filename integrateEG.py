
'''
Two objects with masses m1 and m2 are coupled through springs with spring constants k1 and k2. The left end of the left spring is fixed. We assume that the lengths of the springs, when subjected to no external forces, are L1 and L2.

The masses are sliding on a surface that creates friction, so there are two friction coefficients, b1 and b2.

The differential equations for this system are

m1x″1+b1x′1+k1(x1−L1)−k2(x2−x1−L2)=0
m2x″2+b2x′2+k2(x2−x1−L2)=0

x′1=y1 
y′1=(−b1y1−k1(x1−L1)+k2(x2−x1−L2))/m1
x′2=y2
y′2=(−b2y2−k2(x2−x1−L2))/m2

'''
import sys
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from scipy.integrate import odeint

def system_of_equations(w, t, p):
	x1, y1, x2, y2 = w
	m1, m2, k1, k2, L1, L2, b1, b2 = p
	f = [y1,
         (-b1 * y1 - k1 * (x1 - L1) + k2 * (x2 - x1 - L2)) / m1,
         y2,
         (-b2 * y2 - k2 * (x2 - x1 - L2)) / m2]
	return f


print("\n--> Loading parameters...")
# Parameter values
# Masses:
m1 = 2.0
m2 = 1.5
# Spring constants
k1 = 8.0
k2 = 40.0
# Natural lengths
L1 = 0.5
L2 = 1.0
# Friction coefficients
b1 = 0.8
b2 = 0.5

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1 = 0.5
y1 = 0.0
x2 = 2.25
y2 = 0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 5000

# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]


for m1 in range(1,10):
	# Pack up the parameters and initial conditions:
	p = [m1, m2, k1, k2, L1, L2, b1, b2]
	w0 = [x1, y1, x2, y2]

	# Call the ODE solver.
	wsol = odeint(system_of_equations, w0, t, args=(p,),
	      atol=abserr, rtol=relerr)
	print("--> Solving with m1 = {0}.\n".format(m1))


	X1 = []
	X2 = []
	for _, w1 in zip(t, wsol):
		X1.append(w1[0])
		X2.append(w1[2])

	pl.figure(1, figsize=(6,6))
	pl.xlabel('t')
	pl.plot(t, X1, 'b', linewidth=1)
	pl.plot(t, X2, 'g', linewidth=1)
	pl.legend((r'$x_1$', r'$x_2$'))
	pl.title('Mass Displacements for the\nCoupled Spring-Mass System')

pl.show()