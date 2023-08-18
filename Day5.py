#10진수를 2진수로 변경 -> bin() 사용
#1의 개수 : count()
N, K = map(int, input().split())
numlist = list(map(int, input().split()))
bin_num = []
for i in numlist :
    #bin_num에 1의개수와 10진수 모두 저장 
    bin_num.append((list(bin(i)).count('1'),i))


bin_num.sort(reverse = True)    #내림차순 정렬 
print(bin_num[K-1][1])  #index값은 K-1을 헤줘야함
