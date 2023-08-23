class Solution:
    def numDecodings(self, s: str) -> int:
      
        @cache
        def dp(idx,curr_num):
            if curr_num[0] == "0" or int(curr_num) > 26:
                return 0
            
            if idx == len(s) - 1:
                return 1

            return  dp(idx + 1,s[idx + 1]) + dp(idx + 1, curr_num + s[idx + 1])
               
        return dp(0,s[0])  