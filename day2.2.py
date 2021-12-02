with open('day2.2.txt', mode="r") as fich:
	horizontal = aim = depth = 0
	for line in fich.readlines():
		direction, amount = line.split(" ")
		if direction[0] == "f":
			a = int(amount)
			horizontal += a
			depth += aim * a
		elif direction[0] == "d":
			aim += int(amount)
		elif direction[0] == "u":
			aim -= int(amount)
	print(depth * horizontal)