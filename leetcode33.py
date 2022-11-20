import random
import time
from math import floor
import timeit
class Solution:
    def searchPythonic(self, nums: list, target: int) -> int:
        pivot = 0
        if nums[0] > nums[-1]:
            pivot = ((self.findPivot(nums)) % len(nums)) + 1

        ### Cheese way of doing it ###
        # nums = nums[pivot:] + nums[:pivot]
        # output = self.binarySearchWithCheese(nums, target)
        # if output < 0: return -1
        # return max(-1,self.rotate(len(nums),pivot,output))

        ### Non-pythonic way of doing it ###
        return self.binarySearchPythonic(nums, pivot, target, 0, len(nums) - 1)

    def searchCheese(self, nums: list, target: int) -> int:
        pivot = 0
        if nums[0] > nums[-1]:
            pivot = ((self.findPivot(nums)) % len(nums)) + 1

        ## Cheese way of doing it ###
        nums = nums[pivot:] + nums[:pivot]
        output = self.binarySearchWithCheese(nums, target)
        if output < 0: return -1
        return max(-1,self.rotate(len(nums),pivot,output))

    # Assumes there is a pivot
    def findPivot(self, nums: list):
        if len(nums) == 1:
            return 0

        pivotIndex = floor(len(nums) / 2)
        pivot = nums[pivotIndex]
        if pivot > nums[-1]:
            return pivotIndex + self.findPivot(nums[pivotIndex:])
        elif pivot < nums[0]:
            return self.findPivot(nums[:pivotIndex])
        else:
            return len(nums) - 1

    def binarySearchPythonic(self, nums, pivot, target, left, right):
        if left > right:
            return -1
        elif left == right:
            if nums[self.rotate(len(nums), pivot, left)] != target:
                return -1
            else:
                return self.rotate(len(nums), pivot, left)
        elif right - left == 1 and (nums[self.rotate(len(nums), pivot, left)] != target and nums[self.rotate(len(nums), pivot, right)] != target):
            return -1
        halfpoint = self.rotate(len(nums), pivot, left + floor((right - left) / 2))

        if target > nums[halfpoint]:
            return self.binarySearchPythonic(nums, pivot, target, self.unrotate(len(nums), pivot, halfpoint + 1), right)
        elif target < nums[halfpoint]:
            return self.binarySearchPythonic(nums, pivot, target, left, self.unrotate(len(nums), pivot, halfpoint - 1))
        else:
            return halfpoint

    def binarySearchWithCheese(self, nums, target):
        # print(nums)
        if len(nums) == 1 and nums[0] != target:
            return -1e8
        if len(nums) == 0:
            return -1e8
        halfpoint = floor(len(nums) / 2)

        if target > nums[halfpoint]:
            return halfpoint + self.binarySearchWithCheese(nums[halfpoint:], target)
        elif target < nums[halfpoint]:
            return self.binarySearchWithCheese(nums[:halfpoint], target)
        else:
            return halfpoint

    def unrotate(self, length, pivot, rotated):
        return (rotated - pivot) % length

    def rotate(self, length, pivot, pos):
        return (pos + pivot) % length
    
s = Solution()
for n in range(10,1000):
    pythonictimes = []
    cheesetimes = []
    trials = 100
    for trial in range(trials):
        large_array = [0] * n
        for i in range(n):
            large_array[i] = i

        p = random.randint(0,n)
        t = random.randint(0,n)
        large_array = large_array[p:] + large_array[:p]
        start = time.time()
        s.searchPythonic(large_array,t)
        pythonictimes.append(time.time() - start)
        s.searchCheese(large_array, t)
        cheesetimes.append(time.time() - start)

    print(str(n) + "," + str(sum(pythonictimes)/trials) + "," + str(sum(cheesetimes)/trials))