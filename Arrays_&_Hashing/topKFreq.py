class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        myNums = Counter(nums)
        ans = [i[0] for i in myNums.most_common(k)]
        return ans