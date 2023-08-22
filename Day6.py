#문자열을 가능한 조합으로 나누는 함수 search 
#start는 문자열 조합의 시작, cnt는 남은 문자열을 몇 부분으로 나눌 것인지 
def search(start, cnt):
    global set  #set에 저장, 중복 허용하지 않음
    if cnt == 0:
        set.add(s[start:])
        return
    for i in range(start + 1, n - cnt + 1):
        set.add(s[start:i])
        search(i, cnt - 1)

#문자열 조합에서 최대값 계산을 위함
#P는 문자열을 임시로 저장하는 배열
def cal(start, cnt):
    global result
    if cnt == 0:
        result = max(result, map[s[start:]] + map[P[1]] + map[P[2]])
        return
    for i in range(start + 1, n - cnt + 1):
        P[cnt] = s[start:i]
        cal(i, cnt - 1)

n = int(input())
s = input().strip()
set = set()
P = [''] * 3
result = -1
map = {}
search(0, 2)
index = 1
for string in sorted(set):
    map[string] = index
    index += 1
cal(0, 2)
print(result)
