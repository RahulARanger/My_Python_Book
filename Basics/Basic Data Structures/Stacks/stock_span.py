
def detect(values):
	length = len(values)
	store = [1]
	till_now = values[0], 0

	for value in range(1, length):
		if till_now[0] <= values[value]:
			till_now = values[value], value
			store.append(value + 1)
		else:
			store.append(1)
			till_now = values[value]

	return store


if __name__ == "__main__":
	print(detect([13, 15, 12, 14, 16, 8, 6, 4, 10, 30]))



