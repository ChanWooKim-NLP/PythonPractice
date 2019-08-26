# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:59:52 2019

@author: Kim Chanwoo
"""
N, B = input().split()
B = int(B)

a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(N)
result = 0

while length != 0:
    for i in N:
      nums = a.index(i)
      result += nums * (B**(length - 1))
      length -= 1
print(result)  