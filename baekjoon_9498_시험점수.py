# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:34:33 2019

@author: Kim Chanwoo
"""
#백준 9498번
#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
#나머지 점수는 F를 출력하는 프로그램을 작성하시오.

Score = int(input())

if 90 <= Score <= 100:
    print('A')
elif 80 <= Score < 90:
    print('B')    
elif 70 <= Score < 80:
    print('C')
elif 60 <= Score < 70:'
    print('D')
else: print('F')    