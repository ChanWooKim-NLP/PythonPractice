N, K = map(int, input().split())
coins = [] # 동전을 담아 둘 리스트
count = 0 # 횟수

for i in range(N): 
    coins.append(int(input()))
 
for k in range(1, N+1):
    coin = coins[-k] # 거꾸로 순차, 동전을 내림차순으로 계산
    if K >= coin: # 총합이 지금 돌고 있는 인덱스의 가치보다 클 경우
        num = K // coin # 횟수 = 합계를 가장 큰 동전의 가치로 나눈 값
        count += num # 횟수들을 추가
        K -= coin*num # 전체 합계는 동전 가치를 뺀 횟수만큼 빠짐
        
print(count) # 문제의 목적은 최소 횟수만 출력
