# -*- coding: utf-8 -*-
"""
Created on Mon Feb 4 10:37:46 2019

@author: sagar
"""
"""
DFT calculation for a discrete time signal for conversion to frequency domain
X(ejω)=∑n=−∞+∞x(n)e^−jnω is the standard formulae for calculating the DFT which
can be divided into Sine and Cosine components for better supervision
"""

#Import Math functions
import math
pie = math.pi
cosine = math.cos
sine = math.sin

#Define Power term to be used in the sequence
def powerterm(k):
    return complex(cosine(k),sine(k))
#Define a power function that returns true if the 
def powerfunction(n):
    return False if n == 0 else (n == 1 or powerfunction(n >> 1))

#Define a DFT function that returns a frequency domain signal of a time domain signal
#n is the number of samples in the input signal
#each term with k subscript is an integral term for summation

def DFT(input_time_signal):
    n = len(input_time_signal)
    return [sum((input_time_signal[k] * powerterm(-2 * pie * i * k / n) for k in range(n)))
            for i in range(n)]
#Define a function IDFT to convert incoming frequency domain signals to time domain
#Function returns the sum of each iterable in the summation series
def IDFT(input_frequency_signal):
    n = len(input_frequency_signal)
    return [sum((input_frequency_signal[k] * powerterm(2 * pie * i * k / n) for k in range(n))) // n
            for i in range(n)]

#Main/driver function
if __name__ == "__main__":
    wave = list(input("enter a digitized wave"))
    print" "
    frequency = DFT(wave)
    time = IDFT(frequency)
    print" "
    print("time to frequency domain conversion")    
    print(frequency)
    print" "
    print "frequency to time domain conversion"
    print([x.real for x in time])
    print" "
pass