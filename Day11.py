N = int(input())
A, B = map(int, input().split())
cnt = 0 

def sol (N, A, B) :
	max_num = N // B
	for i in range(max_num, -1, -1) :
		n = N - (B*i)
		if n % A == 0 :
			cnt = n // A
			print(cnt+i)
			return 
	print(-1)
	return
sol(N, A, B)
