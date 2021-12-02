# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:01:38 2021

@author: merel
"""

class Shape:
    def __init__(self, strokeWidth, strokeColor, fillColor):
        self.strokeWidth=strokeWidth
        self.strokeColor=strokeColor
        self.fillColor=fillColor
        
    def getStrokewidth(self):
        return self.strokeWidth
    
    def getStrokeColor(self):
        return self.strokeColor
    
    def getFillColor(self):
        return self.fillColor
    
    def setWidth(self, newwidth):
        self.strokeWidth=newwidth
        
    def setStrokecol(self, newstrokecol):
        self.strokeColor=newstrokecol
        
    def setFillcol(self, newfilcol):
        self.fillColor=newfilcol