from collections import deque

def solution():
    price = []
    weight = []
    queue = deque()
    
    N, M = map(int, input().split())
    
    parking_lot = [0] * N
    park_available = len(parking_lot)
    
    car = [i+1 for i in range(M)]
    
    for _ in range(N):
        Rs = int(input())
        price.append(Rs)
    
    for _ in range(M):
        Wk = int(input())
        weight.append(Wk)
    
    answer = 0
    for _ in range(2*M):
        i = int(input())
        # 주차 자리가 있다면
        if (park_available > 0) and (i > 0):   
            for l in range(len(parking_lot)):
                if parking_lot[l] == 0:
                    parking_lot[l] = car[i-1]
                    park_available -= 1
                    break
                

             
        elif park_available == 0 and (i > 0):
            queue.append(car[i-1])

        elif park_available == 0 and (i < 0):
            if queue:
                new_car = queue.popleft()
                for l in range(len(parking_lot)):
                    if parking_lot[l] == abs(i):
                        parking_lot[l] = car[new_car-1]
                        answer += weight[abs(i)-1] * price[l]

            else:
                for l in range(len(parking_lot)):
                    if parking_lot[l] == abs(i):
                        parking_lot[l] = 0
                        park_available += 1
                        answer += weight[abs(i)-1] * price[l]
        
        else:
            for l in range(len(parking_lot)):
                if parking_lot[l] == abs(i):
                    parking_lot[l] = 0
                    park_available += 1
                    answer += weight[abs(i)-1] * price[l]


    return answer
            
print(solution())
            
