class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = 0
        dist = 0

        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1

            chars.add(s[j])
            dist = max(dist, j - i + 1)

        return dist

