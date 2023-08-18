class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
          
        # optimisation - since we can't form valid ip using string greater than 12 by only placeing 3 dots 
        if len(s) > 12:
            return []
        
        ips = []
        
        def backtrack(i,num_dots,curr_ip):
            if i == len(s) and num_dots == 4:
                ips.append(curr_ip[:~0])
                
            if num_dots > 4:
                return
            
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1,num_dots + 1,curr_ip + s[i:j+1]+"." )
                    
        backtrack(0,0,"")
        
        return ips
        