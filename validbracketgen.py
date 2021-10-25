# Generates string composed of characters ()[] that is valid when evaluated using stack method.
from random import randint


brackets = ["(",")","[","]"]

def genvalidbrackets(length):
	stack = []
	output = ""
	for i in range(int(length/2)):
		if(len(stack) == 0):
			output += brackets[randint(0,1) * 2]
			stack.append(output[-1])
		else:
			if randint(0,1) == 0:
				output += brackets[randint(0,1)*2]
				stack.append(output[-1])
			else:
#				print(brackets[brackets.index(stack[-1])-1])
				output += brackets[brackets.index(stack[-1])+1]
				stack.pop()
	for i in range(len(stack)):
		output += brackets[brackets.index(stack[-1])+1]
		stack.pop()
				
	return output
	

def validatebrackets(string):
	stack = []
	for s in string:
		if s == "(" or s == "[":
			stack.append(s)
		elif (s == ")" or s == "]"):
			if(stack.pop() != brackets[brackets.index(s)-1]):
				return False
		else:
			return False
	return len(stack) == 0
	
# test functions
n = 100
s = 0
strlen = 10
for i in range(n):
	if validatebrackets(genvalidbrackets(10)):
		s += 1
for i in range(10):
	print(genvalidbrackets(30))
print(genvalidbrackets(10))
print(validatebrackets("()[](((([]))))"))
print("Success: " + str(s * 100/n) + "%")
