N, n = map(int, input().split())
area = [input().split() for _ in range(N)]
bomb = [[0]*N for _ in range(N)]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def cal (y, x) :
	for i in range(5) :
		ny = y + dy[i]
		nx = x + dx[i]
		if 0 <= nx < N and 0 <= ny < N :
			if area[ny][nx] == '@' : bomb[ny][nx] += 2
			elif area[ny][nx] == '#' : bomb[ny][nx] += 0
			else : bomb[ny][nx] += 1
	
            
for i in range(n) :
    y, x, = map(int, input().split())
    cal(y-1, x-1)
  
max_bomb = -1

for i in bomb:
    if max(i) > max_bomb:
        max_bomb = max(i)

    
print(max_bomb)
