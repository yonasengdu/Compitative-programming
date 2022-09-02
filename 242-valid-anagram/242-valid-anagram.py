class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t: return False
        for j in t:
            if j not in s:return False
        sl = [i for i in s]
        tl = [i for i in t]
        sl.sort()
        tl.sort()
        if sl != tl[:len(sl)]:return False    
        return True
        