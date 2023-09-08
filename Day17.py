N, M = map(int, input().split())
graph = [set([]) for _ in range(N+1)]   #인접리스트 형태의 그래프 만들기 

for i in range(M) :
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    
def dfs(x, visited) :
    stack = [x]
    visited[x] = True
    history = []
    while stack : #stack이 빌 때까지
        now = stack.pop()
        history.append(now)
        
        for i in graph[now] :
            if not visited[i] :
                stack.append(i)
                visited[i] = True
            else :
                graph[i].remove(now)
    return history

def sol(N, M, graph) :
    answer = []
    max_num = 0
    visited = [False] * (N+1) 

    for i in range(1, N+1) :
        if not visited[i] :
            ans = dfs(i, visited)
            edges = 0
            for j in ans :
                edges += len(graph[j])
            e = edges / len(ans)

            if max_num < e :
                max_num = e
                answer = ans
            elif max_num == e :
                if len(answer) > len(ans) :
                    max_num = e
                    answer = ans
                elif len(answer) == len(ans) :
                    if min(answer) > min(ans) :
                        max_num = e
                        answer = ans
    print(*sorted(answer))       

sol(N, M, graph)
