# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 08:56:13 2018

@author: Halassalab-CG
"""

def dcp21(times):
    start_times = [(t[0], 1) for t in times]
    end_times   = [(t[1],-1) for t in times]
    eventStamps = [t[1] for t in sorted(start_times+end_times, key = lambda t: t[0] )]
    
    maxRoom = 1
    room    = 0
    
    for event in eventStamps:
        room += event
        if room > maxRoom:
            maxRoom =  room
    return maxRoom


times = [(0, 50), (55, 59), (60, 150)]
print("Max Number of rooms = {}".format(dcp21(times)))