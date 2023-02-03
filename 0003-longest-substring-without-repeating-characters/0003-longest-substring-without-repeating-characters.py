class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        while left < len(s):
            temp = set([])
            right = left 
            while right < len(s) and s[right] not in temp:
                temp.add(s[right])
                right += 1
            if len(temp) > count:
                count = len(temp)
            left += 1
        return count
        