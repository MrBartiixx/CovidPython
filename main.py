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

    def __init__(self, x, y, group, action, homeless, unemployed, x_home, y_home, x_work, y_work, house, work):
        self.x = x
        self.y = y
        self.group = group
        self.action = action
        self.homeless = homeless
        self.unemployed = unemployed
        self.x_home = x_home
        self.y_home = y_home
        self.x_work = x_work
        self.y_work = y_work
        self.house = house
        self.work = work

    def actionGoHome(self):
        # IF person not in home, at this function call, move person by 1 px towards home
        if self.x < self.house.x - self.house.dx or self.x > self.house.x + self.house.dx or self.y < self.house.y - self.house.dy or self.y > self.house.y + self.house.dy:
            if self.x < self.x_home:
                self.x = self.x + self.dx
            if self.x > self.x_home:
                self.x = self.x - self.dx
            if self.y < self.y_home:
                self.y = self.y + self.dy
            if self.y > self.y_home:
                self.y = self.y - self.dy
    
    def actionStayHome(self):
        # If person at home, stay at px or move with probability inside home
        if self.x >= self.house.x - self.house.dx or self.x <= self.house.x + self.house.dx or self.y >= self.house.y - self.house.dy or self.y <= self.house.y + self.house.dy:
            eps = random.Random()
            if eps > 0.6 and eps < 0.7:
                self.x = self.x + self.dx
                self.y = self.y + self.dy
            if eps > 0.7 and eps < 0.8:
                self.x = self.x - self.dx
                self.y = self.y - self.dy
            if eps > 0.8 and eps < 0.85:
                self.x =self.x - self.dx
            if eps > 0.85 and eps < 0.9:
                self.x =self.x + self.dx
            if eps > 0.9 and eps < 0.95:
                self.y =self.y - self.dy
            if eps > 0.95:
                self.y =self.y + self.dy      
            if self.x > self.house.x + self.house.dx:
                self.x = self.house.x + self.house.dx - 1
            if self.x > self.house.x - self.house.dx:
                self.x = self.house.x - self.house.dx + 1
            if self.y > self.house.y + self.house.dy:
                self.y = self.house.y + self.house.dy - 1
            if self.y > self.house.y - self.house.dy:
                self.y = self.house.y - self.house.dy + 1   
    
    
    def actionGoWork(self):
        # IF person not in work, at this function call, move person by 1 px towards work
        if self.x < self.work.x - self.work.dx or self.x > self.work.x + self.work.dx or self.y < self.work.y - self.work.dy or self.y > self.work.y + self.work.dy:
            if self.x < self.x_work:
                self.x = self.x + self.dx
            if self.x > self.x_work:
                self.x = self.x - self.dx
            if self.y < self.y_work:
                self.y = self.y + self.dy
            if self.y > self.y_work:
                self.y = self.y - self.dy

    def actionStayAtWork(self):
        # If person at work, stay at px or move with probability inside work
        if self.x >= self.work.x - self.work.dx or self.x <= self.work.x + self.work.dx or self.y >= self.work.y - self.work.dy or self.y <= self.work.y + self.work.dy:
            eps = random.Random()
            if eps > 0.6 and eps < 0.7:
                self.x = self.x + self.dx
                self.y = self.y + self.dy
            if eps > 0.7 and eps < 0.8:
                self.x = self.x - self.dx
                self.y = self.y - self.dy
            if eps > 0.8 and eps < 0.85:
                self.x =self.x - self.dx
            if eps > 0.85 and eps < 0.9:
                self.x =self.x + self.dx
            if eps > 0.9 and eps < 0.95:
                self.y =self.y - self.dy
            if eps > 0.95:
                self.y =self.y + self.dy            
            if self.x > self.work.x + self.work.dx:
                self.x = self.work.x + self.work.dx - 1
            if self.x > self.work.x - self.work.dx:
                self.x = self.work.x - self.work.dx + 1
            if self.y > self.work.y + self.work.dy:
                self.y = self.work.y + self.work.dy - 1
            if self.y > self.work.y - self.work.dy:
                self.y = self.work.y - self.work.dy + 1    

            
            
            

#    def actionWalkFree(self):


class House:
    def __init__(self, x, y, dx, dy, no_residents):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.no_residents = no_residents
        

class Workplace:
    def __init__(self, x, y, dx, dy, no_workers):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.no_workers = no_workers



#def on_press(key):
 #   if key == keyboard.Key.esc:
  #      return False  # stop listener


