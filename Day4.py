N = int(input())
burger= list(map(int, input().split()))
res = sum(burger)
max_flavor = max(burger)
max_idx = burger.index(max_flavor)

for i in range(N-1) :
    if i < max_idx :
        if burger[i] > burger[i+1] :
            res = 0
    else :
        if burger[i] < burger[i+1] :
            res = 0


		
		
print(res)
