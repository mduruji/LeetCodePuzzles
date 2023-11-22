class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        ans = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                h = lambda x,y: x if x < y else y
                b = j - i
                curr = h(height[i],height[j]) * b
                if curr > ans:
                    ans = curr
    
        return ans