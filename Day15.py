
N, K = map(int, input().split()) #N:과일의개수, K:가진돈
fruit=[]
cnt = 0
for i in range(N) :
    P, C = map(int, input().split())    #P:각 과일의 가격, C:포만감
    value = C // P
    fruit.append([P, C, value])



fruit.sort(key=lambda x : x[2], reverse=True)


for i in range(N) :
    if K >= fruit[i][0] :
        cnt += fruit[i][1]
        K -= fruit[i][0]
    else :
        cnt += (fruit[i][1] // fruit[i][0]) * K
        K = 0

print(cnt)
 

    
