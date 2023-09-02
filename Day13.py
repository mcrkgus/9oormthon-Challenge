N, K = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

# dy/dx 배열을 선언합니다.
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(i, j):

	stack = [(i, j)]

	#건물의 유형을 미리 저장해둘게요.
	building_type = town[i][j]

	# 조건을 만족하는 건물의 개수를 세어서, 단지가 될 수 있는지 확인하기 위해 변수를 선언합니다.
	cnt = 0
	
	# stack에 원소가 없을 때까지 반복합니다.
	while stack:
		y, x = stack.pop()

		if town[y][x] != building_type:
			continue
		else : 
			town[y][x] = 0
			cnt += 1
		
		for k in range(4):
			ny = y + dy[k]
			nx = x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or town[ny][nx] != building_type:
				continue
		
			stack.append((ny, nx))
	
	return cnt



cnt = [0] * 31

# 모든 위치에 대해 탐색을 해봅시다.
for i in range(N):
	for j in range(N):
		if town[i][j]:
			building_type = town[i][j]
			if dfs(i, j) >= K:
				cnt[building_type] += 1

result, temp = 0, 0


for i in range(31):
	if temp <= cnt[i]:
		result = i
		temp = cnt[i]

print(result)
