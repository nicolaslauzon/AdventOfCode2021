from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        #print(self.inputData)
        return 0

    def part1(self):
        horizontal = depth = 0
        for line in self.inputData:
            direction, amount = line.split(" ")
            if direction[0] == "f":
                horizontal += int(amount)
            elif direction[0] == "d":
                depth += int(amount)
            elif direction[0] == "u":
                depth -= int(amount)
        print(depth * horizontal)
    
    def part2(self):
        horizontal = aim = depth = 0
        for line in self.inputData:
            direction, amount = line.split(" ")
            if direction[0] == "f":
                a = int(amount)
                horizontal += a
                depth += aim * a
            elif direction[0] == "d":
                aim += int(amount)
            elif direction[0] == "u":
                aim -= int(amount)
        return depth * horizontal