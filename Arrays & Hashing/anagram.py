class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        myCounter1 = Counter(s)
        myCounter2 = Counter(t)
        if myCounter1 == myCounter2:
            print(myCounter1)
            return True
        return False
    
    
    #This is slower because of sorting
    def isAnagram2(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False