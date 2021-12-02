# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 13:10:58 2021

@author: merel
"""

import numpy
from Shape import Shape

class Point(Shape):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def toString(self):
        return (f"Point ({self.x}, {self.y})")
        
    def distance(self, x0, y0):
        dist = numpy.sqrt((self.x-x0)**2 + (self.y-y0)**2)
        return dist
    
    def setPosition(self, newx, newy):
        self.x=newx
        self.y=newy
        
    def setX(self, newx):
        self.x=newx
        
    def setY(self, newy):
        self.y=newy
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y