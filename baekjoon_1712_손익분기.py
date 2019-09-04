# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:00:48 2019

@author: Kim Chanwoo
"""

A, B, C = map(int, input().split()) #map을 이용하여 인풋값을 정수로 변환 


if B >= C: #인건비가 판매가보다 클 경우 팔 수록 적자가 난다.
    print(-1)
    
else: print(A // (C - B) + 1) # 판매가에서 인건비 뺀 값과 A를 나누고 1을 더하면 손익분기점이 나온다.

