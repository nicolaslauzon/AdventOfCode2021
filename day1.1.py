with open('day1.1.txt', mode="r") as fich:
	prev = 0
	count = 0
	for i in fich.readlines():
		curr = int(i)
		if prev < curr:
			count += 1
		prev = curr
	print(count-1)