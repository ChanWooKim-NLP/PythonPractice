import heapq, sys

def merge_page(novels):
    total = 0
    
    # 파일을 합치고 -> 결과 total에 더한 후 -> 힙에 삽입
    # 이 때, 힙의 길이가 1일 시 이 값은 마지막 파일 2개를 합한 비용
    # 더 이상 합칠 파일이 없으므로 계산 종료
    while len(novels) != 1:
        cur_pages = 0
        for _ in range(2):
            cur_pages += heapq.heappop(novels)
            
        total += cur_pages
        heapq.heappush(novels, cur_pages)
        
    return total


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    
    novels = list(map(int, input().split()))
    heapq.heapify(novels)
    
    ans = merge_page(novels)
    print(ans)