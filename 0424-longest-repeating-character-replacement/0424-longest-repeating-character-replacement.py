class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        sub_arr_len = 0
        for latter in string.ascii_uppercase:
            sub_arr_len = max(sub_arr_len,self.checker(latter,k,s))
        return sub_arr_len
   
    def checker(self,char,k,s): 

        left = 0
        converted = 0
        length = 0
        for right  in range(len(s)):
            if s[right] != char:
                converted += 1

            while converted > k:
                if s[left] != char:
                    converted -= 1
                left += 1
             
            length = max(length, right - left + 1) 
        return length

        
 
