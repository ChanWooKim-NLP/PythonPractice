import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(1, n+1):
    x, y = input().split()
    x, y = float(x), float(y)
    arr.append((i, x, y))

# 두 점 사이의 거리
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

# 모든 별에 대해 별 번호와 두 별 사이의 거리를 배열로 구축
graph = []
for i in range(n-1):
    for j in range(i+1, n):
        first_star = arr[i]
        second_star = arr[j]
        
        idx_1, idx_2 = first_star[0], second_star[0]
        
        x1, y1 = first_star[1], first_star[2]
        x2, y2 = second_star[1], second_star[2]
        
        dist = calculate_distance(x1, y1, x2, y2)
        graph.append((idx_1, idx_2, dist))
        
graph.sort(key=lambda x: x[2])

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    
    return find(parent[x])

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    
    if parent_a > parent_b:
        parent[parent_a] = parent_b
        
    else:
        parent[parent_b] = parent_a
        
    return

ans = 0
for edge in graph:
    a, b, dist = edge
    
    if find(a) != find(b):
        union(a, b)
        ans += dist
        
ans = round(ans, 2)
print(ans)