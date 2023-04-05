# 스택으로 nested된 코드인지 확인
def check_nested(code):
    stack = []
    
    # 스택의 top에 있는 태그
    temp = ''
    idx = 0
    while idx != len(code):
        if code[idx] == '<':
            tag_idx = idx + 1
            
            # 닫는 괄호가 나올 때 까지 다음 인덱스부터 탐색
            while code[tag_idx] != '>':
                temp += code[tag_idx]
                tag_idx += 1
                
            # 빠져나온 후 인덱스 업데이트
            idx = tag_idx
    
        else:
            idx += 1
            
        # 추출한 태그 구분
        # 1. 열고 닫는 태그
        if temp and temp[-1] == '/':
            temp = ''
            continue
            
        if temp and temp[0] != '/':
            tag = temp.split()[0]
            stack.append(tag)
            
        elif temp and temp[0] == '/':
            if stack and stack[-1] == temp[1:]:
                stack.pop()
                
            else:
                return 'illegal'
            
        temp = ''
        
    if stack:
        return 'illegal'
    
    else:
        return 'legal'
        
while True:
    codes = input()
    if codes == '#':
        break
    
    is_specified = check_nested(codes)
    
    print(is_specified)
    