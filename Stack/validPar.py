class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue
            
            if stack:
                if s[i] == ')' and stack.pop() == '(':
                    continue
                elif s[i] == ']' and stack.pop() == '[':
                    continue
                elif s[i] == '}' and stack.pop() ==  '{':
                    continue
                else:
                    return False
            else:
                return False

        if not stack:
            return True
        else:
            return False