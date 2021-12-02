from utils.aoc_utils import AOCDay, day

@day(1)
class Day1(AOCDay):
    def common(self):
        #print(self.inputData)
        return 0

    def part1(self):
            prev = 0
            count = 0
            for i in self.inputData:
                curr = int(i)
                if prev < curr:
                    count += 1
                prev = curr
            return count-1
    
    def part2(self):
        middle = []
        for line in range(1, len(self.inputData) -1):
            middle.append(int(self.inputData[line-1]) + int(self.inputData[line]) + int(self.inputData[line+1]))
        count = 0
        for i in range(len(middle)-1):
            if middle[i] < middle[i+1]:
                count += 1
        return count