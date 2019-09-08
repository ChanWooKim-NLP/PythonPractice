# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:54:34 2019

@author: Kim Chanwoo
"""

"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

#스택은 first in, last out의 구조를 지닌다.

from sys import stdin #시간 초과 방지

a = int(input())
counts = a

stack = [] #빈 리스트로 스택 구현

while counts != 0:
    cmd = stdin.readline().split() #모듈 이용
    counts -= 1
    if cmd[0] == 'push':
        stack.append(cmd[1]) #cmd를 띄어쓰기로 나누어서 index가 1인 부분을 스택에 추가
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack[-1])  #pop으로 하면 런타임 오류 나길래 출력하고 삭제하는 것으로 pop 구현
            del stack[-1]
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)    
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else: print(stack[-1]) 