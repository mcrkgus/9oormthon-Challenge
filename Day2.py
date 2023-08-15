N = int(input())
T, M = map(int, input().split())
c = [int(input()) for _ in range(N)]
total = 0
def cal(N, T, M, c) :
    total = sum(c)
    hour = total // 60
    minute = total % 60
    final_M = M + minute
    final_T = T + hour
    
    if final_M > 59 :
        final_M -= 60
        final_T += 1
        
    print(final_T%24, final_M)
    return 

cal(N, T, M, c)
