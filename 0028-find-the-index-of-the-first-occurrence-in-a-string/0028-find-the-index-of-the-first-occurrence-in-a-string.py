class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_needle = len(needle)
        for ind in range(len(haystack)-len(needle)+1):
            temp_word = haystack[ind:ind+len_needle]
            # print(temp_word,len_needle,ind)
            if temp_word == needle:
                return ind
        return -1
            
        
