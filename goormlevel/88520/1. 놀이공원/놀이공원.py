# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n, k = map(int, sys.stdin.readline().split())
	
	arr = [
		list(map(int, sys.stdin.readline().split()))
		for _ in range(n)
	]
	
	prefix_sum = [
		[0] * (n+1)
		for _ in range(n+1)
	]
	
	for i in range(1, n+1):
		for j in range(1, n+1):
			prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
	
	min_trash = 1e9
	for i in range(k, n+1):
		for j in range(k, n+1):
			x1, y1 = i-k, j-k
			
			trash = prefix_sum[i][j] - prefix_sum[i][y1] - prefix_sum[x1][j] + prefix_sum[x1][y1]
			min_trash = min(min_trash, trash)
	
	print(min_trash)