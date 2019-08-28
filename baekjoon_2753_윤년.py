# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:58:17 2019

@author: Kim Chanwoo
"""

x = int(input())

if ((x % 4 == 0) & (x % 100 != 0 or x % 400 == 0)) == True:
    print(1)
    
#비트 연산자를 이용해서 참/거짓 판별, 참이면 1 거짓이면 0

else: print(0)
    
    