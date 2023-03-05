from collections import Counter

def solution(nums):
    hash = Counter(nums)
    
    ponkemon = len(hash.keys())
    max_can_bring = len(nums) // 2
    
    answer = min(max_can_bring, ponkemon)
    return answer