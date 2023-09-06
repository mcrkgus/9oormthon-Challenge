N, M = map(int, input().split())

bridge = [[0] * (N+1) for _ in range(N+1)]

parent = [i for i in range(N+1)]

union = []
for i in range(M) :
	s, e = map(int, input().split())
	bridge[s][e] = 1
 
def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(x, y) :
    fx, fy = find(x), find(y)
    if fx < fy : 
        parent[fy] = fx
    elif fx > fy :
        parent[fx] = fy

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if bridge[i][j] == 1 and bridge[j][i] == 1 :
            union(i, j)
res = set()
for i in range(1, N+1) :
    res.add(find(i))

print(len(res))


