import math


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 1234
        # 1243
        # 1324
        output = self.helper(str(n), str(n), {})
        if output > math.pow(2,31) - 1:
            return -1
        else:
            return output

    def helper(self, numbers, smallest, dp, level=1) -> int:
        # print(str(level) + "  " * level + "problem {} smallest {}".format(numbers, smallest))
        if numbers in dp:
            if smallest in dp[numbers]:
                return dp[numbers][smallest]

        if numbers not in dp:
            dp[numbers] = {}

        numsmallest = int(smallest)
        if len(numbers) == 2:
            opa = int(numbers[0] + numbers[1])
            opb = int(numbers[1] + numbers[0])
            op = sorted([opa, opb])
            for i in op:
                if i > numsmallest:
                    # print(str(level) +"  " * level + "base case selects {}".format(i))
                    dp[numbers][smallest] = i
                    return i
            if numbers in dp:
                dp[numbers][smallest] = -1
            return -1
        if len(numbers) == 1:
            dp[numbers][smallest] = -1
            return -1

        m = {}
        for i in range(len(numbers)):
            tempnumbers = numbers[0:i] + numbers[i + 1:]
            val = numbers[i]
            # print(str(level) +"  " * level + "requesting {}".format(val))
            if int(val) > int(smallest[0]):
                m[val] = self.helper(tempnumbers, "0",dp, level + 1)
            elif int(val) == int(smallest[0]):
                tempsmallest = "0" if numsmallest == 0 else smallest[1:]
                m[val] = self.helper(tempnumbers, tempsmallest,dp, level + 1)
            # else:
                # print(str(level) +"  " * level + "skipping", val)
            # print(str(level) +"  " * level + str(m))
        output = math.inf
        rejected = 0
        for k in m.keys():
            if m[k] == -1:
                rejected += 1
                continue
            temp = int(k) * math.pow(10, len(numbers) - 1) + m[k]
            if temp < output:
                output = temp

        if rejected == len(m):
            return -1
        output = int(output)
        # print(str(level) + "  " * level + "LEVEL" + str(level)  + " DONE " + str(m) + " SELECT " + str(output))
        dp[numbers][smallest] = output
        return output


if __name__ == "__main__":
    s = Solution()
    output = s.nextGreaterElement(2147483476)
    print(output, 230412)
    # output = s.nextGreaterElement(123)
    # print(output, 132)