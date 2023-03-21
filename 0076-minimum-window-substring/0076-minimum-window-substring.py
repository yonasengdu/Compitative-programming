class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
                return ""
        
        unique = Counter(t)
        
        min_len_win = (float(inf),None,None)
        
        formed = 0
        
        window = defaultdict(int)
        
        left = 0
        
        for right in range(len(s)):
            
            window[s[right]] += 1
            
            if s[right] in unique and  window[s[right]] == unique[s[right]]:
                formed += 1
            
            while left <= right and  formed == len(unique):
                 
                if right - left + 1 < min_len_win[0]:
                    min_len_win = (right - left + 1 , left,right)
                      
                window[s[left]] -= 1
                
                if s[left] in unique and  window[s[left]] < unique[s[left]]:
                        formed -= 1
            
             
                    
                left += 1
                
        return "" if min_len_win[0] == float(inf) else s[min_len_win[1] : min_len_win[2] + 1]
                