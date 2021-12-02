# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:27:50 2021

@author: merel
"""
import math
import numpy
import Point
from Shape import Shape

class Circle(Shape):
    def __init__(self, centerPoint, radius):
        self.centerPoint=centerPoint
        self.radius=radius
        
    def getters(self):
        return self.centerPoint, self.radius
    
    def setters(self, newcenter, newradius):
        self.centerPoint=newcenter
        self.radius=newradius
        
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return math.pi*2*self.radius
    
    def containsPoint(self, x0, y0):
        d = numpy.sqrt((self.centerPoint.getX()-x0)**2 + (self.centerPoint.getY()-y0)**2)
        if d < self.radius:
            return True
        else:
            return False
    
    def toString(self):
        return (f"The center point of the cirlce is ({self.centerPoint.getX()}, {self.centerPoint.getY()}) and the radius is {self.radius}")
