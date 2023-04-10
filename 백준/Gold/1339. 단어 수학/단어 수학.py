from collections import defaultdict

n = int(input())

word_dict = defaultdict(int)

word_list = []
for _ in range(n):
    word = input()
    word_list.append(word)

for word in word_list:
    for i in range(len(word)):
        # 알파벳 별로 위치한 자리수를 십진수로 나타낸 딕셔너리 구축
        # ABDEB : [10000, 1001, 100, 10]
        word_dict[word[i]] += 10 ** (len(word) - i - 1)

# 내림차순 정렬, 
word_to_val = list(word_dict.values())
word_to_val.sort(reverse=True)

# 자리수가 높은 알파벳이 높은 숫자를 부여받음
ans = 0
pows = 9
for val in word_to_val:
    ans += val * pows
    pows -= 1
    
print(ans)
