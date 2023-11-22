class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        biggerAngList = []
        angDict = dict()
        for i in strs:
            t = "".join(sorted(i))
            if t in angDict:
                # if i not in angDict[t]:
                angDict[t].append(i)
            else:
                angDict[t] = [i]
        for value in angDict.values():
            biggerAngList.append(value)
        return biggerAngList