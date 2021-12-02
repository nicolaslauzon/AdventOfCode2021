with open('day1.2.txt', mode="r") as fich:
	lines = fich.readlines()
	middle = []
	for line in range(1, len(lines) -1):
		middle.append(int(lines[line-1]) + int(lines[line]) + int(lines[line+1]))
	count = 0
	for i in range(len(middle)-1):
		if middle[i] < middle[i+1]:
			count += 1
	print(count)
