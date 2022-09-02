class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls = list(s)
        lt = list(t)
        finalstr = ""
        for i in lt:
            if i not in ls:
                finalstr += i
            else:
                ls.remove(i)
        return finalstr
     
        