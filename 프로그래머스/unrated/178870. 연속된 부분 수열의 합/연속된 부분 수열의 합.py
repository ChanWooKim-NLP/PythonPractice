def solution(sequence, k):
    candidate_index = []
    answer = []
    
    right = 0
    cur_val = 0
    
    cur_len = float('inf')
    for left in range(len(sequence)):
        while cur_val < k and right < len(sequence):
            cur_val += sequence[right]
            right += 1
        
        if cur_val == k:
            if right - left < cur_len:
                candidate_index.append([left, right-1])
                
        cur_val -= sequence[left]
    candidate_index.sort(key=lambda x: (x[1]-x[0], x[0]))
    
    answer = candidate_index[0]
    return answer