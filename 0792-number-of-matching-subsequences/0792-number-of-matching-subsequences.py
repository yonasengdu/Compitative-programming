
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:   
        
        cp = defaultdict(list)
        for i,char in enumerate(s):    
            cp[char].append(i)
       
    
        pointer = {char:0 for char in ascii_lowercase}
    
        search = Counter(words)
        
        ans = 0
        for word,count in search.items():
            prev_ind = -1
            valid = 0
            
            for char in word:
                
                for i in range(len(cp[char])):
                    if cp[char][i] > prev_ind: 
                        prev_ind = cp[char][i]
                        pointer[char] += i
                        valid += 1
                        break 
                

            if valid == len(word):
                ans += count
                
        return ans
                    
                
                    
                
                    
                    
                   
                    
                
         
        
        
        