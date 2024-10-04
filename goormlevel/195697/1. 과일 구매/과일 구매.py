# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

n, k = map(int, sys.stdin.readline().split())

c_per_p = []
for idx in range(n):
	p, c = map(int, sys.stdin.readline().split())
	c_per_p.append((p, c // p))
	
c_per_p.sort(key=lambda x:(-x[1], -x[1]*x[0]))

sum_c = 0
for info in c_per_p:
	price, per_c = info
	
	if k - price >= 0:
		k -= price
		sum_c += per_c * price
		
	else:
		sum_c += k * per_c
		k = 0

print(sum_c)