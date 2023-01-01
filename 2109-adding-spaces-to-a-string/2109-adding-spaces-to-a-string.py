class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        ptr = 0
        len_s = len(s)
        for latter_index in range(len_s):
            value = s[latter_index]
            if  ptr < len(spaces) and latter_index == spaces[ptr]:
                value = s[latter_index]
                ans.append(f' {value}')
                ptr += 1
            else:
                ans.append(value)
        return ''.join(ans)
        