from itertools import permutations

def travel(k, order):
    i = 0
    cnt = 0
    while k > 0:
        if i == len(order):
            break
        
        if k >= order[i][0]:
            cnt += 1
            k -= order[i][1]
        
        i += 1
        
    return cnt


def solution(k, dungeons):
    total_dungeon_orders = list(permutations(dungeons, len(dungeons)))
    
    answer = 0
    for order in total_dungeon_orders:
        cnt = travel(k, order)
        answer = max(answer, cnt)
    
    return answer