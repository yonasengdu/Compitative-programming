class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_arr = s.split()
        len_max = 0
        ans = []
        for word in word_arr:
            len_max = max(len(word),len_max)
        for word_ptr in range(len_max):
            temp_ans = []
            for latter_ptr in range(len(word_arr)):
                word = word_arr[latter_ptr]
                if word_ptr < len(word):
                    temp_ans.append(word[word_ptr]) 
                else:
                    temp_ans.append(" ")
            ans.append(''.join(temp_ans).rstrip())
        return ans
            
                    
                