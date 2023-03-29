class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        
        def backtrack(start,sub_seq):
            str_sub_seq = "".join(sub_seq)
            if len(set(str_sub_seq)) == len(str_sub_seq):
                self.ans = max(self.ans,len(str_sub_seq))
            
            if start >= len(arr):
                return
            
            for ind in range(start,len(arr)):
                    sub_seq.append(arr[ind])
                    
                    backtrack(ind+1,sub_seq)
                    
                    if sub_seq:
                        sub_seq.pop()
        backtrack(0,[])
        return self.ans
        