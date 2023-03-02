from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    
    answer = 0
    bridge = deque([0] * bridge_length)
    weight_bridge_sum = 0
    
    while bridge:
        weight_bridge_sum -= bridge.popleft()
        answer += 1
        
        # 대기 트럭이 있고 새로 추가될 트럭과 다리 위 트럭 무게의 합이 지탱 무게를 넘지 않을 경우
        if truck_weights:
            if weight_bridge_sum + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                weight_bridge_sum += new_truck
        
            # 다리 길이 유지 위해 0 입력
            else:
                bridge.append(0)
            
    return answer