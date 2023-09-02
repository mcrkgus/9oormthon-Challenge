# 한 번 방문한 노드는 다시 방문할 수 없다 -> visited를 체크하기 
# 방문할 수 있으면서 번호가 가장 작은 노드로 이동 -> 
# 그래프 표현 방법 : 인접 리스트 
import sys
sys.setrecursionlimit(10**4)

N, M , K= map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)
	
visited = [False] * (N+1)
def dfs(current) :
	for i in sorted(graph[current]) :	#현재 노드 current에서 이동 가능한 정점들을 정렬해서 순회하기 
		if visited[i] == 0 :	#방문하지 않았더라면 
			visited[i] = 1	#방문하고
			return dfs(i)	#탐색
	else : return current	
	
visited[K] = 1
res = dfs(K)
print(sum(visited), res)
