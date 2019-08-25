# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:02:45 2019

@author: Kim Chanwoo
"""
n = int(input())
i = 0 #i의 값으로 먼저 0을 지정
while True: #무한 루프
    i += 1 #i의 값 count
    if i > n: break #i의 값이 n을 넘으면 브레이크
    a = "*"*(n-(i-1))
    print(a.rjust(n))