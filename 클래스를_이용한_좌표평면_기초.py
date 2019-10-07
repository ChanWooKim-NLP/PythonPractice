# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:48:34 2019

@author: Kim Chanwoo
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self):
        return (self.x, self.y)
        
    def equal(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        if (self.x1, self.y1) == (self.x, self.y):
            return 1
        else: return 0
        
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_from_point(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        return ((self.x-self.x1)**2 + (self.y-self.y1)**2)**0.5
