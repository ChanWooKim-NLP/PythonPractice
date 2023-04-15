from collections import deque, defaultdict, Counter

def solution(topping):
    if len(topping) == 1:
        return 0
    
    answer = 0
    
    # 철수와 동생이 가진 토핑 개수
    set_cs = defaultdict(int)
    set_bro = Counter(topping)
    
    # 동생의 조각 : 덱을 통해 한 조각씩 popleft하여 철수에게 전달
    topping = deque(topping)
    
    cnt_cs = 0
    cnt_bro = len(set_bro.keys())
    
    # 토핑이 존재하고, 두 형제가 가진 토핑의 개수가 일치하지 않을 때
    while topping:
        if cnt_cs == cnt_bro:
            answer += 1
        
        # 동생의 케이크에서 철수에게 분배
        cake_topping = topping.popleft()
        set_bro[cake_topping] -= 1
        
        # 동생이 가진 해당 토핑 개수가 0이 된다면 가진 토핑 개수 차감
        if set_bro[cake_topping] == 0:
            cnt_bro -= 1            
        
        if set_cs[cake_topping] == 0:
            cnt_cs += 1
        
        set_cs[cake_topping] += 1
        
        
    
    return answer