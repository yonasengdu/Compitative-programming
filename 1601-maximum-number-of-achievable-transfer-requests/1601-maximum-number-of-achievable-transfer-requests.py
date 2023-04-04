class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        self.comb_arr = []
        self.ans = 0
        
        def backtrack(start,comb,k):
            if len(comb) == k:
                self.comb_arr.append(comb[:])
                return
            
            if start == len(requests):
                return
            
            for num in range(start,len(requests)):
                comb.append(requests[num])
                
                backtrack(num+1,comb,k)
                
                comb.pop()
                
        def checker(arr):
            
            
            for req_comb in arr:
                validator_dict = defaultdict(int)
                for req in req_comb:
                    fromm = req[0]
                    to = req[1]
                    
                    validator_dict[fromm] -= 1
                    validator_dict[to] += 1
                flag = True  
                for val in validator_dict.values():
                    if val != 0:
                        flag = False
                        
                if flag:
                    self.ans = max(self.ans,len(req_comb))
                    
                    
        
        for k in range(len(requests)+1):
            backtrack(0,[],k)
            checker(self.comb_arr)
            self.comb_arr = []
            
            
            
        return self.ans
        