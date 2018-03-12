# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 18:44:29 2018

@author: sage
"""

import numpy
import random
import math
from NN import *
    
class GA(object):
    def __init__(self, gen_number = 100, mutation_rate = .1, pop_number = 10):
        
        self.gen_number = gen_number
        self.mutation_rate = mutation_rate
        self.fitness_function = 0
        self.crossover_rate = .5
        
        self.pop_number = pop_number
        
        self.pop = []
        
        self.genCount = 0
    def defineFitnessFunction(self,F):
        self.fitness_function = F
        
    def populate(self):
        
        for x in range(self.pop_number):
            self.pop.append([NN(9,25,init=True).encodeNN(),0])
        
    def crossover(self):
        pass
    
    def mutation(self):
        pass
    
    def selection(self, k, khat):
        
        self.pop = sorted(self.pop, key=lambda x : x[1], reverse=True)
        selection_buffer = []
        
        for x in self.pop:
            
            looping = True
            
            while looping == True:
                temp_buffer = []
                best_sel = 0
                
                for y in range(k):
                    temp_buffer.append(random.choice(self.pop))
                
                for z in range(len(temp_buffer)-1):
                    
                    if z == 0:
                        best_sel = temp_buffer[0]
                    
                    else: 
                        if temp_buffer[z][1] > best_sel[1]:
                            best_sel = temp_buffer[z]
                
                if best_sel[1] != x[1]:
                    looping = False
                    selection_buffer.append((x,best_sel))
                    
        return selection_buffer
            
    def fitness(self, args):
        return self.fitness_function(args)
        
    def exportNN(self):
        return self.pop
    
    def evaluate(self):
        
        for x in self.pop:
            temp = getNNFromCode(x[0])    
            x[1] = self.fitness(temp)
    
    
        
        