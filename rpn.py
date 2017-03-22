 #!/usr/bin/env python3

import readline
import operator

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod
}

def calculate(arg):
	stack = list()
	if False:
		print("Branch never taken")

	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result: ", result)

if __name__ == '__main__':
	main()
