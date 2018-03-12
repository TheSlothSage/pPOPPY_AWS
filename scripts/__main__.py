# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 03:46:05 2018

@author: sage
"""

from NN import *
from GA import *
from poppySim import *

if __name__ == "__main__":
    
    g = GA()
    g.populate()

    p = PoppySim()
    g.defineFitnessFunction(p.runSim)
    
    g.evaluate()
    v = g.selection(5,3)