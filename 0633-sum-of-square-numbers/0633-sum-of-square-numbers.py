class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = []
        for num in range(int(sqrt(c))+1):
                 arr.append(num **2)
        left = 0
        right = len(arr)-1
        print(arr)
        while left < right:
            if arr[left] + arr[right] > c:
                right -= 1
            elif arr[left] + arr[right] < c:
                left += 1
            else:
                return True
        print(left,right)
        print(arr)
        if arr[left] + arr[right] == c:
            return True
        return False
            
        