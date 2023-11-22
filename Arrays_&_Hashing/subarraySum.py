class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        z = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
                continue
                
            else:
                z = nums[i]
                for j in range(i + 1, len(nums)):
                    if z + nums[j] == k:
                        count += 1
                        break
                    
                    z += nums[j]
        
            
        return count