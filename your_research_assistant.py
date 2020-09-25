#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 01:35:36 2020

@author: cinema
"""
import numpy as np
import scipy.stats as si

"""Question 2"""
def blackScholesMersonMethod(option_type, volatiility, risk_free_rate,time_to_expiry,strike_price,spot_price):
    T = time_to_expiry/365 #Time to maturity expressed in years.  
    S = spot_price #Spot price of underlying asset at time t.
    K = strike_price #Strike price for each share in our options contract.
    r = risk_free_rate #Risk free rate assumed to be a value between our T and t.
    D = volatiility #Volatility of returns of the underlying asset ,SD of datapoints in assets returns. 
    N = si.norm.cdf #Cumulative distribution function of a standard normal distribution with a mean = 0 and SD of 1. 
    deriv = (D**2)/2
    d1 =  (np.log(S/K) + ((r + deriv) * T)) / (D * np.sqrt(T))
    d2 = d1 - (D * np.sqrt(T))
    power_PV = -r*T
    PV = K*np.exp(power_PV)
    if (option_type == "call"):
        first_half_eqn = N(d1,0,1) * S #normal distribution * spot price. 
        second_half_eqn = N(d2,0,1) * PV #normal distribution wth d2 multiplied by PV.
        C = first_half_eqn - second_half_eqn #get final call value.
        print("derivative = ", deriv)
        print("d1 = ", d1, "d2 = ", d2)
        print("Standard normalized d1 = ", N(d1), "Standard normalized d1 = ", N(d2))
        #print(PV)
        #print("Time value = ", T)
        import scipy.stats as sc
        call = ((S * sc.norm.cdf(d1, 0,1)) - K * np.exp(power_PV) * sc.norm.cdf(d2,0,1)) 
        print("This is call:",call)
        return C
    elif(option_type == "put"):
        P = PV * N(-d2,0,1) - S * N(-d1,0,1)
        put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        print("This is put:",put)
        return P
    
 
"""Question 4"""   
def prothNumber(n,k): #For any 2 random positive integers n and k where k is odd, N is our proth number. 
    while(k % 2 != 0 and 2**n > k): #checks if k is odd and if 2^n is greater than k. 
        N = (k*2**n) + 1 #Get Proth Number.
        value_list = list(range(1,10)) #create list in the range of 1 - 10.
        print(N) #Print Proth number
        power = (N-1)/2 #get raised power after relevant computations.
        power_a = [a **power + 1 for a in value_list] #get all values of a raised to power. 
        prime_check = [x % N == 0 for x in power_a] #iterate through all values in range 1 - 10 and check if they are divisible by N(our proth number) without a remainder.
        if(any(prime_check) == True): #If any value in the range returns as true then N is a Proth Prime number.
            return N, "Is a Proth Prime Number."
        else :
            return N, "Is not a Proth Prime Number."
    return "Conditions for proth number generation not satisfied, check your parameters."
def prothPrime(N):
        a = list(range(0,10))#create list in the range of 1 - 10.
        power = (N-1)/2 #get power after relevant computations.
        #a = 5**power + 1#(N-1)/2) + 1
        power_a = [i **power + 1 for i in a]#get all values of a raised to power.
        prime_check = [x % N == 0 for x in power_a]#iterate through all values in range 1 - 10 and check if they are divisible by N(our proth number) without a remainder.
        if(any(prime_check) == True): #If any value in the range returns as true then N is a Proth Prime number.
            return N, "Is a Proth Prime Number."
        else :
            return N, "Is not a Proth Prime Number."


"""Question 5"""
def rN():
    values = list(range(0,10))
    y = [np.sqrt(((x+6)**2) + 25) + np.sqrt(((x - 6)**2) + 121) for x in values]
    return y
