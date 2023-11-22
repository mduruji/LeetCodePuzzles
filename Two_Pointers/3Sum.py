class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        from itertools import combinations
        resDict = dict()
        j = 0
        combinations_list = combinations(nums, 3)
        combs = list(filter(lambda comb: sum(comb) == 0, combinations_list))

        for comb in combs:
            a = sorted(comb)
            if a not in resDict.values():
                resDict[j] = a
                j += 1
            
        return resDict.values()