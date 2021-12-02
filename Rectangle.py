# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:27:20 2021

@author: merel
"""

import Point 
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, TopLeftPoint, width, height):
        self.TopLeftPoint=TopLeftPoint
        self.width=width
        self.height=height
        
    def getters(self):
        return self.TopLeftPoint, self.width, self.height
    
    def setters(self, newtop, newwidth, newheight):
        self.TopLeftPoint=newtop
        self.width=newwidth
        self.height=newheight
        
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*self.width+2*self.height

    def contains(self, Point):
        xmin = self.TopLeftPoint.getX()
        xmax = self.TopLeftPoint.getX() + self.width
        x = Point.getX()
        ymin = self.TopLeftPoint.getY() - self.height
        ymax = self.TopLeftPoint.getY() 
        y = Point.getY()
        if xmin <= x <= xmax and ymin <= y <= ymax:
                return True
        else:
            return False
        
    def Centroid(self):
        xcentroid=self.TopLeftPoint.getX()+(1/2)*self.width
        ycentroid=self.TopLeftPoint.getY()-(1/2)*self.height
        centroid=Point.Point(float(xcentroid), float(ycentroid))
        return centroid
    
    def toString(self):
        return (f"Rectangle: the top left point is ({self.TopLeftPoint.getX()},{self.TopLeftPoint.getY()}), the width is {self.width} and the height is {self.height}")