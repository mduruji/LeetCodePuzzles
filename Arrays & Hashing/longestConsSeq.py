class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        countDict = dict()
        j = 0

        for i in range(len(nums)):
            if nums[i] == nums[i-1] +1:
                countDict[j].append(nums[i])
            else:
                j += 1
                countDict[j] = [nums[i]]
        
        max_key = max(countDict, key=lambda k: len(countDict[k]))
        count = len(countDict[max_key])
        return count