 #!/usr/bin/env python3

import readline
import operator
import sys
from termcolor import colored, cprint

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
			if operand < 0:
				cprint(operand, 'red', end=' ')
			elif operand >= 0:
				print(operand, end=' ')
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			cprint(operand, 'yellow')
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		try:
			read_in = input('rpn calc> ')
			if read_in == "quit":
				break
			result = calculate(read_in)
			print("Result: ", result)
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print("Invalid input! Please retry calculation")
			

if __name__ == '__main__':
	main()
