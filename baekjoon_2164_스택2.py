# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:00:54 2019

@author: Kim Chanwoo
"""

a = int(input())
card = [i+1 for i in range(a)]


while True:
    if a == 1: break
    else:
        card.pop(0)
        card.append(card.pop(0))
        if len(card) == 1:
            break
        
print(card[0])