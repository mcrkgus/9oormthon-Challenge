from collections import deque

def bfs(start, off):
	if start == off:
		return -1
	
	visited = [0] * (N + 1)
	q = deque([start])
	visited[start] = 1
	step = 1
	
	while q:
		step += 1
		for _ in range(len(q)):
			now = q.popleft()

			for to in graph[now]:
				if visited[to] or to == off:
					continue
					
				if to == E:
					return step
				
				visited[to] = 1
				q.append(to)
	
	return -1
	
N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(1, N + 1):
	print(bfs(S, i))
