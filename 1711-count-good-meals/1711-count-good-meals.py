class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        the_power_of_two = {}
        num_good_meals = 0
        length_dilicousness = len(deliciousness)
        num_deliciousness = Counter(deliciousness)
        
       
        
        #loop to create a hash for the power of two from 2**0 to 2**20
        for power in range(22):
            the_power_of_two[power]=2**power
    
            
        #loop to to identify numbert of good meals
        for single_deliciousness in deliciousness:
            num_deliciousness[single_deliciousness]  -= 1 
            for power in range(22):
                temp_difference = the_power_of_two[power] -  single_deliciousness
                if  temp_difference in num_deliciousness :
                    num_good_meals+=num_deliciousness[ temp_difference]
                    
                    
            
             
        return num_good_meals % (10**9 + 7)
                    
                
                
                
        