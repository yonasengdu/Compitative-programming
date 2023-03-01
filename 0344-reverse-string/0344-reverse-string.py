class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s)-1
        def helper(s,l,r):
            if l >= r:
                return s
            
            
            s[l],s[r] = s[r], s[l]
            return helper(s,l+1,r-1)
        
        return helper(s,l,r)
        
        """
        Do not return anything, modify s in-place instead.
        """
        