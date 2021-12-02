with open('day2.1.txt', mode="r") as fich:
	horizontal = depth = 0
	for line in fich.readlines():
		direction, amount = line.split(" ")
		if direction[0] == "f":
			horizontal += int(amount)
		elif direction[0] == "d":
			depth += int(amount)
		elif direction[0] == "u":
			depth -= int(amount)
	print(depth * horizontal)