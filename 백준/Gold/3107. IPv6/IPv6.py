ip = input()

# 전체 구간 개수 8개
ip_split = ip.split(':')

origin_ip = ''

# 엣지 케이스 -> ::으로 시작하거나 끝나는 경우 : 기준 split하면 공백이 2개 이상 생김
# 전처리 수행하여 ''이 2개 이상 나오는 경우 제거
if ip_split[0] == '':
    ip_split = ip_split[1:] 

if ip_split[-1] == '':
    ip_split = ip_split[:-1]   

for adress in ip_split:
    # 주소가 비어있다면 연속된 0 그룹 -> 복구
    if adress == '':
        # 복구 횟수는 8에서 0이 아닌 주소값 개수 차이
        origin_ip += '0000:' * (8 - len(ip_split) + 1)
        
    else:
        origin_ip += adress.zfill(4) + ':'

# 마지막 : 제거
print(origin_ip[:-1])
    