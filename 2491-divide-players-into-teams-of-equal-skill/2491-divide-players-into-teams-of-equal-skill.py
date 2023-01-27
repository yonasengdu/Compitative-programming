class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        summ = skill[0] + skill[~0]
        result = 0
        for ind in range(len(skill)):
            if skill[ind]+skill[~ind] != summ:
                return -1
            else:
                temp_res = skill[ind] * skill[~ind]
                result += temp_res
        return result//2

                
        
        
        