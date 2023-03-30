n = int(input())

buildings = list(map(int, input().split()))

# 빌딩 간 기울기
def get_gradient(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

ans = 0
# 왼쪽 건물과 비교하여 기울기가 left_max_grad보다 낮은 건물을 볼 수 있음
# 오른쪽 건물과 비교하여 기울기가 right_max_grad보다 높은 건물을 볼 수 있음
for i in range(len(buildings)):
    cur_height = buildings[i]
    
    # 자기 자신을 제외하고 주변 볼 수 있는 건물 개수
    cnt = 0
    
    left_min_grad = float('inf')
    right_max_grad = -float('inf')
    for j in range(i-1, -1, -1):
        left_height = buildings[j]
        left_grad = get_gradient(i+1, cur_height, j+1, left_height)
        
        if left_grad < left_min_grad:
            left_min_grad = left_grad
            cnt += 1
            
    for k in range(i+1, n):
        right_height = buildings[k]
        right_grad = get_gradient(i+1, cur_height, k+1, right_height)
        
        if right_grad > right_max_grad:
            right_max_grad = right_grad
            cnt += 1
            
    ans = max(ans, cnt)
    
print(ans)
        