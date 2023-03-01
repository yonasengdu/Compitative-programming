class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        # calculate the prefix sum
        # shift each latter 
            
        """
        ans = []
        
        for i in range(1,len(shifts)):
            shifts[~i] += shifts[~i + 1]
            
        print(shifts) 
        for ind in  range(len(shifts)):
            ord_latter = ord(s[ind])
            shift_amount = shifts[ind] % 26
            to_shift = ord_latter + shift_amount
            if to_shift > 122: 
                to_shift =  96 + to_shift % 122
            ans.append(chr(to_shift))
        return "".join(ans)