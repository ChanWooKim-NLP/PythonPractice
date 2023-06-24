import sys
input = sys.stdin.readline

n, m = map(int, input().split())

empire_to_idx = {}
idx_to_empire = {}
for i in range(n):
    emp_name = input().strip()
    
    empire_to_idx[emp_name] = i
    idx_to_empire[i] = emp_name

def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

# 두 왕국이 싸운 후 속국을 이룸
def union(x, y, w):
    px, py = find(x), find(y)

    # 문제 조건 상 두 나라는 종주국 - 속국 / 종주국 - 종주국 관계임
    # 만일 종주국 - 속국 관계라면, 속국의 parents 정보는 자기 자신이 아니라 종주국일 것
    # 즉, px와 py가 같은 경우임

    # x 왕국이 승리 -> y의 종주국은 x
    if w == '1':
        if px == py and px != x:
            parents[x] = x
            px = x
        parents[py] = px
    
    # y 왕국이 승리 -> x의 종주국은 y
    else:
        if px == py and py != y:
            parents[y] = y
            py = y
        parents[px] = py
    
parents = [i for i in range(n)]

for _ in range(m):
    emp_name_1, emp_name_2, w = input().strip().split(',')
    emp_idx_1 = empire_to_idx[emp_name_1]
    emp_idx_2 = empire_to_idx[emp_name_2]    
    
    union(emp_idx_1, emp_idx_2, w)
    
    for i in range(n):
        find(i)

not_dependency_list = []
# 전쟁 결과 종주국 리스트
# 국가 번호 -> 국가 이름으로 append
for idx, emp_no in enumerate(parents):
    if idx == emp_no:
        not_dependency_list.append(idx_to_empire[emp_no])
        
# ascii 기준 종주국 정렬
not_dependency_list.sort(key=lambda x: x.split()[-1])

print(len(not_dependency_list))
for emp in not_dependency_list:
    print(emp)