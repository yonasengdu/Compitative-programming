class Solution:
     def totalFruit(self, fruits: List[int]) -> int:
            fruit_count = defaultdict(int)
            left , res, total = 0,0,0
            for right in range(len(fruits)):
                fruit_count[fruits[right]] += 1
                total += 1
                
                while len(fruit_count) > 2:
                    fruit = fruits[left]
                    fruit_count[fruit] -= 1
                    total -= 1
                    left += 1
                    if not fruit_count[fruit]:
                        fruit_count.pop(fruit)
                res = max(res,total)
            return res
            
