import sys

n, m = map(int, sys.stdin.readline().split())

min_price = 1e9

package_min = 1e9
each_min = 1e9

for _ in range(m):
    package, each = map(int, sys.stdin.readline().split())
     
    package_min = min(package, package_min)
    each_min = min(each_min, each)

package_cnt = n // 6

# 1. 패키지로 전부 살 때
all_package = package_min * (package_cnt+1)

# 2. 패키지와 낱개 섞어서 살 때
mix_package_each = package_min * package_cnt + (each_min * (n%6))

# 3. 전부 낱개로 살 때
all_each = each_min * n

print(min(all_package, mix_package_each, all_each))