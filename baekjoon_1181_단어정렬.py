a = int(input())

voca_list = [] # 단어를 저장하는 리스트

for i in range(a):
    voca = str(input())
    voca_list.append(voca) # 입력값 리스트 저장
    
voca_list1 = list(set(voca_list)) # 세트화 시키면 중복 제거

voca_list2 = [] # 정렬하기 전 리스트

for j in voca_list1:
    voca_list2.append((len(j), j)) # 우선순위는 길이, 그 다음 알파벳
    
voca_list2.sort() # 길이 순으로 정렬, 그 다음 j의 단어 순대로 정렬 (내장)

for k, t in voca_list2:
    print(t)
