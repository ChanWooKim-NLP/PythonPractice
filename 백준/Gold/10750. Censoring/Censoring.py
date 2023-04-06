s = input()
t = input()

def delete_word_from_stack(delete_word):
    # 삭제 대상 단어 길이만큼 stack의 top에서 탐색
    del_word_len = len(delete_word)
    top_of_stack = stack[-del_word_len:]
    
    # 중간에 일치하지 않는다면 탐색 중단
    for s in range(del_word_len):
        if delete_word[s] != top_of_stack[s]:
            return 
    
    # 일치하면 삭제 단어 길이만큼 pop
    for _ in range(del_word_len):
        stack.pop()
    
    return
        
stack = []
for string in s:
    stack.append(string)
    
    # 1. 스택에 쌓인 문자열이 삭제 대상 문자열 길이보다 크다
    # 2. 스택의 마지막 문자가 삭제 대상 문자열의 마지막 문자와 같으면 탐색 진행
    if len(stack) >= len(t) and string == t[-1]:
        delete_word_from_stack(t)
        

print(''.join(stack))
    
    