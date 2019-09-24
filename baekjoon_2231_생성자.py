# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:48:34 2019

@author: Kim Chanwoo
"""

# 입력은 출력의 분해합, 브루드 포스

a = int(input())
checker = 0 # 판별기?

for i in range(1, a+1): #자연수 1부터 입력값까지
    n = list(map(int, str(i))) # 자연수의 각 자릿수를 쪼개줌
    sum_num = i + sum(n) # 자연수와 그것을 이루는 자릿수들의 합
    if sum_num == a: #i 중에 생성자가 존재 할 경우
        checker = i #판별기는 생성자가 된다.
        break
print(checker)