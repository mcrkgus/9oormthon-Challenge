#행렬값이 0일때 인접한 8칸 중에서 구름이 K개 있는 칸의 개수 구하기 
#모든 칸 확인하면서 비어있는 경우에 개수 세기 


n, k = map(int, input().split())
mat = [input().split() for i in range(n)]
dy, dx = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(n):
        if mat[i][j] == '0':
            flag = 0
            for a in range(8):
                y, x = i + dy[a], j + dx[a]
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                flag += int(mat[y][x] == '1')
            mat[i][j] = flag
cnt = 0
for i in range(n):
    cnt += mat[i].count(k)
print(cnt)
