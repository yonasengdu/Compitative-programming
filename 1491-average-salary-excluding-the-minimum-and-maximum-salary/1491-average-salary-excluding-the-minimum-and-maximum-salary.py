class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum_without_min_max = sum(salary) - sum([salary[0],salary[-1]])
        num_without_min_max = len(salary) -2
        avarage =   sum_without_min_max/num_without_min_max
        return avarage
        