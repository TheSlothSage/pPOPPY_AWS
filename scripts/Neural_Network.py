# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 22:56:07 2018

@author: sage
"""

import numpy
import matplotlib.pyplot as plt
import scipy
import random
import struct

class NN(object):
    def __init__(self, i, j, nodenumber = random.randint(1, 5)+2, init = True):
        
        """
        i -> input dimention in the horizontal
        j -> output direction in the horizontal
        hi ->ith hidden layer length
        
        100 nodes max for hidden layer
        
        """
        self.init = init
        
        #Arbitrary Max Size Limit used for testing. Set to hnumber
        self.nodenumber = nodenumber
        
        self.hnumber = 100
                
        self.biases=[]
        
        self.weights=[]
        
        self.activation = []
        
        self.connections = []
        
        for x in range(self.nodenumber):
            self.activation.append(0)
        
        self.i = i
        self.j = j
        
        if self.init == True:
            self.randomWeights()
        self.init == False

    def sigmoid(self, x):
        return 1/(1+numpy.exp(-x))
    
    def randomWeights(self):
        """For initializing a population only"""

        for x in range(self.nodenumber):            
            #thing1=numpy.random.randint(-5,5,size=(100,j))
            if x == self.nodenumber-1:
                self.biases.append([numpy.random.random((self.j,1)),numpy.random.random((self.hnumber,self.j))])
                self.weights.append(numpy.random.random((self.hnumber, self.j)))
            elif x==0:
                self.biases.append([numpy.random.random((1,self.i)),numpy.random.random((self.i,self.hnumber))])
                self.weights.append(numpy.random.random((self.i, self.hnumber)))
            else:
                self.biases.append([numpy.random.random((1, self.hnumber)),numpy.random.random((self.hnumber,self.hnumber))])
                self.weights.append(numpy.random.random((self.hnumber,self.hnumber)))
                self.connections.append(numpy.random.randint(0,2,(1,self.hnumber)))
                
    
    def encodeNN(self):
        return (self.weights, self.biases, self.nodenumber, self.connections, self.i, self.j)
        
    def forward(self, X):
        try:
            z1 = numpy.dot(X, self.weights[0])
            b1 = numpy.dot(self.biases[0][0], self.biases[0][1])
            self.activation[0] = self.sigmoid(z1+b1)
            
            for x in range(self.nodenumber-2):
                self.activation[x+1] = self.sigmoid(numpy.dot(self.activation[x],self.weights[x+1])
                                            + numpy.dot(self.biases[x+1][0],self.biases[x+1][1]))*self.connections[x]
                
            zi = numpy.dot(self.activation[len(self.activation)-2],self.weights[-1])
            bi = numpy.dot(self.biases[-1][1],self.biases[-1][0])
            self.activation[-1] = self.sigmoid(zi+bi)
            
            self.yhat = self.activation[-1]
            
        except ValueError():
            print X
        
        return self.yhat
    
def getNNFromCode(nn_encoded):
    nn = NN(nn_encoded[4],nn_encoded[5],nn_encoded[2], False)
    
    nn.biases = nn_encoded[1]
    nn.weights = nn_encoded[0]
    nn.connections = nn_encoded[3]
    
    return nn
        
            



    
        

        
    
        
        
        
        