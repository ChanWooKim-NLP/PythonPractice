n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

home_loc = []
chicken_loc = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home_loc.append((i, j))
            
        elif arr[i][j] == 2:
            chicken_loc.append((i, j))

visited = [0] * len(chicken_loc)

min_dist = float('inf')

# 유지할 수 있는 치킨집의 조합
chosen_chicken = []
def pick_chicken(cnt, idx, max_m):    
    global min_dist
    
    if cnt == max_m:
        result = calculate_chicken_dist(chosen_chicken, home_loc)
        min_dist = min(result, min_dist)
    
    for i in range(idx, len(chicken_loc)):
        if not visited[i]:
            visited[i] = 1
            chosen_chicken.append(chicken_loc[i])
            
            pick_chicken(cnt+1, i+1, max_m)
            
            chosen_chicken.pop()
            visited[i] = 0


def calculate_chicken_dist(c_list, h_list):
    chicken_dist = [float("inf")] * len(h_list) 
    
    for c in range(len(c_list)):
        for h in range(len(h_list)):
            # 치킨
            r1, c1 = c_list[c]
            # 집
            r2, c2 = h_list[h]
            
            dist = abs(r2-r1) + abs(c2-c1)
            chicken_dist[h] = min(chicken_dist[h], dist)
    
    return sum(chicken_dist)
            
for i in range(1, m+1):
    pick_chicken(0, 0, i)

print(min_dist)