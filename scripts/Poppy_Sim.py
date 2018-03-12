# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 07:39:05 2018

@author: sage
"""
from NN import *
import pypot.vrep as vrep
from pypot.vrep import from_vrep
from pypot.vrep.io import VrepIO
from pypot.creatures import PoppyHumanoid
from time import time

class PoppySim(object):
    
    def __init__(self):
        
        vrep.close_all_connections()
        
        self.poppy = PoppyHumanoid(simulator='vrep')
        
        self.waitTime()
        
        #self.vrep_io = VrepIO(vrep_port=port, start=True)
        
        #self.vrep_io.load_scene("thing.ttt")
        
        #self.vrep_io.start_simulation()
        
        self.poppy_head_pos = []
        
        self.next_update = .2
        self.last_update = time()
        #self.motor_names_file = open(motorfile, 'r')
        
        #self.motor_names = []
    def waitTime(self):
        
        t0 = time()
        while time()-t0 <= .1:
            pass
        
    def getOrientation(self):
        
        #self.poppy_head_pos = self.vrep_io.get_object_orientation("head_visual")
        
        self.poppy_head_pos = self.poppy.get_object_orientation("head_visual")
        
        self.waitTime()
        
        self.poppy_Lthigh_orientation = self.poppy.get_object_orientation("l_thigh_visual")
        
        self.waitTime()
        
        self.poppy_Rthigh_orientation = self.poppy.get_object_orientation("r_thigh_visual")
        
        self.waitTime()
        
        concant_list = self.poppy_head_pos+ self.poppy_Lthigh_orientation + self.poppy_Rthigh_orientation
        
        return concant_list
    
    #def populateMotorNames(self):
        
        #for line in self.motor_names_file:
            #self.motor_names.append(line)
        #pass
            
    def nnOut(self,nn):
        
        if time() - self.last_update >= self.next_update:
            
            o = self.getOrientation()
            
            for x in o:
                x /= 360    
            
            o = nn.forward((numpy.asarray(o)).reshape((1,9)))
    
            ol = []
           
            for x in numpy.nditer(o):
                ol.append(float(x))
            
            for x,y in zip(ol, self.poppy.motors):
                y.goal_position = float(x*360)
                
                if y.goal_position >= 360:
                    print("goal position out of range!")
                    
        #for x,y in zip(ol, self.motor_names):
            #self.vrep_io.set_motor_position(y,x)  
            
        
    def fitness(self):
        
        f = -self.poppy.get_object_position("pelvis_visual")[1]
            
        self.t0 = time()
        
        self.poppy.reset_simulation()
        
        return f
    
    def runSim(self,nn):
        self.t0 = time()
        self.poppy.start_simulation()
        
        while (time()-self.t0) <= 8.0:
            self.nnOut(nn)
        
        return self.fitness()
        
if __name__ == "__main__":
    pass
    
"""     
    nn = NN(3,25,5)
    foo = numpy.random.random((1,25))
    bar = []
    for x in numpy.nditer(foo):
        bar.append(float(x)) 
"""