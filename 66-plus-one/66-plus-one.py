class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            strd = []
            for i in digits:
                strd.append(str(i))
            largestint = str(int("".join((strd))) + 1)
            ls = []
            for i in largestint:
                ls.append(int(i))

            return ls