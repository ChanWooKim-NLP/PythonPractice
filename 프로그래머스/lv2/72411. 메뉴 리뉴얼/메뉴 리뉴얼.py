from collections import defaultdict

def solution(orders, course):
    menu_dict = defaultdict(int)
    
    # 백트래킹 : 메뉴 조합을 구하여 딕셔너리로 빈도와 같이 저장
    def make_candidate_course(order, idx, target_cnt, comb=[]):
        if len(comb) == target_cnt:
            menu = ''.join(comb)
            menu_dict[menu] += 1
            return
        
        # 원래 단품메뉴 조합에서 백트래킹으로 메뉴 조합하기
        for i in range(idx, len(order)):
            comb.append(order[i])
            make_candidate_course(order, i+1, target_cnt, comb)
            comb.pop()
    
    # 모든 단품메뉴에 대해 백트래킹 조합 수행
    for order in orders:
        order = sorted(list(order))
        for i in range(2, len(order)+1):
            # 조합 구하기 전 알파벳 순 정렬
            # 백트래킹
            make_candidate_course(order, 0, i)
    
    # key : 메뉴 이름 길이 value : 메뉴 이름, 주문 횟수
    length_cnt_dict = defaultdict(list)
    
    for key, val in menu_dict.items():
        if val > 1:
            length_menu = len(key)
            length_cnt_dict[length_menu].append((key, val))
    
    # 딕셔너리 정렬
    for key in length_cnt_dict.keys():
        length_cnt_dict[key].sort(key=lambda x: -x[1])
    
    answer = []
    for menu_len in course:
        # 해당 길이의 메뉴 조합을 주문한 최대 인원
        if menu_len in length_cnt_dict.keys():
            # 해당 key의 0번째 튜플의 0번 인덱스가 최대 주문 횟수 
            max_order = length_cnt_dict[menu_len][0][1]
        
        # 최대 주문이 발생한 메뉴를 저장
        for menu, cnt in length_cnt_dict[menu_len]:
            if cnt == max_order:
                answer.append(menu)
                
            else:
                break
    
    # 정렬
    answer.sort()
    print(answer)
    
    return answer