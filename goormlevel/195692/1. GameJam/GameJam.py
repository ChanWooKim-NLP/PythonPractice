# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

n = int(sys.stdin.readline())

goorm_x, goorm_y = map(int, sys.stdin.readline().split())
player_x, player_y = map(int, sys.stdin.readline().split())

board = [
	sys.stdin.readline().split()
	for _ in range(n)
]

direction = {
	'L' : [0, -1],
	'R' : [0, 1],
	'U' : [-1, 0],
	'D' : [1, 0]
}

def play(x, y):
	visited = [
		[0] * n
		for _ in range(n)
	]
	visited[x][y] = 1
	score = 1
	
	cx, cy = x, y
	
	comeback = False
	
	while not comeback:
		cur = board[cx][cy]
		count, command = int(cur[:-1]), cur[-1]

		nx, ny = direction[command]
		for i in range(count):
			cx += nx
			cy += ny

			cx %= n
			cy %= n
		
			if not visited[cx][cy]:
				visited[cx][cy] = 1	
				score += 1
		
			else:
				comeback = True
				break
				
	return score
	
goorm_score = play(goorm_x-1, goorm_y-1)
player_score = play(player_x-1, player_y-1)

if goorm_score > player_score:
	print('goorm', goorm_score)
	
else:
	print('player', player_score)