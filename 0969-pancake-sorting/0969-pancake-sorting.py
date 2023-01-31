class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        right = len(arr)-1
        ans = []
        if sorted(arr) == arr:
            return []
        while right > 0:
            left = 0
            max_ind = arr.index(max(arr[:right+1]))
            ans.append(max_ind+1)
            while left < max_ind:
                arr[left],arr[max_ind] = arr[max_ind],arr[left]
                left += 1
                max_ind -= 1
            temp_right = right
            temp_left = 0
            while temp_left < temp_right:
                arr[temp_left],arr[temp_right] = arr[temp_right],arr[temp_left]
                temp_left += 1
                temp_right -= 1
            ans.append(right+1)
            right -= 1
            print(arr)
        return ans
            
        
        