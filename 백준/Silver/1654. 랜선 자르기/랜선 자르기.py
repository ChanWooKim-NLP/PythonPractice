k, n = map(int, input().split())

lan_cable = []

for _ in range(k):
    l = int(input())
    lan_cable.append(l)

min_length, max_length = 1, max(lan_cable)

def cut_cable(length):
    cnt = 0
    
    for c in lan_cable:
        cnt += c // length
    
    return cnt


# 길이를 반으로 줄여가면서 랜선 잘라보기
while min_length <= max_length:
    mid = (min_length + max_length) // 2
    cable_cnt = cut_cable(mid)
    
    # 할당량을 채울 수 없으면 더 작게 자름
    if cable_cnt < n:
        max_length = mid - 1
        
    elif cable_cnt >= n:
        min_length = mid + 1
    

print(min_length-1)
