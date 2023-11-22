class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)

        curr = 1
        for i in range(len(nums) - 1, - 1, -1):
            ans[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(len(nums)):
            ans[i] *= curr
            curr *= nums[i]

        return ans