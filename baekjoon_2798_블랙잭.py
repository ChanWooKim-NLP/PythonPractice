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
# a는 배열의 총 길이, b는 카드 3개의 총합에 가까워야 하는 수

card = list(map(int, input().split())) # 배열을 적으면 card 라는 리스트에 적용됨
answer = 0 # 가장 근접한 수를 구하기 위한 변수

for i in range(0, a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if (card[i]+card[j]+card[k]) <= b and b-(card[i]+card[j]+card[k]) < b-answer:
                answer = card[i]+card[j]+card[k]
                
   # 3중 반복문을 통해서 가장 근접한 수를 찾는 과정.
   # 만약 3개의 숫자가 b보다 작으면서'도' b랑 근접하면 answer에 대입
                
print(answer)
