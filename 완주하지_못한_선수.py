from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    player_dict = Counter(participant)
    comp_dict = Counter(completion)
    
    for p in player_dict:
        if player_dict[p] != comp_dict[p]:
            return p
