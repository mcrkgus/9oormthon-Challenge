def main():
	n = int(input())
	current = []	#구름이와 플레이어의 말이 위치를 저장할 current
	Rg, Cg = map(int, input().split())
	Rp, Cp = map(int, input().split())
	current.append([Rg, Cg])
	current.append([Rp, Cp])

	info = [list(input().split()) for _ in range(n)]
	score = []
	
	def sol(x, y, cnt, com):
		if visited[x][y]: #방문을 했다면
			return 0	#종료

		visited[x][y] = True	#방문 표시 
		if cnt == 0:
		#처음에는 count가 한자리수라고만 생각해서 info[x][y][0]은 count, info[x][y][1]은 command로 설정했는데 오답이 나왔다. 
		#이후 index -1만 command로 하고 나머지는 전부 다 count로 함 
			cnt, com = int(info[x][y][:-1]), info[x][y][-1]
		#위, 왼쪽 이동은 좌표에서 '김소'의 개념 , 아래, 오른쪽은 좌표에서 '증가'의 개념이다. 
		if com == 'U':	#위로 이동
			if x-1 >= 0 : x -= 1 
			else : x = n-1
			return 1 + sol(x, y, cnt-1, com)
		
		elif com == 'D':	#아래로 이동 
			x = (x+1)%n
			return 1 + sol(x, y, cnt-1, com)
		
		elif com == 'L':	#왼쪽으로 이동
			if y-1 >= 0 : y -= 1
			else : y = n-1
			return 1 + sol(x, y, cnt-1, com)
		
		elif com == 'R':	#오른쪽으로 이동 
			y = (y+1)%n
			return 1 + sol(x, y, cnt-1, com)
		
	for x, y in current:
		x -= 1
		y -= 1
		visited = [[False] * n for _ in range(n)]	#visited를 전부 다 방문하지 않음 으로 표시 
		score.append(sol(x, y, 0, ""))
		
	if score[0] < score[1]:
		print("player", score[1])
	else:
		print("goorm", score[0])
	
main()