def contact(person1,person2):
    if person1.x == person2.x and person1.y == person2.y:
        return True
    return False




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
N: int = S + E + I + R  # Population

Sarray=[]
Earray=[]
Iarray=[]
Rarray=[]


### Agents ###

PPL = []  # [x,y,group,action]
ACT = np.array(['Home', 'Work', 'WalkFree', 'Movement'])
HOU=[]
WRP=[]

family_size = 3
homeless_rate = 0.0005
no_houses = int((N - N * homeless_rate)/family_size)
unemployment_rate = 0.12
no_workplaces = 50



### Environment ###

Length = 1000
Width = 1000

# each pixel corresponds to area 5x5 meters.


#for n in range(N):
#    PPL[n, 0] = random.uniform(0, Width)
#    PPL[n, 1] = random.uniform(0, Length)

### Parameters ###

contagion_distance = 1
contagion_probability = 0.9
incubation_time = 5
transmission_time = 8
recovering_time = 20
ICU_limit = N * 0.05




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

### Spawn houses ###
for f in range(no_houses):
    done1 = False
    while not done1:
        x = int(random.uniform(0, Length+1))
        y = int(random.uniform(0, Width+1))
        dx = int(random.uniform(1,3))
        dy = int(random.uniform(1,3))
        HOU.append(House(x, y, dx, dy, 0))
        done1 = True
        
### Spawn workplaces ###
for f in range(no_workplaces):
    done1 = False
    while not done1:
        x = int(random.uniform(0, Length+1))
        y = int(random.uniform(0, Width+1))
        dx = int(random.uniform(1,7))
        dy = int(random.uniform(1,7))
        WRP.append(Workplace(x, y, dx, dy, 0))
        done1 = True

### Spawn people ###

emptyWork = Workplace(0,0,0,0,0)
empytHouse = House(0, 0, 0, 0, 0)



for i in range(1):
    PPL.append(Human(1,1,0,0,1,1,-1,-1,-1,-1,empytHouse,emptyWork))

for i in range(N-2):
    PPL.append(Human(1,1,0,0,0,0,-1,-1,-1,-1,empytHouse,emptyWork))

for i in range(1):
    PPL.append(Human(1,1,2,0,0,0,-1,-1,-1,-1,empytHouse,emptyWork))

random.shuffle(HOU)
random.shuffle(PPL)
for house in HOU:
    ff = int(random.uniform(2,5))
    temp = 0
    for person in PPL:
        if person.homeless == 0:
            if person.x_home == -1:
                person.house = house
                person.x_home = house.x
                person.y_home = house.y
                person.x = house.x
                person.y = house.y
                house.no_residents = house.no_residents + 1 
                temp = temp + 1
                if temp == ff:
                    break

random.shuffle(WRP)
random.shuffle(PPL)
for workplace in WRP:
    ff = int(random.uniform(20, 61))
    temp = 0
    for person in PPL:
        if person.unemployed == 0:
            if person.x_work == -1:
                person.work = workplace
                person.x_work = workplace.x
                person.y_work = workplace.y
                workplace.no_workers = workplace.no_workers + 1 
                temp = temp + 1
                if temp == ff:
                    break

housesx = []
housesy = []
worksx = []
worksy = []
for house in HOU:
    housesx.append(house.x)
    housesy.append(house.y)
for work in WRP:
    worksx.append(work.x)
    worksy.append(work.y)
    
plt.plot(housesy, housesx, 'o', color='black')
plt.plot(worksy, worksx, 'o', color='green')
plt.show()

for person in PPL:
    if person.x_work > 1000 & person.x_work < 0 & person.y_work > 1000 & person.y_work < 0 & person.x_home > 1000 & person.x_home < 0 & person.y_home > 1000 & person.y_home < 0:
        print(person)


done = False
while not done:
    #print("S: ", S, "E: ", E, "I: ", I, "R: ", R, "time: ", T)
    
    for hour in range(24):
        if hour > -1 & hour < 8:
            for timestamp in range(600):
                for person in PPL:
                     if person.unemployed == 0:
                         person.actionGoWork()
                         person.actionStayAtWork()
                         for person2 in PPL:
                             if contact(person,person2):
                                 if person.group == 2:
                                     person2.group = 1
                                 if person2.group == 2:
                                     person.group = 1
        if hour > 7 & hour < :

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

#plt.plot(timepassed,Sarray,'g',timepassed,Earray,'y',timepassed,Iarray,'r',timepassed,Rarray,'b')
#plt.show()

