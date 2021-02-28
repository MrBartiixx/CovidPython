# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:59:15 2021

@author: Bartosz Wawrzyniak, Stergios Polymenidis

Covid 19
Agent Based Modelling
SIR model


"""

##################### Inputs ########################
import math
import random

from pynput import keyboard
import matplotlib.pyplot as plt
import numpy as np


##################### Functions ########################



def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener


def proximity(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))




##################### Variables ########################

### Groups ###

N = 1800  # Population
S = 1799  # Susceptible
E = 0  # Exposed
I = 1  # Infected
I_hosp = 0  # Infected hospitalized
I_icu = 0  # Infected ICU (ventilator)
R = 0  # Recovered
D = 0  # Deceased
Q = 0  # Quarantined


### Agents ###

PPL = np.zeros((N, 4))  # [x,y,group,action]
ACT = np.array(['Home', 'Work', 'WalkFree', 'Movement'])


### Environment ###

Width = 1000
Length = 1000

for n in range(N):
    PPL[n, 0] = random.uniform(0, Width)
    PPL[n, 1] = random.uniform(0, Length)

### Parameters ###

b = 0.001  # rate of contact/ contact rate
q = 0.01  # b/g # contact ratio
g = 0.05  # b / q


## Sim Time ##

T = 1000  # Time horizon

### Constraints ###

I_hosp_max = N * 0.02
I_icu_max = N * 0.01


##################### Main Loop ########################

done = False
while not done:
    print("S: ", S, "I: ", I, "R: ", R)


    S1 = S
    I1 = I
    R1 = R

    Sdot = - b * I * S
    Idot = b * I * S - g * I
    Rdot = g * I

    S = S1 + Sdot
    I = I1 + Idot
    R = R1 + Rdot

    if S < 0:
        S = 0
    if I > N:
        I = N
    if R > N:
        R = N

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys
