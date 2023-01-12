class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        if k == 1:
            return arr[-1]
        def recur(arr,k ,i=0):
            if len(arr) == 1:
                return arr[0]
            i = (i + k-1) % len(arr)
            arr.pop(i)
            return recur(arr,k , i)
            
        return recur(arr,k)
        
        