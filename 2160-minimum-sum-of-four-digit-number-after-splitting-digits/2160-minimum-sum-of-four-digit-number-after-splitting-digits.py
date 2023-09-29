class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num > 0:
            arr.append(str(num%10))
            num //= 10
        
        arr.sort()
        
        return int(arr[0] + arr[-1]) + int(arr[1] + arr[-2])
        
        
        