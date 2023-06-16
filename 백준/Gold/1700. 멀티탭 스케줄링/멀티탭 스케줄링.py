from collections import defaultdict

n, k = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

multitab = []
for idx in range(k):
    if arr[idx] in multitab:
        continue
    
    if len(multitab) < n:
        multitab.append(arr[idx])
        continue
    
    # 미래에 사용할 전자기기
    future_use = arr[idx:]
    
    # 현재 플러그에 있고 앞으로 사용할 기구 중 가장 나중에 사용될 기구를 구함
    future_tool = 0
    future_use_idx = 0
    for tool in multitab:
        # 멀티탭에 꽂힌 기구 중 앞으로 사용되지 않는다면 그 기구를 교체
        if tool not in future_use:
            future_tool = tool
            break
        
        # 현재 기구가 다시 사용되는 미래 시점
        temp_future_use_idx = future_use.index(tool)
        
        # 그 시점이 현재 기록한 가장 먼 시점보다 크다면 그것을 기록
        if temp_future_use_idx > future_use_idx:
            future_use_idx = temp_future_use_idx
            future_tool = tool
    
    # 멀티탭에서 교체 진행
    change_idx = multitab.index(future_tool)
    multitab[change_idx] = arr[idx]
    answer += 1
    
print(answer)