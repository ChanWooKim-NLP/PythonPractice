from math import ceil

def solution(picks, minerals):
    # 곡괭이 별 피로도
    mine = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    
    stone_to_idx = {
        'diamond' : 0,
        'iron' : 1,
        'stone' : 2
    }
    
    answer = float('inf')
    
    # 모두 캐는데 필요한 곡괭이 수
    max_use = ceil(len(minerals) / 5)
    
    def dfs(total_cnt, use_mine_list=[]):
        nonlocal answer
        
        # 모든 광물을 캘 수 없는 경우
        if picks[0] == picks[1] == picks[2] == 0:
            tired_cnt = 0
            
            for idx, stone in enumerate(minerals):
                # 더 이상 캘 수 없으면 끝
                if idx // 5 >= len(use_mine_list):
                    break
                    
                mine_idx = use_mine_list[idx // 5]
                stone_idx = stone_to_idx[stone]
                tired_cnt += mine[mine_idx][stone_idx]
                
            answer = min(answer, tired_cnt)
            return
        
        # 선택한 곡괭이 수로 모든 광물을 캘 수 있는 경우 
        if total_cnt == max_use:
            tired_cnt = 0
            
            # 곡괭이와 광물 별 피로도 측정
            for idx, stone in enumerate(minerals):
                mine_idx = use_mine_list[idx // 5]
                stone_idx = stone_to_idx[stone]
                tired_cnt += mine[mine_idx][stone_idx]
            
            answer = min(answer, tired_cnt)
            return
        
        # 사용 가능한 곡괭이 조합을 구함
        for idx in range(len(picks)):
            if picks[idx] > 0:
                picks[idx] -= 1
                use_mine_list.append(idx)
                
                dfs(total_cnt+1, use_mine_list)
                
                use_mine_list.pop()
                picks[idx] += 1
                
        return 
    
    dfs(0)
    
    return answer