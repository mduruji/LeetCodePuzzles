class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(char.lower() for char in s if char.isalnum())
        if s2 == s2[::-1]:
            return True
        return False