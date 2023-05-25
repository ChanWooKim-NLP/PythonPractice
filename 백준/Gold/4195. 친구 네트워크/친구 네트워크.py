import sys
from collections import defaultdict

input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    
    if px != py:
        parents[py] = px
        connected[px] += connected[py]
 
t = int(input())

for _ in range(t):
        
    f = int(input())
    
    parents = defaultdict(str)
    connected = defaultdict(int)
    
    name_idx = 1
    for _ in range(f):
        f1, f2 = input().split()
        
        if not parents[f1]:
            parents[f1] = f1
            connected[f1] = 1
            
        if not parents[f2]:
            parents[f2] = f2
            connected[f2] = 1
            
        union(f1, f2)
        
        root = find(f1)
        print(connected[root])