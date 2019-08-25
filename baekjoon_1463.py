# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:34:58 2019

@author: Kim Chanwoo
"""

a = int(input())
Try = 0

while True:
    if (a % 3) == 0:
        a = a // 3
        Try += 1
    if (a % 2) == 0:
        a = a // 2
        Try += 1
    if (a % 3 or 2) == 1:
        a -= 1
        Try += 1
    if a == 1:
        break
print(Try)