T = int(input())
total = 0
for i in range(T) :
	num1, op, num2 = input().split()
	if op == '+' :
		res = int(num1) + int(num2)
	elif op == '-' :
		res = int(num1) - int(num2)
	elif op == '/' :
		res = int(num1) // int(num2)
	elif op == '*' :
		res = int(num1) * int(num2)

	total += res
	
print(total)
