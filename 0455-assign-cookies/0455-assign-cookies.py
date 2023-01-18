class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            numOfChildren = 0
            g.sort()
            s.sort()
            for ind in range(len(s)):
                for child_ind in range(len(g)):
                    if s[ind] >= g[child_ind]:
                        numOfChildren += 1
                        g[child_ind] = float("inf")
                        break
            return numOfChildren


 