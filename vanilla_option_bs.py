# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:02:12 2019

@author: markus
"""

import numpy as np
import scipy.stats as ss

def black_Scholes(type, St, K, sigma, delta_T, r):
    
    d1 = 1 / (sigma * np.sqrt(delta_T)) * (np.log(St/K) + (r + sigma**2/2) * delta_T)
    d2 = d1 - sigma * np.sqrt(delta_T)
    
    if type == "Call":
        price = ss.norm.cdf(d1) * St - ss.norm.cdf(d2) * K * np.exp(-r * delta_T)
    elif type == "Put":
        price = ss.norm.cdf(-d2) * K * np.exp(-r * delta_T) - ss.norm.cdf(-d1) * St


    return price


type = "Call"
St = 100
K = 99
sigma = 0.3
delta_T = 1
r = 0.01

price = black_Scholes(type, St, K, sigma, delta_T, r)
print(price)
