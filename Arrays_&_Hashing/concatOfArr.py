class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0 for i in range(2 * len(nums))]
        midp = len(ans) // 2
        ans[0:midp] = nums
        ans[midp:len(ans)] = nums
        return ans