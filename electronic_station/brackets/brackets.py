'''
Task
You are given an expression with numbers, brackets and operators. 
 For this task only the brackets matter. Brackets come in three 
 flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict
 some expression. If a bracket is open, then it must be closed with a closing bracket of the same type.
 The scope of a bracket must not intersected by another bracket.
 For this task, you should to make a decision to correct an expression or not based on the brackets.
 Do not worry about operators and operands.
Input: An expression with different of types brackets as a string (unicode).
Output: A verdict on the correctness of the expression in boolean (True or False).
'''


def checkio(expression):
	stack = [] # this will be used as a stack
	valid_chars = ["{", "}", "(", ")", "[", "]"]
	for char in expression:
		if char not in valid_chars:
			continue
		print("================")
		print("Looking at: " + char)
		print("Stack before: " + str(stack))
		if char in ["{", "(", "["]:
			# if we see an open bracket thing
			stack.append(char)
		elif len(stack) == 0:
			return False
		elif char == "}":
			if stack[-1] == "{":
				stack.pop()
			else:
				return False
		elif char == ")":
			if stack[-1] == "(":
				stack.pop()
			else:
				return False
		elif char == "]":
			if stack[-1] == "[":
				stack.pop()
			else:
				return False
		print("Stack after: " + str(stack))
	if len(stack) != 0:
		return False
	return True



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	# print(checkio(u"((5+3)*2+1)"))
	# print(checkio(u"{[(3+1)+2]+}"))
	# print(checkio(u"(3+{1-1)}"))
	# print(checkio(u"[1+1]+(2*2)-{3/3}"))
	# print(checkio(u"(({[(((1)-2)+3)-3]/3}-3)"))
	# print(checkio(u"2+3"))
	print(checkio("(((1+(1+1))))]"))