class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer = 0
        len_word1 = len(word1)
        len_word2 = len(word2)
        min_num_word = min(len_word1,len_word2)
        merged_word = ""
        while pointer < min_num_word:
            merged_word += f'{word1[pointer]}{word2[pointer]}'
            pointer+=1
        if len_word1 > len_word2:
            for latter in word1[pointer:]:
                merged_word += latter
        else: 
            for latter in word2[pointer:]:
                merged_word += latter
        return merged_word
            
            
          
        
        
        