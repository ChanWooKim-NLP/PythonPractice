# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

t = int(sys.stdin.readline())

for _ in range(t):
	x, y, n = map(int, sys.stdin.readline().split())
	
	if abs(x) + abs(y) > n:
		print('NO')
		continue
	
	if (x + y) % 2 == 1 and n % 2 == 1:
		print('YES')
		
	elif (x + y) % 2 == 0 and n % 2 == 0:
		print('YES')
		
	else:
		print('NO')