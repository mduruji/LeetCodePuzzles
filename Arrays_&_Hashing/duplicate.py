class Solution:
    def containsDuplicate(self, nums) -> bool:
        numsAndCount = dict()
        for i in range(len(nums)):
            numsAndCount[nums[i]] = 0
        for i in range(len(nums)):
            numsAndCount[nums[i]] += 1
        for value in numsAndCount.values():
            if value != 1:
                return True
        return False
    
    #Better Solution
    def containsDuplicate2(self, nums) -> bool:
        nums = sorted(nums)
        if len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] == nums[i -1]:
                    return True
        return False