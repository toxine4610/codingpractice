# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:22:44 2018

@author: Halassalab-CG
"""

from brian2 import *
import matplotlib.pyplot as plt

N = 5000
Vr = 10*mV
theta = 20*mV
tau = 20*ms
delta = 2*ms
taurefr = 2*ms
duration = 0.1*second
C = 1000
sparseness = float(C)/N
J = 0.1*mV
muext = 25*mV
sigmaext = 4*mV


eqs = """
dV/dt = (-V + muext +sigmaext*sqrt(tau)*xi)/tau : volt
"""
group = NeuronGroup(N, eqs, threshold = 'V>theta', reset = 'V=Vr', refractory = taurefr, method = 'euler')
group.V = Vr
conn = Synapses(group,group,on_pre = 'V+= -J',delay=delta)
conn.connect(p = sparseness)
mon = SpikeMonitor(group)

net = Network(collect())  # automatically include G and S
net.add(mon)  # manually add the monitors