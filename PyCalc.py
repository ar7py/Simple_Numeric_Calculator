a = int(input("Enter A Numbeer:"))
b = int(input("Enter A Numbeer:"))

def calc(a,b,op='add'):
	if op == 'add':
		return a + b
	if op == 'sub':
		return a - b
	elif op == 'mul':
		return a * b
	elif op == 'div':
		return a / b
	if op == 'sqr':
		return a ** b
	else:
		print("Invalid Operation!")

print("Result:")
# For different operations change op, like op='add',op='mul' etc.
print(calc(a, b, op='div'))

