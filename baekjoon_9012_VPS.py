# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:26:00 2019

@author: Kim Chanwoo
"""


a = int(input())


for t in range(a): #input의 횟수만큼 stack을 만들고 그 과정이 끝나면 초기화
    stack = [] #스택, (를 보관할 리스트
    PS = str(input())
    checker = 1 #참과 거짓 판별, 특정한 과정을 거치면 0으로 스위치하게 만듬
    
    for i in range(0, len(PS)): #리스트는 0부터 시작, PS의 길이까지
        if PS[i] == '(':
            stack.append(1) #'('이면 그대로(1 = true) 스택에 집어넣고
            
        elif PS[i] == ')': #')'이 등장하면, 앞에 (가 있을 시에만 스택에서 꺼냄(쌍이 맞는 것들만 빼내는 작업)
            if len(stack) == 0:
                checker = 0 #처음부터 등장하면 판별기가 0으로 스위치
                break
            else:
                stack.pop() 
                
                
    if len(stack) != 0: #()의 쌍을 판별하는 for문이 끝나고 스택의 길이 확인, 
        checker = 0 #스택의 길이가 0이 아니면 짝이 안맞는 ()가 있다는 의미, 0으로 바꿈
            
    if checker == 1: #판별기가 True, False일 때
        print('YES')
    else: print('NO')
            
                
    
    

        