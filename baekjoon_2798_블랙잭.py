# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:03:52 2019

@author: Kim Chanwoo
"""

"""
브루트 포스 알고리즘 - 가능한 모든 조합을 직접 해보는 방식
이러한 방식은 가장 단순하지만 비효율적인 면에서 단점을 가진다.
만들기 쉬우며 다른 알고리즘의 출발점
"""

a, b = map(int, input().split())

card = list(map(int, input().split()))
answer = 0

for i in range(0, a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if (card[i]+card[j]+card[k]) <= b and b-(card[i]+card[j]+card[k]) < b-answer:
                answer = card[i]+card[j]+card[k]
                
print(answer)
