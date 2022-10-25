#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:35:15 2022

@author: yoshida

fitting test of Maclaurin
checking residual
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# - - - - - - - Maclaurin - - - - - - - - - 
fnorm = np.linspace(1e-4,0.999,100)
elip = np.sqrt(1-(1-fnorm)**2)
W2maclaurin = []
for e in elip:
    if e>1e-6:
        W2maclaurin.append( 1.5/np.sqrt(1-e**2)\
    *(np.sqrt(1-e**2)*(3-2*e**2)*np.arcsin(e)/e**3\
      -3*(1-e**2)/e**2) )
    else:
        W2maclaurin.append(1.5*(4*e**2/15+4*e**4/105))
# - - - - - - - - - - - - - - - -

ow2f = np.array(W2maclaurin)/fnorm

fobl = np.linspace(1e-4,0.999,100)

def fnc(x, a0, a1, a2, b1, b2):
    return (a0+a1*x+a2*x**2)/(1+b1*x+b2*x**2)

popt, pcov = curve_fit(fnc,fnorm,ow2f)
a0 = popt[0]
a1 = popt[1]
a2 = popt[2]
b1 = popt[3]
b2 = popt[4]
fitfunction1 = fnc(fobl, a0, a1, a2, b1, b2)
residual1 = (fitfunction1-ow2f)/(fitfunction1+ow2f)*2

plt.plot(fobl, residual1 * 100)
plt.xlabel(r'$f_{\rm obl}$', fontsize=14)
plt.ylabel('residual (%)', fontsize=14)
plt.grid()
