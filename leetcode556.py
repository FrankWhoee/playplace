import math


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 1234
        # 1243
        # 1324

        return int(self.helper(str(n), n))

    def helper(self, numbers, smallest) -> int:

        if len(numbers) == 2:
            opa = int(numbers[0] + numbers[1])
            opb = int(numbers[1] + numbers[0])
            op = sorted([opa, opb])
            for i in op:
                if i > smallest:
                    # print(i)
                    return i
            return -1
        if len(numbers) == 1:
            return -1

        m = {}
        for i in range(len(numbers)):
            tempnumbers = numbers[0:i] + numbers[i + 1:]
            val = numbers[i]
            if int(val) > int(numbers[0]):
                m[val] = self.helper(tempnumbers, 0)
            elif int(val) == int(numbers[0]):
                tempsmallest = 0 if smallest == 0 else int(str(smallest)[1:])
                m[val] = self.helper(tempnumbers, tempsmallest)
        output = numbers[0]
        output = int(output) * math.pow(10, len(numbers) - 1) + m[output]
        rejected = 0
        for k in m.keys():
            if m[k] == -1:
                rejected += 1
                continue
            temp = int(k) * math.pow(10, len(numbers) - 1) + m[k]
            if temp < output and m[k] > smallest:
                output = temp

        if rejected == len(m):
            return -1
        print(smallest, m)
        return output


if __name__ == "__main__":
    s = Solution()
    # output = s.nextGreaterElement(230241)
    # print(output, 230412)
    output = s.nextGreaterElement(123)
    print(output, 132)