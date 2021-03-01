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

#from pynput import keyboard
import matplotlib.pyplot as plt
import numpy as np


##################### Functions ########################

class Human:

    dx = 1
    dy = 1

    def __init__(self, x, y, group, action, x_home, y_home, x_work, y_work):
        self.x = x
        self.y = y
        self.group = group
        self.action = action
        self.x_home = x_home
        self.y_home = y_home
        self.x_work = x_work
        self.y_work = y_work


    def actionGoHome(self):
        if self.x < self.x_home:
            self.x = self.x + self.dx
        if self.x > self.x_home:
            self.x = self.x - self.dx
        if self.y < self.y_home:
            self.y = self.y + self.dy
        if self.y > self.y_home:
            self.y = self.y - self.dy

    def actionGoWork(self):
        if self.x < self.x_work:
            self.x = self.x + self.dx
        if self.x > self.x_work:
            self.x = self.x - self.dx
        if self.y < self.y_work:
            self.y = self.y + self.dy
        if self.y > self.y_work:
            self.y = self.y - self.dy

 #   def actionWalkFree(self):




#def on_press(key):
 #   if key == keyboard.Key.esc:
  #      return False  # stop listener


def proximity(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))




##################### Variables ########################

### Groups ###

S = 1799  # Susceptible
E = 0  # Exposed
I = 1  # Infected
I_hosp = 0  # Infected hospitalized
I_icu = 0  # Infected ICU (ventilator)
R = 0  # Recovered
D = 0  # Deceased
Q = 0  # Quarantined
N = S + E + I + R  # Population

Sarray=[]
Earray=[]
Iarray=[]
Rarray=[]


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

b = 0.001  # infectious rate, controls the rate of spread which represents the probability of transmitting disease between a susceptible and an infectious individual.
q = 0.01  # b/g # contact ratio
g = 0.05  # b / q # recovery rate
e = 0.1  # incubation rate is the rate of latent individuals becoming infectious (average duration of incubation is 1/σ)


## Sim Time ##

T = 0  # Time horizon
timepassed=[]

### Constraints ###

I_hosp_max = N * 0.02
I_icu_max = N * 0.01

timepassed.append(T)
Sarray.append(S)
Earray.append(E)
Iarray.append(I)
Rarray.append(R)

##################### Main Loop ########################

done = False
while not done:
    print("S: ", S, "E: ", E, "I: ", I, "R: ", R, "time: ", T)

    T = T + 1

    S1 = S
    E1 = E
    I1 = I
    R1 = R

    Sdot = - b * I * S
    Edot = b * I * S - e * E
    Idot = e * E - g * I
    Rdot = g * I

    S = S1 + Sdot
    E = E1 + Edot
    I = I1 + Idot
    R = R1 + Rdot

    if S < 0:
        S = 0
    if E > N:
        E = N
    if I > N:
        I = N
    if R > N:
        R = N

    timepassed.append(T)
    Sarray.append(S)
    Earray.append(E)
    Iarray.append(I)
    Rarray.append(R)


#    listener = keyboard.Listener(on_press=on_press)
#    listener.start()  # start to listen on a separate thread
#    listener.join()  # remove if main thread is polling self.keys

#    print("End loop ?")
#    end = input()
    if T == 150:
        done = True

plt.plot(timepassed,Sarray,'g',timepassed,Earray,'y',timepassed,Iarray,'r',timepassed,Rarray,'b')
plt.show()

