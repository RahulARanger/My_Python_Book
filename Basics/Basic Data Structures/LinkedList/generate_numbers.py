# https://practice.geeksforgeeks.org/tracks/DSASP-Queue/?batchId=154

"""
Question: given that we can use numbers that uses any of digits in {5, 6} then print the first n numbers
in ascending order of the numbers that we can make from it
"""


from queue_ import Queue
from string import digits

# we can do this with any number of digits in fact all the digits
def generate(n):
	"""
	Time Complexity: O(N) if the concat op is O(1)
	"""
	container = Queue()

	container.append('5')
	container.append('6')

	for index in range(n):
		index = container.pop()

		print(index, end=" ")

		container.append(index + "5")
		container.append(index + "6")  
	print()


def preview_generate(n):
	# but we have range tho

	container = Queue()

	for digit in digits:
		container.append(digit)

	for index in range(n):
		index = container.pop()

		print(index, end=' ')

		for digit in digits:
			if index == '0':
				continue
			container.append(index + digit)

	print()		


if __name__ == "__main__":
	generate(10)
	generate(4)

	preview_generate(20)  # range(20)
	preview_generate(100)  # range(100)


