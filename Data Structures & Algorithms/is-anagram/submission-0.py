class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for letter in s:
            sDict[letter] = sDict.get(letter,0) + 1
        for letter in t:
            tDict[letter] = tDict.get(letter,0) + 1
        for skey, svalue in sDict.items():
            if tDict.get(skey,0) != svalue:
                return False
        for tkey, tvalue in tDict.items():
            if sDict.get(tkey,0) != tvalue:
                return False
        return True
