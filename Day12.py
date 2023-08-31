import sys
sys.setrecursionlimit(10**5) 

N = int(input())
town = [list(map(int, input().split())) for _ in range(N)]

result = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(i, j):
	stack = [(i, j)]
	while stack:
		y, x = stack.pop()

		if not town[y][x]:
			continue
		town[y][x] = 0

		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			if ny in (-1, N) or nx in (-1, N) or not town[ny][nx]:
				continue
			stack.append((ny, nx))
			
			
for i in range(N):
	for j in range(N):
		if town[i][j]:
			result += 1
			dfs(i, j)

print(result)
