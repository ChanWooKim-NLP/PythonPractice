from collections import defaultdict

def find_parent(x, parent):
    if parent[x] == x:
        return parent[x]
    
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    parent_x = find_parent(x, parent)
    parent_y = find_parent(y, parent)

    if parent_x > parent_y:
        parent[parent_x] = parent_y
    
    else:
        parent[parent_y] = parent_x
    
def solution(n, costs):    
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])
    total_cost = 0
               
    for x, y, cost in costs:
        if find_parent(x, parent) != find_parent(y, parent):
            union(x, y, parent)
            total_cost += cost
        
    return total_cost