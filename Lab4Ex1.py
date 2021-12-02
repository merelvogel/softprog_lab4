# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:38:40 2021

@author: merel
"""

import unittest
import Point
import Rectangle
import Circle
import math

class TestPoint(unittest.TestCase):

    def test_get_X(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(15, test_point.getX())

    def test_get_Y(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(35, test_point.getY())
        
    def test_set_X(self):
        test_point = Point.Point(15,35)
        test_point.setX(10)
        self.assertEqual(10, test_point.x)
        
    def test_set_Y(self):
        test_point = Point.Point(15,35)
        test_point.setY(10)
        self.assertEqual(10, test_point.y)
        
    def test_setPosition(self):
        test_point = Point.Point(15,35)
        test_point.setPosition(10, 20)
        self.assertEqual(10, test_point.x)
        self.assertEqual(20, test_point.y)
        
    def test_distance(self):
        test_point = Point.Point(15,35)
        x0 = 16
        y0 = 35
        self.assertEqual(1, test_point.distance(x0, y0))
        
    def test_toString(self):
        test_point = Point.Point(15,35)
        self.assertEqual("Point (15, 35)", test_point.toString())
        
    def test_getstrokewidth(self):
        test_point = Point.Point(15,35)
        test_point.strokeWidth=4
        self.assertEqual(4, test_point.getStrokewidth())
        
    def test_setstrokewidth(self):
        test_point = Point.Point(15,35)
        test_point.setWidth(4)
        self.assertEqual(4, test_point.getStrokewidth())
        
    def test_getstrokecolor(self):
        test_point = Point.Point(15,35)
        test_point.strokeColor = "red"
        self.assertEqual("red", test_point.getStrokeColor())
        
    def test_setstrokecolor(self):
        test_point = Point.Point(15,35)
        test_point.setStrokecol("red")
        self.assertEqual("red", test_point.getStrokeColor())
        
    def test_getfilcol(self):
        test_point = Point.Point(15,35)
        test_point.fillColor = "red"
        self.assertEqual("red", test_point.getFillColor())
        
    def test_setfilcol(self):
        test_point = Point.Point(15,35)  
        test_point.setFillcol("red")
        self.assertEqual("red", test_point.getFillColor())

class TestRectangle(unittest.TestCase):
    
    def test_getters(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        results = test_rectangle.getters()
        self.assertEqual(results, (test_topleftpoint, 3, 5))

    def test_setters(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        new_topleftpoint = Point.Point(10,20)
        test_rectangle.setters(new_topleftpoint, 4, 6)
        self.assertEqual((new_topleftpoint, 4, 6), (test_rectangle.TopLeftPoint, test_rectangle.width, test_rectangle.height))
        
    def test_area(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        self.assertEqual(15, test_rectangle.area())
        
    def test_perimeter(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        self.assertEqual(16, test_rectangle.perimeter())
        
    def test_contains(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_pointinside = Point.Point(16,33)
        self.assertEqual(True, test_rectangle.contains(test_pointinside))
    
    def test_centroid(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle = Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_centroid = Point.Point(16.5, 32.5)
        results = test_rectangle.Centroid()
        self.assertEqual((results.getX(),results.getY()), (test_centroid.x, test_centroid.y))
        
    def test_toString(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle = Rectangle.Rectangle(test_topleftpoint, 3, 5)
        results = test_rectangle.toString()
        self.assertEqual("Rectangle: the top left point is (15,35), the width is 3 and the height is 5", results)
        
    def test_getstrokewidth(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.strokeWidth=4
        self.assertEqual(4, test_rectangle.getStrokewidth())
        
    def test_setstrokewidth(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.setWidth(4)
        self.assertEqual(4, test_rectangle.getStrokewidth())
        
    def test_getstrokecolor(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.strokeColor = "red"
        self.assertEqual("red", test_rectangle.getStrokeColor())
        
    def test_setstrokecolor(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.setStrokecol("red")
        self.assertEqual("red", test_rectangle.getStrokeColor())
        
    def test_getfilcol(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.fillColor = "red"
        self.assertEqual("red", test_rectangle.getFillColor())
        
    def test_setfilcol(self):
        test_topleftpoint = Point.Point(15,35)
        test_rectangle=Rectangle.Rectangle(test_topleftpoint, 3, 5)
        test_rectangle.setFillcol("red")
        self.assertEqual("red", test_rectangle.getFillColor())

class TestCircle(unittest.TestCase):
    
    def test_getters(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        results = test_circle.getters()
        self.assertEqual(results, (test_centerpoint, 3))
        
    def test_setters(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        new_centerpoint = Point.Point(10,20)
        test_circle.setters(new_centerpoint, 4)
        self.assertEqual((new_centerpoint, 4), (test_circle.centerPoint, test_circle.radius))
        
    def test_area(self):
        test_centerpoint = Point.Point(15,35)
        test_circle = Circle.Circle(test_centerpoint, 3)
        area = math.pi*3**2
        self.assertEqual(area, test_circle.area())
        
    def test_perimeter(self):
        test_centerpoint = Point.Point(15,35)
        test_circle = Circle.Circle(test_centerpoint, 3)
        perim = 2*math.pi*3
        self.assertEqual(perim, test_circle.perimeter())
        
    def test_contains(self):
        test_centerpoint = Point.Point(15,35)
        test_circle = Circle.Circle(test_centerpoint, 3)
        test_pointinside = Point.Point(15,36)
        self.assertEqual(True, test_circle.containsPoint(test_pointinside.getX(), test_pointinside.getY()))
    
    def test_toString(self):
        test_centerpoint = Point.Point(15,35)
        test_circle = Circle.Circle(test_centerpoint, 3)
        results = test_circle.toString()
        self.assertEqual("The center point of the cirlce is (15, 35) and the radius is 3", results)
        
    def test_getstrokewidth(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.strokeWidth=4
        self.assertEqual(4, test_circle.getStrokewidth())
        
    def test_setstrokewidth(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.setWidth(4)
        self.assertEqual(4, test_circle.getStrokewidth())
        
    def test_getstrokecolor(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.strokeColor = "red"
        self.assertEqual("red", test_circle.getStrokeColor())
        
    def test_setstrokecolor(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.setStrokecol("red")
        self.assertEqual("red", test_circle.getStrokeColor())
        
    def test_getfilcol(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.fillColor = "red"
        self.assertEqual("red", test_circle.getFillColor())
        
    def test_setfilcol(self):
        test_centerpoint = Point.Point(15,35)
        test_circle=Circle.Circle(test_centerpoint, 3)
        test_circle.setFillcol("red")
        self.assertEqual("red", test_circle.getFillColor())
    
if __name__ == '__main__': 
     unittest.main()