# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:50:43 2019

@author: Kim Chanwoo
"""

a = int(input())
b = map(int, input().split())

num_list = []

for i in b:
    num_list.append(i)

print(min(num_list), max(num_list))
