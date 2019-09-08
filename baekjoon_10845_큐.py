# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:51:57 2019

@author: Kim Chanwoo
"""

#큐 구현, 큐는 first in first out의 구조를 지닌다.

from sys import stdin #시간 초과 방지

a = int(input())
counts = a
queue = []

while counts != 0:
    b = stdin.readline().split()
    counts -= 1
    
    if b[0] == 'push':
        queue.append(b[1])
    elif b[0] == 'pop': #스택과 반대로 먼저 들어간 것이 먼저 나와야 함(append는 나중에 입력된 값이 리스트 뒤로 추가)
        if len(queue) >= 1:
            print(queue[0])
            del queue[0]
        else: print(-1)
    elif b[0] == 'size':
        print(len(queue))
    elif b[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else: print(0)
    elif b[0] == 'front': 
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif b[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else: print(queue[-1])