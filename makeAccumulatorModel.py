# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:41:30 2018

@author: Halassalab-CG
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

# freeze the noise
np.random.seed(0)

def makePoissonTrain(rate):
    times = np.linspace(0,30,2000)
    dt    = np.round(times[1]-times[0],3)
    spikes = np.zeros(len(times))
    for i in range(len(times)):
        if (rate*dt) > np.random.rand():
            spikes[i] = 1
    return [spikes, times]

def convolveKernel(spike):
    window =  signal.exponential(100, 0, 25, False)
    return np.convolve(spike,window,mode='same')
    

def genInputs(rate1, rate2):
    spikes_A, _ = makePoissonTrain(rate1)
    spikes_B, times = makePoissonTrain(rate2)
    
    spikes_A = convolveKernel(spikes_A)
    spikes_B = convolveKernel(spikes_B)
    return spikes_A, spikes_B, times


def theoreticalAccumulator(rate1,rate2):
    spikes_A, spikes_B, times = genInputs(rate1, rate2)
    Acc = np.zeros(len(times))
    lam = 0.04
    dt  = 0.001
    
    for i in range(0, len(times)-1):
        gwn = 0.1*np.random.randn()
        Acc[i+1] = (1+dt*lam)*Acc[i] + dt*(spikes_A[i] - spikes_B[i] + gwn )
    return Acc, spikes_A, spikes_B, times

def buildCircuitModel(Acc, spikes_A, spikes_B, times):
    # builds Murray and Wang model JNeurosci
    return True
    













##### MAIN...

jet = cm = plt.get_cmap('plasma') 
cNorm  = colors.Normalize(vmin=0, vmax=6)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

ct= 0
v = [1,0.8,0.6,0.4,0.2,0]
slope = []

for i in v:
    colorVal = scalarMap.to_rgba(ct)

    Acc_hard, spikes_A_hard, spikes_B_hard, times = theoreticalAccumulator(i,1-i)    
    slope.append(  Acc_hard[-1] - Acc_hard[0] )
    
    plt.figure(num=1)
    plt.plot(times, Acc_hard, color = colorVal )
    ct += 1


plt.figure(num=2)
plt.plot(v, slope)

    
    
    
    
    #plt.plot(times, Acc_easy)   
    
