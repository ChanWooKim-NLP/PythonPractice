# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:59:52 2019

@author: Kim Chanwoo
"""

a = int(input())
b = int(input())    

n = len(str(b)) #b의 길이를 나타내기 위해 문자열 처리하고 자릿수를 뽑아냄
base = 0 #자릿수 추가를 위한 base

result = 0 #결과값

List = [] #b의 숫자들을 모아두기 위한 리스트. 이 값을 pop메서드를 이용하여 거꾸로 뽑아낸다.
for i in str(b): #b의 값을 백의 자리부터 출력
    List.append(int(i)) #문자열이었던 i를 정수 형태로 출력
    
while base != n : #while문과 for문을 이용, for문을 한단계 한단계 출력하고 계산
    for multiplier in List: #리스트 안의 요소를 multiplier로 지정
        multiplier = List.pop() #리스트 안의 값을 '거꾸로' 출력 (1의 자리부터 곱셈을 구현)
        print(a*multiplier)         
        result += a*(multiplier*10**base) #result 변수 안에 곱한 값을 더함(시그마)
        base += 1 #자릿수를 늘림
    

print(result)
