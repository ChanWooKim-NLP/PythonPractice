# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:21:04 2019

@author: Kim Chanwoo
"""

a = int(input())
counts = a
account = []


while counts != 0:
    b = int(input())
    counts -= 1
    if b == 0: #입력값이 0일 때 스택의 마지막 입력값을 지워줌
        del account[-1]
    else: account.append(b) #0이 아닐 시 추가
    
print(sum(account)) #나머지값을 더해줌
    
    