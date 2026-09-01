class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CntS, CntT = {}, {}
        for i in range(len(s)):
            CntS[s[i]] = 1 + CntS.get(s[i], 0)
            CntT[t[i]] = 1 + CntT.get(t[i], 0)
        
        return CntS == CntT
