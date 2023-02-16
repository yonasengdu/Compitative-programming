class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        value = {}
        for i in range(len(s)):
            for j in range(len(indices)):
                if i == indices[j] :
                    value[i] = s[j]
        return "".join([ind for ind in value.values()])
                    