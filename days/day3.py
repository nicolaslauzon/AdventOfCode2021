from os import stat
from utils.aoc_utils import AOCDay, day

@day(3)
class Day3(AOCDay):
    def common(self):
        #print(self.inputData)
        return 0

    def part1(self):
        q_de_1 = [0 for _ in range(len(self.inputData[0]))]
        q_de_bit = len(self.inputData)

        gamma_rate = ""

        for i in self.inputData:
            for j in range(len(i)):
                if(i[j] == "1"):
                    q_de_1[j] += 1
        epsilon = ""
        for i in range(len(q_de_1)):
            if q_de_bit - q_de_1[i] > q_de_1[i]:
                gamma_rate += "0"
                epsilon += "1"
            else:
                gamma_rate += "1"
                epsilon += "0"
        return int(gamma_rate, 2) * int(epsilon, 2)


    def part2(self):
        oxygen_rating = self.inputData
        co2_rating = self.inputData
        i = 0
        while(len(oxygen_rating) > 1):
            oxygen_rating = self.Filter(oxygen_rating, i, self.FindMostCommon(oxygen_rating, i))
            i += 1
        i = 0
        while(len(co2_rating) > 1):
            co2_rating = self.Filter(co2_rating, i, self.FindLeastCommon(co2_rating, i))
            i += 1
        return int(oxygen_rating[0], 2) * int(co2_rating[0], 2)

    @staticmethod
    def FindMostCommon(input, bitI):
        total = 0
        for i in input:
            if i[bitI] == "1":
                total += 1
            else:
                total -= 1
        if total >= 0:
            return "1"
        return "0"

    @staticmethod
    def FindLeastCommon(input, bitI):
        total = 0
        for i in input:
            if i[bitI] == "1":
                total += 1
            else:
                total -= 1
        if total >= 0:
            return "0"
        return "1"
        
    
    @staticmethod
    def Filter(input, bitI, wantedValue):
        output = []
        for i in input:
            if i[bitI] == wantedValue:
                output.append(i)
        return output