from stack import SimpleStack

def bracketBalance(raw):
	allowed = {
	'[':']',
	'{':'}',
	'(':')'
	}
	

	checker = SimpleStack()

	for char in raw:
		if char not in allowed and char not in allowed.values():
			continue

		if char in allowed:
			checker.append(char)
		else:
			if not checker.top() or allowed[checker.top()] != char:
				return False

			checker.pop()


	return checker.isEmpty() 


if __name__ == "__main__":
	print(bracketBalance("([])"))
	print(bracketBalance("((())"))
	print(bracketBalance("([)]"))
	print(bracketBalance("{}([()])"))
	print(bracketBalance("(()))"))