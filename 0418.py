# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:30:55 2020

@author: user
"""

class Human():
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    def BMI(self):
        return self.width / ((self.height/100)**2)
    
    
    
a=Human("jojoron",50,145)
print(a.name,a.BMI)