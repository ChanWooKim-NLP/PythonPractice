from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 중복 티켓 제거하여 그래프에 추가
    for start, end in tickets:
        graph[start].append(end)
    
    # 알파벳 순 정렬
    # 스택으로 제일 먼저 가야하는 공항이 top으로 가도록 역순 정렬
    for key in graph:
        graph[key].sort(reverse=True)    
    
    answer = []
    def dfs():
        stack = ["ICN"]
        # 현재 공항 answer에 추가
        
        while stack:
            top = stack[-1]
            
            # 해당 공항에서 출발하는 항공권이 없는 경우
            if not graph[top]:
                answer.append(stack.pop())
            
            # 해당 공항에서 출발 가능한 경우 인접 공항을 스택에 삽입
            else:
                stack.append(graph[top].pop())
    
    # 스택은 거꾸로 쌓이므로 역순으로 출력
    dfs()
    return answer[::-1]