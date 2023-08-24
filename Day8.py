item = [1, 7, 14]
N = int(input())
res = 0


if N < 7 :
	res += N
elif N < 14 : 
	res += N - 6
else :
	res += N//14
	N %= 14
	if N < 7 :
		res += N
	else : 
		res += N - 6

print(res)
