class Solution:

    #Uses less space
    def twoSum(self, nums, target: int) -> list[int]:
        for i, n in enumerate(nums):
            result = target - n 
            if result in nums and nums.index(result) != i:
                return [i, nums.index(result)]

    #Runs faster
    def twoSum2(self, nums, target: int) -> list[int]:
        prevMap = {} #hashmap for every previous element, val: index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i #if difference is not in prevMap
        return 