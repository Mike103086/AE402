# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:29:26 2020

@author: user
"""

    
import random 
n=0
n=random.randint(1,20)
c=1

for i in range(5):
    ans=int(input("請輸入答案:"))
    
    if ans == n :
        print("Good")
    if ans>n:
        print("Too Big")
    if ans<n:
        print("Too small")
 
    
