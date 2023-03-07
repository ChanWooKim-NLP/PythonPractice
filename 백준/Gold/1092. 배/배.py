n = int(input())
crain = list(map(int, input().split()))

m = int(input())
box = list(map(int, input().split()))

# 무거운 순 정렬
box.sort(reverse=True)
crain.sort(reverse=True)

answer = 0
# 옮길 상자가 존재하면 이동 시도
while box:
    # 가장 무거운 크레인으로도 옮길 수 없는 박스면 반복문 해제
    if box[0] > crain[0]:
        break
    
    # 크레인으로 옮길 수 있는 짐 탐색
    # 옮길 수 있는 짐을 만날 때 까지 탐색
    # 예) 크레인이 1 2 3 4, 박스가 1 1 2 2 3 3 4 4일 때
    # 4 3 2 1을 집을 때 까지 탐색
    for c in crain:
        for b in box:
            if b <= c:
                # 해당 크레인은 짐을 옮겼으므로 break
                # 해당 짐을 제거
                box.remove(b) 
                break
        
    answer += 1

if box:
    print(-1)

else:
    print(answer)